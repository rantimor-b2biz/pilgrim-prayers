# CLARITY Integration - Complete Setup Guide

## מה שהושלם

✅ **CLARITY Integration Script** - סקריפט Python שמחבר ל-Microsoft Clarity API
✅ **Configuration File** - קובץ להחזקת API key ו-Project ID
✅ **Weekly Report Integration** - CLARITY נכלל כעת בדוח השבועי
✅ **Updated Paid Search Agent** - סוכן עודכן עם CLARITY כמקור נתונים

---

## 📊 מה CLARITY תעשה בשבילך

כל שבוע, הסקריפט יוציא:

### 1. **Heatmaps** - מפות חום של הקליקים
- איפה משתמשים קוללקים?
- כמה עמוק הם גוללים?
- איזה אלמנטים מזניחים?

**למודעות:** אם משתמשים מגיעים לדף ולא רואים את ה-CTA שלך, תנסה להעביר אותו.

### 2. **Session Recordings** - הקלטות ממשתמשים
- כמה זמן אנשים מבלים בעמוד?
- מה הם עושים (קליק, scroll, typing)?
- מי המשתמשים המעורבים ביותר?

**למודעות:** אם מסשנים בעלי score גבוה משתמשים מילה X, זה עדות אמיתית שהמילה עובדת!

### 3. **Conversion Funnels** - איפה אנשים מתאבדים
- שלב 1: נחתו בעמוד (100%)
- שלב 2: לחצו על "תקרא עוד" (45% טיפול)
- שלב 3: הגיעו לטופס (20% טיפול)
- שלב 4: שלחו תלילה (5% טיפול)

**למודעות:** אם 80% מצטטים בשלב 3, בדוק מה בטופס - maybe הטקסט של המודעה לא תואם?

---

## 🚀 כדי להתחיל

### צעד 1: קבל את CLARITY Credentials

1. לך ל **https://clarity.microsoft.com/**
2. בחר את הפרויקט של Pilgrim Prayers
3. לך ל **Settings → Project settings**
4. Copy את ה-**Project ID** (למשל: `1234567890`)
5. לך ל **Settings → API & integrations**
6. Copy את ה-**API Token** (או שיצור אחד חדש)

### צעד 2: הכנס את זה בקובץ Config

תאריך קובץ זה:
```
B-brain/google-auth/clarity-config.json
```

תחליף את זה:
```json
{
  "api_key": "YOUR_CLARITY_API_KEY_HERE",
  "project_id": "YOUR_PROJECT_ID_HERE"
}
```

עם זה (דוגמה):
```json
{
  "api_key": "sk_live_xyz123...",
  "project_id": "1234567890"
}
```

**חשוב:** אל תשתף קובץ זה! זה מסד שלך.

### צעד 3: בדוק את החיבור

הרץ:
```bash
cd "C:\Users\rant\Documents\ran-workspace\Pilgrim Prayers\T-tools\scripts"
python clarity_integration.py
```

אם זה עובד, תראה:
```
[OK] Fetched heatmap data: 5 pages tracked
[OK] Fetched 42 top engagement sessions
[OK] Fetched funnel analysis: 3 funnels tracked
[OK] Analysis saved to: B-brain/clarity-analysis/2026-02-22-clarity-analysis.md
```

---

## 📅 מה שיקרה כל שבוע

כל יום שישי, בעת הרצת:
```bash
python generate_weekly_report.py
```

תקבל דוח שכולל:
1. **GA4** - צפיות עמודים, סשנים, המרות
2. **GSC** - חיפושים אורגניים שמובילים לאתר
3. **Google Ads** - ביצוע הקמפיינים שלך
4. **CLARITY** ← **חדש!** התנהגות משתמש, friction points

הכל בקובץ אחד:
```
B-brain/ads-performance/[תאריך]-weekly-summary.md
```

---

## 🎯 איך להשתמש בנתונים CLARITY

### Friction Point Analysis
```
אם 60% מהמשתמשים נבנו בשלב X, זה בעיה!
→ קרא את ה-heatmap עבור עמוד זה
→ ראה איפה משתמשים קוללקים/מגללים
→ שנה את הטקסט, CTA, או הוצאות העמוד
```

### Ad Copy Optimization
```
אם session recordings מראים שמשתמשים עם ערך engagement גבוה קוללקים על "Prayer at Western Wall"
→ זה איתות שהמילה "Western Wall" כדאי להיות בכל מודעה
→ נסה להוסיף את זה ל-ad headlines
```

### Landing Page Redesign
```
אם heatmaps מראה שמשתמשים לא קוללקים על ה-CTA שלך
→ אולי ה-CTA בצבע שגוי, או בגודל שגוי, או בטקסט גרוע
→ תנסה להעביר את זה או לנסח מחדש
```

---

## 📍 ממציאים של הקבצים החדשים

```
T-tools/scripts/
├── clarity_integration.py          ← סקריפט ראשי לחיבור
├── CLARITY_SETUP.md                ← הוראות הגדרה
└── generate_weekly_report.py       ← עדכן כדי לכלול CLARITY

B-brain/google-auth/
├── clarity-config.json             ← שם יכניסו את API key שלך

B-brain/clarity-analysis/           ← תלכנס כל הדוחות שבועיים
└── [2026-02-22]-clarity-analysis.md
```

---

## 🔒 Privacy & Security

✅ **API key מאובטח** - שמור בתוך `B-brain/google-auth/` (לא נשלח לאיש)
✅ **נתונים מקומיים** - הכל חי על המכונה שלך בלבד
✅ **קריאה בלבד** - הסקריפט רק קורא נתונים, לא משנה כלום
✅ **צפוי להוספה לגיט** - הוסף `clarity-config.json` ל- `.gitignore`

---

## ❓ עיכובים ותרופות

| בעיה | פתרון |
|------|--------|
| "Config file not found" | צור `B-brain/google-auth/clarity-config.json` |
| "Invalid API key" | בדוק שה-API key נכון בקובץ |
| "Project not found" | בדוק שה-project ID נכון |
| "No heatmap data" | Clarity צריך זמן לאסוף נתונים (בדרך כלל 24 שעות) |
| "403 Forbidden" | API key עלול להיות expired - קבל אחד חדש |

---

## 🎯 הצעדים הבאים

1. **זקוף credentials** - עדכן את `clarity-config.json` עם ה-API key שלך
2. **בדוק החיבור** - הרץ `python clarity_integration.py`
3. **הרץ דוח שבועי** - `python generate_weekly_report.py` כל יום שישי
4. **קרא את הדוחות** - בדוק את `B-brain/clarity-analysis/` לתובנות
5. **עדכן מודעות** - השתמש בתובנות כדי לשפר עותקים של מודעות

---

## 📞 שאלות?

קובץ הוראות מלא זמין ב:
```
T-tools/scripts/CLARITY_SETUP.md
```

כל שנבחר - עדכון המערכת הבאה שתגדל היא:
- Google Ads automation (עדכוני הצעות אוטומטיים)
- Bing Ads integration (להרחיב מעבר ל-Google)
- Multi-language ad variants (תמיכה בערבית?)

**כרגע, יש לך מערכת חזקה של נתונים. עכשיו הזמן להשתמש בה כדי לגדול.** 🚀
