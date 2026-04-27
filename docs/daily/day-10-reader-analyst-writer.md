# 📘 ملف تعلّم Claude Code — اليوم العاشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم العاشر — Reader + Analyst + Writer Agents  
**التاريخ:** 27 أبريل 2026  
**المدة الفعلية:** ~3 ساعات  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

اليوم أكملنا الـpipeline كامل — 4 agents يشتغلوا مع بعض بالترتيب وينتجوا تقرير كامل من موضوع وحد.

---

## 📚 شرح كل Agent بالتفصيل

---

### 1. ReaderAgent — القارئ

**مهمته:** يأخذ نص ورابط، يرسله للـAI، يطلب منه استخراج 3 نقاط رئيسية.

**Input (شو يستقبل):**
```python
text: str  # النص اللي يقرأه
url: str   # من وين جاء النص
```

**Output (شو يرجع):**
```python
class ReaderResult(BaseModel):
    key_points: list[str]  # قائمة من 3 نقاط رئيسية
    source_url: str        # الرابط الأصلي
```

**كيف يشتغل خطوة بخطوة:**

```python
# الخطوة 1: يبني الـprompt (الطلب للـAI)
prompt = f"""
Read the following text and extract exactly 3 key points.
Text: {text}
"""

# الخطوة 2: يرسل الطلب لـOpenRouter
response = await self._client.chat.completions.create(
    model=os.getenv("DEFAULT_MODEL"),
    messages=[{"role": "user", "content": prompt}]
)

# الخطوة 3: يحلل الرد ويستخرج النقاط
# مثلاً الرد: "1. AI transforms healthcare\n2. ML improves accuracy\n3. ..."
# يحوّله لـlist: ["AI transforms...", "ML improves...", "..."]
```

---

### 2. AnalystAgent — المحلّل

**مهمته:** يأخذ نتائج الـReader من كل المصادر، يقارنها، يلاقي التناقضات، يكتب ملخص.

**Input (شو يستقبل):**
```python
reader_results: list[ReaderResult]  # قائمة من نتائج الـReader
```

**Output (شو يرجع):**
```python
class AnalystResult(BaseModel):
    summary: str              # ملخص كل المصادر
    contradictions: list[str] # قائمة التناقضات
```

**كيف يشتغل خطوة بخطوة:**

```python
# الخطوة 1: يجمع كل النقاط من كل المصادر
all_points = ""
for result in reader_results:
    all_points += f"Source: {result.source_url}\n"
    for point in result.key_points:
        all_points += f"- {point}\n"

# الخطوة 2: يبني prompt يطلب من AI تحليل كل النقاط
prompt = f"""
Analyze these key points from multiple sources:
{all_points}

Write:
SUMMARY: [ملخص شامل]
CONTRADICTIONS: [قائمة التناقضات]
"""

# الخطوة 3: يحلل الرد ويستخرج SUMMARY و CONTRADICTIONS
```

**ليش مهم؟**
لو عندك 3 مصادر تتكلم عن AI:
- مصدر 1: "AI خطر على الوظائف"
- مصدر 2: "AI يخلق وظائف جديدة"
- مصدر 3: "AI محايد"

الـAnalyst يكتشف التناقض ويذكره في التقرير!

---

### 3. WriterAgent — الكاتب

**مهمته:** يأخذ كل شي (الموضوع + تحليل الـAnalyst + قائمة المصادر) ويكتب تقرير احترافي.

**Input (شو يستقبل):**
```python
topic: str                    # الموضوع
analyst_result: AnalystResult # نتيجة التحليل
sources: list[Source]         # قائمة المصادر الأصلية
```

**Output (شو يرجع):**
```python
class WriterResult(BaseModel):
    report: str  # التقرير الكامل
```

**كيف يشتغل:**

```python
# يبني prompt يطلب من AI كتابة تقرير 300-500 كلمة
prompt = f"""
Write a structured report about: {topic}

Summary: {analyst_result.summary}
Contradictions: {analyst_result.contradictions}

Sources:
[1] {sources[0].url}
[2] {sources[1].url}
[3] {sources[2].url}

Write a report with introduction, body, conclusion, and [1][2][3] citations.
"""
```

---

### 4. شو هو OpenRouter وليش `openrouter/free`؟

**OpenRouter** = موقع يجمع نماذج AI كثيرة في مكان وحد. بدل ما تشترك بكل شركة لحالها (Google, Meta, Mistral...) تشترك بـOpenRouter وتوصل لكلهم.

