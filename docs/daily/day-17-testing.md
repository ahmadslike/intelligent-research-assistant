# 📘 ملف تعلّم Claude Code — اليوم السابع عشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم السابع عشر — Error Handling + Testing  
**التاريخ:** 7 مايو 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

تعلمنا كيف نجعل المشروع قوي ومستقر — tests تكتشف الأخطاء تلقائياً، وtimeout مناسب للمستخدم.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هو pytest؟

pytest = إطار اختبار Python — يشغّل functions تتحقق إن الكود يشتغل صح.

```python
# مثال test بسيط
def test_health():
    result = get_health()
    assert result == {"status": "healthy"}
```

**ليش مهم؟**
لو عدّلت كود في المستقبل وكسرت شي → الـtests تخبرك فوراً بدل ما تكتشفه المستخدم.

---

### 2. شو يعني ASGITransport؟

```python
from httpx import ASGITransport, AsyncClient

transport = ASGITransport(app=app)
async with AsyncClient(transport=transport, base_url="http://test") as client:
    # نختبر بدون ما نشغّل uvicorn!
```

بدل ما نشغّل الـserver ونرسل requests حقيقية → نوصّل httpx مباشرة لـFastAPI في الذاكرة.

**النتيجة:** tests أسرع وما تحتاج server شغّال.

---

### 3. الـTests اللي كتبناها

```python
# اختبار 1: صحة الـAPI
async def test_health(client):
    r = await client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "healthy"}

# اختبار 2: إضافة مستند
async def test_rag_add(client):
    r = await client.post("/rag/add", json={"text": "نص تجريبي", "metadata": {}})
    assert r.json()["status"] == "added"
    assert isinstance(r.json()["doc_id"], str)

# اختبار 3: البحث
async def test_rag_search(client):
    r = await client.post("/rag/search", json={"query": "نص تجريبي"})
    assert isinstance(r.json()["results"], list)

# اختبار 4: العدد
async def test_rag_count(client):
    r = await client.get("/rag/count")
    assert isinstance(r.json()["count"], int)
```

**النتيجة:**
```
test_health   PASSED ✅
test_rag_add  PASSED ✅
test_rag_search PASSED ✅
test_rag_count PASSED ✅
4 passed in 21.92s ✅
```

---

### 4. شو هو pytest.ini؟

ملف إعدادات pytest — أضفنا:
```ini
[pytest]
asyncio_mode = auto
```

هاد يخلي pytest يفهم الـasync fixtures تلقائياً بدون إعدادات إضافية في كل ملف.

---

### 5. تعديل الـTimeout لـ120 ثانية

```typescript
// قبل
const timeoutId = setTimeout(() => controller.abort(), 60_000);  // 60 ثانية

// بعد
const timeoutId = setTimeout(() => controller.abort(), 120_000); // 120 ثانية
```

**السبب:** البحث الحقيقي يأخذ 40-70 ثانية. الـ60 ثانية كانت تقطع البحث وهو على وشك يكمل. الـ120 ثانية تعطيه مساحة كافية.

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو pytest وليش مهم؟  
**ج:** إطار اختبار — يكتشف الأخطاء تلقائياً لو كسرت شي بالمستقبل ✅

**س2:** شو يعني AbortController والـ120 ثانية؟  
**ج:** يوقف الطلب تلقائياً بعد 120 ثانية — غيّرناه من 60 عشان ما يقطع البحث قبل ما يخلص ✅

**س3:** ليش pytest.ini مع asyncio_mode = auto؟  
**ج:** عشان pytest يفهم الـasync fixtures تلقائياً ✅

---

## 📅 التحضير ليوم 18

**موضوع يوم 18:** Deployment — Railway (Backend) + Vercel (Frontend)

---

**نهاية توثيق اليوم السابع عشر** ✅  
📌 *"Tests = حارس المشروع — يكتشف الأخطاء قبل المستخدم"*
