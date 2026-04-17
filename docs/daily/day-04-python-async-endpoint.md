# 📘 ملف تعلّم Claude Code — اليوم الرابع

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الرابع — Python Refresh + Type Hints + Async + Research Endpoint  
**التاريخ:** 16 أبريل 2026  
**المدة الفعلية:** ~3 ساعات  
**المشروع:** Intelligent Research Assistant (RAG + Multi-Agent System)

---

## 🎯 ما الذي تعلمناه اليوم؟

اليوم تعلمنا Python بالشكل اللي يحتاجه مشروعنا — وبنينا أول endpoint حقيقي يقبل بيانات ويرد عليها. لأول مرة أرسلنا request وأخذنا response حقيقي!

---

### 1. شو هي Type Hints؟

Python عادةً ما تحدد نوع المتغير — تكتب أي شي وتشتغل. بس مع FastAPI لازم تحدد النوع عشان يفهم شو يقبل وشو يرفض.

```python
# بدون type hints — Python العادية
def greet(name):
    return "Hello " + name

# مع type hints — FastAPI style
def greet(name: str) -> str:
    return "Hello " + name
```

**الأنواع الأساسية:**
- `str` = نص
- `int` = رقم صحيح
- `float` = رقم عشري
- `bool` = True/False
- `list` = قائمة

---

### 2. شو هو Async/Await؟

تخيّل نادل في مطعم:

**بدون async (بطيء):**
النادل يأخذ طلب → يذهب للمطبخ → **ينتظر** الطعام → يرجع → يأخذ طلب ثاني

**مع async (سريع):**
النادل يأخذ طلب → يذهب للمطبخ → **بينما الطعام يُطبخ** يأخذ طلب ثاني ويخدم طاولة أخرى

```python
# بدون async - ينتظر كل API call
def get_research(topic: str):
    result = call_ai_api(topic)  # الكود يتوقف هنا
    return result

# مع async - يكمل غيره بالانتظار
async def get_research(topic: str):
    result = await call_ai_api(topic)  # يكمل غيره
    return result
```

مشروعنا يحتاج async لأنه رح يستدعي APIs خارجية كثيرة في نفس الوقت.

---

### 3. شو هو BaseModel (Pydantic)؟

يحدد "شكل" البيانات — مثل نموذج رسمي فيه حقول محددة. لو أرسلت بيانات ناقصة أو خاطئة، Pydantic يرفضها تلقائياً.

```python
from pydantic import BaseModel

class ResearchRequest(BaseModel):
    topic: str           # نص إلزامي
    max_sources: int = 5 # رقم، افتراضي 5

class ResearchResponse(BaseModel):
    topic: str
    status: str
    message: str
```

---

### 4. شو هو POST Endpoint؟

GET = "أعطني معلومات" (مثل فتح صفحة ويب)
POST = "خذ هاي البيانات واعمل شي" (مثل إرسال نموذج)

```python
@app.post("/research", response_model=ResearchResponse)
async def start_research(request: ResearchRequest):
    return ResearchResponse(
        topic=request.topic,
        status="received",
        message=f"Research request for '{request.topic}' received."
    )
```

---

### 5. شو هو 422 Validation Error؟

لو أرسلت request بدون `topic` أو بنوع خاطئ، FastAPI يرد تلقائياً:
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "topic"],
      "msg": "Field required"
    }
  ]
}
```

ما تحتاج تكتب أي كود للتحقق — Pydantic يتكفل بكل شي.

---

## 🛠️ كل الأوامر التي استخدمناها اليوم

---

**الأمر:**
```powershell
code .
```
**وظيفته:** يفتح VS Code في المجلد الحالي  
**ملاحظة:** نقطة `.` تعني "المجلد الحالي"

---

**الأمر:**
```powershell
cd backend
uvicorn main:app --reload
```
**وظيفته:** يشغّل FastAPI server مع إعادة تشغيل تلقائية  
**الناتج:** `Uvicorn running on http://127.0.0.1:8000`

---

## 🧪 ما جربناه اليوم

### Swagger UI (/docs)
فتحنا `http://127.0.0.1:8000/docs` وجربنا:

**Request أرسلناه:**
```json
{
  "topic": "artificial intelligence",
  "max_sources": 3
}
```

**Response استلمناه:**
```json
{
  "topic": "artificial intelligence",
  "status": "received",
  "message": "Research request for 'artificial intelligence' received. Processing 3 sources."
}
```

**Status code:** 200 OK ✅

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو الفرق بين `def` و `async def`؟  
**ج:** `async def` يكمل غيره بالانتظار — أسرع للـAPIs الخارجية ✅

**س2:** شو هو `BaseModel`؟  
**ج:** من pydantic — يحدد شكل البيانات المطلوبة ونوعها ✅

**س3:** لو أرسلت request بدون `topic`، شو يصير؟  
**ج:** 422 Validation Error — FastAPI يرفض تلقائياً ✅

---

## 📊 ملخص سريع

### هيكل الـEndpoint:
```
POST /research
  ↓ يقبل: ResearchRequest (topic, max_sources)
  ↓ يتحقق: Pydantic
  ↓ يعالج: async function
  ↓ يرجع: ResearchResponse (topic, status, message)
```

### ✅ ما أتقنته اليوم:
- Type hints في Python
- Async/Await مفهوم ومطبّق
- BaseModel لتحديد شكل البيانات
- POST endpoint كامل
- تجربة API من Swagger UI
- VS Code مع Python extension

### 🎯 التحدي الأكبر:
فهم async — لكن مثال النادل وضّح الفكرة تماماً.

### 💡 أهم درس:
FastAPI + Pydantic = validation تلقائي بدون كود إضافي.

---

## 📅 التحضير ليوم 5

**موضوع يوم 5:** Embeddings + ChromaDB + أول semantic search

**ما أحتاج أراجعه:**
- الفرق بين GET و POST
- شو يعني `async def` وليش أهم من `def` في مشروعنا

---

**نهاية توثيق اليوم الرابع** ✅  
📌 *"API يشتغل = مشروع حقيقي بدأ"*