**ليش غيّرنا النموذج؟**
```
gemini-2.0-flash-exp:free  → انتهى وما عاد متاح (deprecated فبراير 2026)
gemini-2.5-flash-preview:free → اسم غلط
openrouter/free → يختار تلقائياً أي نموذج مجاني متاح ✅
```

`openrouter/free` = "أعطيني أي نموذج مجاني شغّال الحين"

---

### 5. شرح AsyncOpenAI بالتفصيل

```python
from openai import AsyncOpenAI

# ننشئ client يتصل بـOpenRouter بدل OpenAI
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",  # عنوان OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),  # مفتاحنا
)
```

**ليش AsyncOpenAI وليش OpenAI العادي؟**
- `OpenAI` = ينتظر الرد قبل ما يكمل (بطيء)
- `AsyncOpenAI` = يكمل غيره بالانتظار (سريع)

لأن مشروعنا رح يستدعي الـAPI 3+ مرات لكل طلب، `async` أسرع بكثير.

---

### 6. شرح الـPipeline كامل

```python
# الخطوة 1: Researcher يبحث
researcher = ResearcherAgent()
research = await researcher.research("artificial intelligence")
# ← ينتج: 3 مصادر (Wikipedia, Britannica, arXiv)

# الخطوة 2: Reader يقرأ كل مصدر
reader = ReaderAgent()
reader_results = []
for source in research.sources:
    result = await reader.read("نص المصدر", source.url)
    reader_results.append(result)
# ← ينتج: 3 نتائج، كل واحد فيه 3 نقاط

# الخطوة 3: Analyst يحلل كل النتائج
analyst = AnalystAgent()
analysis = await analyst.analyse(reader_results)
# ← ينتج: ملخص + قائمة تناقضات

# الخطوة 4: Writer يكتب التقرير
writer = WriterAgent()
final = await writer.write("artificial intelligence", analysis, research.sources)
# ← ينتج: تقرير 300-500 كلمة مع citations
```

**النتيجة الفعلية اليوم:**
```
✅ Researcher: 3 sources
✅ Reader: 3 results
✅ Analyst summary: "AI is significantly transforming healthcare..."
✅ Writer report: "Artificial Intelligence: A Transformation of Healthcare..."
```

---

## 🐛 المشاكل اللي واجهناها وحلولها

**المشكلة 1:** `ModuleNotFoundError: No module named 'openai'`  
**السبب:** openai مش مثبّت في الـvenv  
**الحل:** `pip install openai==1.50.0`

**المشكلة 2:** `from backend.agents.reader import ReaderResult` — خطأ  
**السبب:** لما تكون داخل `backend/`، الـimport يبدأ من هنا  
**الحل:** `from agents.reader import ReaderResult`  
**القاعدة:** موقعك يحدد كيف تكتب الـimport

**المشكلة 3:** `No endpoints found for google/gemini-2.0-flash-exp:free`  
**السبب:** النموذج deprecated  
**الحل:** غيّرنا لـ`openrouter/free`

---

## 📊 ملخص سريع

| Agent | Input | Output | يستخدم AI؟ |
|-------|-------|--------|-----------|
| Researcher | topic | 3 sources | ❌ (mock) |
| Reader | text + url | 3 key points | ✅ |
| Analyst | list of ReaderResults | summary + contradictions | ✅ |
| Writer | topic + analysis + sources | full report | ✅ |

### ✅ ما أتقنته اليوم:
- فهم كيف يتواصل كل agent مع التالي
- AsyncOpenAI مع OpenRouter
- استخراج معلومات من رد الـAI (parsing)
- حل مشاكل الـimports
- تغيير النموذج لما يتوقف عن العمل

### 💡 أهم درس:
النماذج المجانية تتغيّر — `openrouter/free` الأأمن لأنه يختار تلقائياً.

### 🎯 التحدي الأكبر:
فهم الـimports — متى تكتب `from agents.x` ومتى `from backend.agents.x` حسب مكانك.

---

## 📅 التحضير ليوم 11

**موضوع يوم 11:** Skills — بناء skill اسمه `academic-writer`

**سؤال للتفكير:**
شو الفرق بين Custom Slash Command اللي عملناه يوم 8 وبين Skill؟

---

**نهاية توثيق اليوم العاشر** ✅  
📌 *"4 agents + pipeline كامل = مشروع AI حقيقي"*
