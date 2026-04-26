# 📘 ملف تعلّم Claude Code — اليوم التاسع

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم التاسع — Sub-Agents + Researcher Agent  
**التاريخ:** 26 أبريل 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 8/10

---

## 🎯 شو تعلمنا اليوم؟

اليوم بنينا أول "مساعد ذكي" في مشروعنا — الـResearcher Agent. بس قبل ما نشرح الكود، خلينا نفهم كل مفهوم من الصفر.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هو Sub-Agent؟

تخيّل مطعم كبير:
- **بدون agents:** طباخ وحد يطبخ + يخدم + يحاسب + ينظّف = بطيء ومتعب
- **مع agents:** طباخ متخصص، نادل متخصص، محاسب متخصص = كل وحد يتقن شغلته

في مشروعنا نفس الفكرة:
```
Researcher Agent → يبحث عن مصادر
Reader Agent     → يقرأ المصادر
Analyst Agent    → يحلل المعلومات  
Writer Agent     → يكتب التقرير
```

**ليش أفضل من كود وحد طويل؟**
- كل agent صغير = أسهل تصليح لو صار خطأ
- كل agent يتقن مهمته = نتائج أفضل
- تقدر تبدّل agent بآخر بدون تغيير كل شي

---

### 2. شو هو Class في Python؟

```python
class ResearcherAgent:
```

Class = "قالب" لإنشاء كائنات. مثل قالب الكيكة — تستخدمه لتصنع كيكات كثيرة.

```python
# أنشأنا "قالب" اسمه ResearcherAgent
class ResearcherAgent:
    async def research(self, topic: str):
        # هنا الوصفة

# استخدمنا القالب لنصنع agent
agent = ResearcherAgent()  # مثل "خبزنا كيكة" من القالب
result = await agent.research("AI")  # استخدمنا الكيكة
```

---

### 3. شو يعني async def؟

```python
async def research(self, topic: str):
```

تخيّل نادل في مطعم:

**بدون async (def عادي):**
```
النادل يأخذ طلب طاولة 1
ينتظر الطعام يُطبخ (5 دقائق)
يوصّل الطعام
ثم يروح لطاولة 2
```
= بطيء جداً

**مع async:**
```
النادل يأخذ طلب طاولة 1
يذهب للمطبخ ويرجع (ما ينتظر)
يأخذ طلب طاولة 2
يأخذ طلب طاولة 3
لما يخلص الطعام يوصّله
```
= سريع جداً

في كودنا، `async def research` يعني: "أثناء ما ننتظر الإنترنت يرد، نكمل أشياء ثانية".

---

### 4. شو يعني await؟

```python
await client.get(source.url, timeout=5.0)
```

`await` = "انتظر هاي العملية تخلص قبل ما تكمل، بس خلّي غيرك يشتغل بالانتظار".

مثل: "انتظر هنا لما الباب يفتح، بس ما تسكّر عالناس الثانيين"

---

### 5. شو هو Pydantic Model؟

```python
class Source(BaseModel):
    title: str
    url: str
    summary: str
```

Pydantic Model = "عقد رسمي" للبيانات. يقول:
- `title` لازم يكون نص (str)
- `url` لازم يكون نص
- `summary` لازم يكون نص

لو حاولت تعطيه رقم بدل نص → يطلع خطأ تلقائياً.

**ليش مفيد؟**
```python
# بدون Pydantic - ممكن تغلط بدون ما تعرف
source = {"title": 123, "url": None}  # غلط بس ما يطلع خطأ

# مع Pydantic - يكتشف الغلط فوراً
source = Source(title=123, url=None)  # خطأ واضح فوراً!
```

---

### 6. شرح الكود كامل سطر بسطر

```python
import httpx
```
= "جيب مكتبة httpx" — هي مكتبة لعمل طلبات للإنترنت (مثل متصفح بس في الكود)

```python
from pydantic import BaseModel
```
= "جيب BaseModel من مكتبة pydantic" — عشان نقدر نعمل models

```python
class Source(BaseModel):
    title: str    # عنوان المصدر، لازم نص
    url: str      # رابط المصدر، لازم نص
    summary: str  # ملخص، لازم نص
```
= "أنشئ قالب للمصدر الوحد"

```python
class ResearchResult(BaseModel):
    topic: str           # موضوع البحث
    sources: list[Source]  # قائمة من المصادر (كل وحد Source)
```
= "أنشئ قالب للنتيجة الكاملة — موضوع + قائمة مصادر"

