# اختبارات لنقاط الـ API الأساسية في الباك-إند
# تستخدم httpx مع ASGITransport — يعني ما بنحتاج نشغّل uvicorn
import sys
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient

# نضيف مجلد backend للـ path حتى تشتغل الاستيرادات الموجودة فيه
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))
from main import app  # noqa: E402


# fixture مشترك لإنشاء client async موصول مباشرة بتطبيق FastAPI
@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health(client):
    # نقطة الفحص الصحي — لازم ترجع status: healthy
    r = await client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "healthy"}


@pytest.mark.asyncio
async def test_rag_add(client):
    # إضافة وثيقة جديدة — لازم نستلم doc_id و status="added"
    r = await client.post("/rag/add", json={"text": "نص تجريبي للاختبار", "metadata": {"source": "test"}})
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "added"
    assert isinstance(body["doc_id"], str) and body["doc_id"]


@pytest.mark.asyncio
async def test_rag_search(client):
    # البحث — لازم يرجّع قائمة (قد تكون فارغة لكن لازم تكون list)
    r = await client.post("/rag/search", json={"query": "نص تجريبي"})
    assert r.status_code == 200
    assert isinstance(r.json()["results"], list)


@pytest.mark.asyncio
async def test_rag_count(client):
    # عدّ الوثائق — لازم يكون رقم صحيح غير سالب
    r = await client.get("/rag/count")
    assert r.status_code == 200
    count = r.json()["count"]
    assert isinstance(count, int) and count >= 0
