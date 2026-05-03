# 📘 ملف تعلّم Claude Code — اليوم الحادي عشر

**الطالب:** أحمد سليق  
**المدرّب:** Claude Sonnet 4.6  
**اليوم:** اليوم الحادي عشر — Skills  
**التاريخ:** 3 مايو 2026  
**المدة الفعلية:** ~2 ساعة  
**تقييم اليوم:** 9/10

---

## 🎯 شو تعلمنا اليوم؟

تعلمنا كيف نعمل Skills — مهارات نعلّمها لـClaude Code يستخدمها تلقائياً لما يحتاجها.

---

## 📚 المفاهيم بالتفصيل

### 1. شو هي Skill؟

Skill = ملف Markdown يعلّم Claude طريقة معينة للتفكير أو الكتابة أو العمل.

**الفرق عن Custom Slash Command:**

| | Custom Slash Command | Skill |
|--|---------------------|-------|
| **متى يشتغل؟** | لما أنت تستدعيه يدوياً `/test-rag` | تلقائياً لما Claude يحتاجه |
| **مثال** | `/deploy-check` تكتبه أنت | academic-writer يشتغل وحده لما تطلب تقرير |
| **وين يتحفظ؟** | `.claude/commands/` | `.claude/skills/` |

---

### 2. شو هي Hedging Language؟

كلمات تخفّف من قوة الادعاء في الكتابة الأكاديمية — لأن العلم ما يقول "مؤكد 100%" إلا لما عنده دليل قاطع.

```
❌ "AI replaces doctors"
✅ "AI may augment doctors"

❌ "This proves that..."
✅ "This suggests that..."

❌ "AI will cure cancer"
✅ "AI shows promise in treating cancer"
```

**ليش مهم؟** الكتابة الأكاديمية الصادقة تعترف بحدود المعرفة.

---

### 3. شو بنينا اليوم؟

ملف `.claude/skills/academic-writer.md` يحتوي على:

1. **قواعد الكتابة الأكاديمية:**
   - لهجة رسمية بضمير الغائب (third person)
   - لا اختصارات (don't → do not)
   - Hedging language دائماً
   - Citations بأسلوب موحّد

2. **Template جاهز:**
   - Abstract
   - Introduction
   - Background
   - Key Findings
   - Analysis
   - Conclusion
   - References

3. **أمثلة جيدة وسيئة:**
   - 5 مقارنات توضّح الفرق

4. **متى يفعّل نفسه:**
   - عند كتابة تقارير بحثية
   - عند طلب ملخص أكاديمي
   - **لا** يفعّل في المحادثة العادية

---

## 🧪 النتيجة الفعلية

طلبنا من Claude كتابة ملخص أكاديمي عن AI في الطب — النتيجة كانت:
- تقرير 5 أقسام كامل ✅
- Citations لمقالات علمية حقيقية ✅
- Hedging language في كل الادعاءات ✅
- References list كاملة ✅

---

## 🧠 أسئلة الاختبار + الأجوبة

**س1:** شو الفرق بين Skill وSlash Command؟  
**ج:** Skill تلقائية، Slash Command يدوية ✅

**س2:** وين تتحفظ Skills؟  
**ج:** `.claude/skills/` ✅

**س3:** شو Hedging Language؟  
**ج:** كلمات تخفّف الادعاء: "may", "suggests", "shows promise" ✅

---

## 📅 التحضير ليوم 12

**موضوع يوم 12:** Hooks — أتمتة تلقائية قبل وبعد كل عملية

---

**نهاية توثيق اليوم الحادي عشر** ✅  
📌 *"Skills = ذكاء دائم، Commands = أدوات عند الطلب"*