```python
MOCK_SOURCES = [
    {
        "title": "Introduction to {topic} - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/{topic_slug}",
        "summary": "A comprehensive overview...",
    },
    ...
]
```
= "قائمة مصادر وهمية (mock) نستخدمها للاختبار". الـ`{topic}` هو placeholder رح يتبدّل بالموضوع الحقيقي.

```python
class ResearcherAgent:
```
= "أنشئ قالب للـResearcher Agent"

```python
def _build_sources(self, topic: str) -> list[Source]:
```
= "دالة خاصة (الـ_ في البداية تعني خاصة) تبني قائمة المصادر"
- `self` = "الـagent نفسه"
- `topic: str` = "الموضوع، لازم نص"
- `-> list[Source]` = "ترجع قائمة من Source"

```python
topic_slug = topic.replace(" ", "_")
```
= "حوّل المسافات لـ_" مثل "artificial intelligence" → "artificial_intelligence" (عشان تشتغل في URLs)

```python
async def research(self, topic: str) -> ResearchResult:
```
= "دالة async (سريعة) تستقبل موضوع وترجع ResearchResult"

```python
sources = self._build_sources(topic)
```
= "استخدم الدالة الخاصة لبناء قائمة المصادر"

```python
async with httpx.AsyncClient() as client:
```
= "افتح اتصال بالإنترنت" — مثل فتح متصفح

```python
    for source in sources:
        try:
            await client.get(source.url, timeout=5.0)
        except Exception:
            pass
```
= "لكل مصدر، حاول تفتح رابطه. لو فشل، تجاهل الخطأ وكمّل"
- `timeout=5.0` = "انتظر 5 ثوان بس، لو ما رد تجاهل"
- `pass` = "لا تعمل شي لو صار خطأ"

```python
return ResearchResult(topic=topic, sources=sources)
```
= "ارجع النتيجة النهائية"

---

### 7. كيف تكتبه لحالك المرة الجاية؟

لو بدك تعمل agent جديد من الصفر، اتبع هاد الترتيب:

**الخطوة 1:** حدد شو يستقبل وشو يرجع
```python
# يستقبل: موضوع (نص)
# يرجع: قائمة مصادر
```

**الخطوة 2:** أنشئ الـPydantic models
```python
class MyInput(BaseModel):
    topic: str

class MyOutput(BaseModel):
    results: list[str]
```

**الخطوة 3:** أنشئ الـClass
```python
class MyAgent:
    async def run(self, input: MyInput) -> MyOutput:
        # منطق الـagent هنا
        return MyOutput(results=[...])
```

**الخطوة 4:** اختبر
```python
agent = MyAgent()
result = await agent.run(MyInput(topic="test"))
```

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو Sub-Agent وليش نستخدمه؟  
**ج:** مساعد متخصص بمهمة وحدة — أفضل من كود طويل يعمل كل شي ✅

**س2:** شو يعني async def؟  
**ج:** دالة سريعة — ما تنتظر عملية تخلص قبل ما تبدأ غيرها ✅

**س3:** شو هو ResearchResult؟  
**ج:** Pydantic model = عقد رسمي لشكل البيانات اللي يرجعها الـagent ✅

---

## 📊 ملخص سريع للمراجعة

| المفهوم | الشرح بجملة وحدة |
|---------|-----------------|
| Sub-Agent | مساعد متخصص بمهمة وحدة |
| Class | قالب لإنشاء كائنات |
| async def | دالة سريعة ما تنتظر |
| await | انتظر هاي العملية بس خلّي غيرك يشتغل |
| BaseModel | عقد رسمي لشكل البيانات |
| MOCK_SOURCES | بيانات وهمية للاختبار |
| timeout=5.0 | انتظر 5 ثوان بس |
| pass | تجاهل الخطأ وكمّل |

---

## ⚠️ درس مهم من اليوم

لو ما فهمت شيئاً، قل "ما فهمت" فوراً. أفضل تسأل 10 مرات من إنك تنسخ وتلصق بدون فهم. الفهم هو الهدف مش إنهاء المهام.

---

## 📅 التحضير ليوم 10

**موضوع يوم 10:** بناء Reader + Analyst + Writer Agents

**سؤال للتفكير الليلة:**
لو بدك تعمل Reader Agent يقرأ نص ويستخرج أهم 3 نقاط — شو الـinput وشو الـoutput؟

---

**نهاية توثيق اليوم التاسع** ✅  
📌 *"الفهم أهم من السرعة — اسأل دائماً"*
