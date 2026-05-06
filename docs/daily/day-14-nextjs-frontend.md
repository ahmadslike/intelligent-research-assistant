# 📘 ملف تعلّم Claude Code — اليوم الرابع عشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الرابع عشر — Next.js Frontend  
**التاريخ:** 6 مايو 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

اليوم بنينا أول واجهة بصرية للمشروع — صفحة ويب عربية تقدر فيها تكتب موضوع وتستلم تقرير كامل.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هو Next.js؟

Next.js = إطار عمل JavaScript لبناء واجهات ويب احترافية. مثل FastAPI للـPython، Next.js للـJavaScript.

**ليش Next.js وليس HTML عادي؟**
- يدعم TypeScript (أنواع للبيانات)
- Tailwind CSS جاهز للتصميم السريع
- تحديث تلقائي لما تعدّل الكود

---

### 2. شو يعني 'use client'؟

```typescript
'use client'  // ← لازم يكون أول سطر
import { useState } from "react";
```

Next.js بشكل افتراضي يشغّل الكود على الـserver. لما نستخدم:
- `useState` (حالة التطبيق)
- `fetch` (طلبات للـAPI)
- أي تفاعل مع المستخدم

لازم نقول `'use client'` — يعني "هاد الكود يشتغل في متصفح المستخدم مش على الـserver".

---

### 3. شو هو CORS وليش كان المشكلة؟

**CORS** = Cross-Origin Resource Sharing

المتصفح بيحمي المستخدم — ما يسمح لصفحة على port معين تتصل بـserver على port ثاني بدون إذن صريح.

```
Frontend: http://localhost:3000
Backend:  http://localhost:8000
↑ منفصلين → المتصفح يحجب الاتصال بدون CORS
```

**الحل:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # السماح للـFrontend
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 4. شرح كود الـFrontend

```typescript
// حالة التطبيق — 4 متغيرات
const [topic, setTopic] = useState("");           // الموضوع اللي يكتبه المستخدم
const [loading, setLoading] = useState(false);   // هل نحن بانتظار الـAPI؟
const [result, setResult] = useState(null);      // النتيجة النهائية
const [error, setError] = useState(null);        // رسالة الخطأ لو صار
```

**شو يعني useState؟**
مثل متغير عادي بس لما يتغيّر → الصفحة تتحدث تلقائياً.

```typescript
// لما المستخدم يضغط "ابحث"
async function handleSubmit(e) {
  e.preventDefault();           // منع إعادة تحميل الصفحة
  setLoading(true);             // عرض "جارٍ البحث..."
  
  const res = await fetch("http://localhost:8000/research/full", {
    method: "POST",
    body: JSON.stringify({ topic })
  });
  
  const data = await res.json();
  setResult(data);              // عرض النتيجة
  setLoading(false);            // إخفاء "جارٍ البحث..."
}
```

---

### 5. الفرق بين Frontend وBackend

| Frontend | Backend |
|----------|---------|
| ما يراه المستخدم | المحرك الخفي |
| Next.js + TypeScript | FastAPI + Python |
| يشتغل في المتصفح | يشتغل على الـserver |
| port 3000 | port 8000 |
| يرسل طلبات | يستقبل ويعالج |

---

## 🧪 النتيجة الفعلية

كتبنا "الذكاء الاصطناعي في الطب" وبعد دقيقتين استلمنا:
- تقرير 4 أقسام كامل بالإنجليزي ✅
- 3 مصادر مع روابط ✅
- Citations [1][2][3] ✅

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو CORS وليش كان محتاجينه؟  
**ج:** حماية المتصفح من الاتصال بين ports مختلفة — أضفنا إذن صريح ✅

**س2:** شو يعني 'use client'؟  
**ج:** يخبر Next.js إن الكود يشتغل في المتصفح مش على الـserver ✅

**س3:** شو الفرق بين Frontend وBackend؟  
**ج:** Frontend = الواجهة، Backend = المحرك الخفي ✅

---

## 📅 التحضير ليوم 15

**موضوع يوم 15:** تحسين RAG — Chunking أذكى ونتائج أدق

---

**نهاية توثيق اليوم الرابع عشر** ✅  
📌 *"اليوم صار عندنا Full-Stack AI App حقيقي شغّال!"*
