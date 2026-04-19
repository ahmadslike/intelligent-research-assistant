# 📘 ملف تعلّم Claude Code — اليوم السادس

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم السادس — MCPs (Model Context Protocol)  
**التاريخ:** 18 أبريل 2026  
**المدة الفعلية:** ~2 ساعة  
**المشروع:** Intelligent Research Assistant (RAG + Multi-Agent System)

---

## 🎯 ما الذي تعلمناه اليوم؟

اليوم تعلمنا كيف نعطي Claude Code "أدوات" إضافية تخليه يتصرف بنفسه بدل ما يعطيك تعليمات تنفّذها أنت.

---

### 1. شو هو MCP؟

MCP = Model Context Protocol — بروتوكول يخلي Claude Code يتصل بأدوات خارجية مباشرة.

**بدون MCP:**
```
أنت → تسأل Claude → Claude يقول "افعل كذا" → أنت تنفّذ
```

**مع MCP:**
```
أنت → تسأل Claude → Claude ينفّذ مباشرة بنفسه
```

مثل الفرق بين تطلب من مساعد يوجّهك، أو تعطيه مفاتيح البيت يشتغل بنفسه.

---

### 2. الـMCPs اللي ثبّتناها اليوم

**Filesystem MCP:**
- يقرأ ويكتب ملفات مشروعك مباشرة
- Claude يشوف كل الملفات بدون ما تعطيه شي
- مثّل استخدمناه: طلبنا منه يعرض هيكل المشروع → عمله لحاله

**GitHub MCP:**
- يتعامل مع GitHub مباشرة
- يقدر يقرأ الـcommits والـissues والـPRs

**Context7 MCP:**
- يجيب documentation محدّثة لأي مكتبة
- مهم لأن Claude بعض أحيان يعرف نسخ قديمة
- مثّل استخدمناه: طلبنا docs لـFastAPI → جاب أحدث نسخة وربطها بمشروعنا

---

## 🛠️ الأوامر التي استخدمناها اليوم

**إضافة MCP:**
```powershell
claude mcp add filesystem -- npx @modelcontextprotocol/server-filesystem C:\Users\HP\Desktop\intelligent-research-assistant
claude mcp add github -- npx @modelcontextprotocol/server-github
claude mcp add context7 -- npx @upstash/context7-mcp
```

**عرض MCPs:**
```powershell
claude mcp list
```

**داخل Claude Code:**
```
/mcp    → عرض حالة الـMCPs
/login  → تسجيل دخول لو انقطع
```

---

## 🧪 ما جرّبناه اليوم

**اختبار Filesystem:**
```
List all files in the current project and tell me the structure
```
النتيجة: Claude قرأ كل الملفات وعمل شجرة كاملة للمشروع ✅

**اختبار Context7:**
```
Use context7 to get documentation for FastAPI
```
النتيجة: جاب docs محدّثة وربطها بمشروعنا مباشرة ✅

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو هو MCP وشو الفرق بدونه ومعه؟  
**ج:** أداة/server تخلي Claude ينفّذ بنفسه بدل ما يعطيك تعليمات ✅

**س2:** شو يعمل Filesystem MCP؟  
**ج:** يقرأ ويكتب الملفات مباشرة ✅

**س3:** شو يعمل Context7 وليش مفيد؟  
**ج:** يجيب documentation محدّثة — أفضل من المعلومات القديمة عند Claude ✅

---

## 📊 ملخص سريع

### ✅ ما أتقنته اليوم:
- فهم مفهوم MCP
- تثبيت 3 MCPs مختلفة
- تجربة Filesystem وContext7 فعلياً
- حل مشكلة authentication

### 💡 أهم درس:
MCPs تحوّل Claude من "مستشار" لـ"مساعد فعلي" يتصرف بنفسه.

---

## 📅 التحضير ليوم 7

**موضوع يوم 7:** مراجعة الأسبوع + بناء RAG كامل شغّال

---

**نهاية توثيق اليوم السادس** ✅  
📌 *"MCPs = أيدي Claude في عالمك"*
