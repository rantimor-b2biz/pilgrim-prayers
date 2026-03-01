# Agent Scheduler - Complete Guide

## מה זה?

**Agent Scheduler** הוא אוטומציה שמריצה את agents שלך בזמנים קבועים.

ברירת המחדל:
- **Paid Search Agent** — כל יום שישי בשעה 6 בבוקר
- **UX Expert Agent** — כל יום שני בשעה 8 בבוקר

---

## 🚀 איך זה עובד?

### Option 1: אוטומטי (מעבר ל-Windows Scheduler)
תזמן ב-Windows Task Scheduler:
```
Task: Run Pilgrim Prayers Agent Scheduler
Schedule: Every day at 6 AM
Script: python "C:\Users\rant\Documents\ran-workspace\Pilgrim Prayers\T-tools\scripts\agent-scheduler.py" check
```

ה-scheduler יבדוק כל בוקר אם צריך להריץ סוכן. אם זה יום שישי בשעה 6? הוא מריץ את Paid Search.

### Option 2: ידני (עדיף להתחלה)
הרץ את הפקודה ידנית כאשר אתה רוצה:
```bash
python agent-scheduler.py check
```

---

## 📋 פקודות זמינות

### 1. **Check & Run** (בדוק אם צריך להריץ משהו)
```bash
python agent-scheduler.py check
```
**פלט:**
```
[DATA] Agent Scheduler - 2026-02-22 06:00:00
[INFO] paid_search:
       Scheduled: friday at 06:00
       Current: friday at 06:00
[*] RUNNING NOW!
[OK] paid_search: Execution successful
```

### 2. **List** (הצג את לוח הזמנים)
```bash
python agent-scheduler.py list
```
**פלט:**
```
[ON] paid_search
    When: friday at 06:00
    Script: generate_weekly_report.py
    Description: Pull GA4, GSC, Google Ads, and CLARITY data

[ON] ux_expert
    When: monday at 08:00
    Script: ux_expert_analysis.py
    Description: Analyze landing pages and friction points
```

### 3. **Run Now** (הרץ סוכן מסוים עכשיו)
```bash
python agent-scheduler.py run paid_search
python agent-scheduler.py run ux_expert
```

תופעל מיד, בלי לחכות ללוח הזמנים!

### 4. **Log** (ראה היסטוריית ביצועים)
```bash
python agent-scheduler.py log
```
**פלט:**
```
[2026-02-22 06:00:15] paid_search: [OK] - Execution successful
[2026-02-22 08:00:22] ux_expert: [OK] - Execution successful
[2026-02-23 06:01:30] paid_search: [OK] - Execution successful
```

### 5. **Edit** (ערוך את לוח הזמנים)
```bash
python agent-scheduler.py edit
```
עדכן ישירות בקובץ:
```
T-tools/agent-schedule.json
```

---

## ⚙️ איך לשנות את לוח הזמנים

פתח קובץ זה:
```
T-tools/agent-schedule.json
```

**כרגע:**
```json
{
  "paid_search": {
    "enabled": true,
    "day_of_week": "friday",
    "hour": 6,
    "minute": 0,
    "script": "generate_weekly_report.py",
    "description": "..."
  }
}
```

**שנה את:**
- `day_of_week` — יום (monday, tuesday, wednesday, thursday, friday, saturday, sunday)
- `hour` — שעה (0-23)
- `minute` — דקה (0-59)
- `enabled` — true/false

**דוגמה - להריץ ב-Sunday בשעה 19:00:**
```json
{
  "paid_search": {
    "enabled": true,
    "day_of_week": "sunday",
    "hour": 19,
    "minute": 0,
    ...
  }
}
```

---

## 🔧 Setup - Windows Task Scheduler

אם אתה רוצה שזה רץ אוטומטית כל בוקר:

### Step 1: פתח Task Scheduler
```
Windows + R
TaskScheduler
```

### Step 2: צור task חדש
```
Create Basic Task
Name: "Pilgrim Prayers Agent Scheduler"
Trigger: Daily at 6:00 AM
Action: Start a program
Program: C:\Python\python.exe
Arguments: "C:\Users\rant\Documents\ran-workspace\Pilgrim Prayers\T-tools\scripts\agent-scheduler.py" check
```

### Step 3: סיום
Task Scheduler יריץ את הפקודה כל בוקר בשעה 6, והוא יבדוק אם צריך להריץ סוכן.

---

## 📊 Execution Log

כל פעם שסוכן רץ, זה נשמר ב:
```
B-brain/agent-logs/agent-execution.log
```

**דוגמה:**
```
[2026-02-21 08:00:15] ux_expert: [OK] - Execution successful
[2026-02-21 20:34:22] paid_search: [OK] - Execution successful
[2026-02-22 06:00:08] paid_search: [OK] - Execution successful
```

---

## 🎯 תזמון המוקדש שלך

| יום | שעה | סוכן | פעולה |
|-----|------|------|--------|
| **ב' (Monday)** | 08:00 | UX Expert | ניתוח landing pages |
| **ה' (Friday)** | 06:00 | Paid Search | שלוף נתונים, צור דוח |

**למה בזמנים האלה?**
- **יום ב' בבוקר** — UX Expert מעדכן את בעיות העיצוב, עדיין למנהל הדיגיטלי יש זמן לקרוא
- **יום ה' בבוקר** — Paid Search מעדכן את הדוח השבועי, Paid Search Manager קורא אותו בשעות העבודה

---

## 🚨 בעיות ותרופות

| בעיה | פתרון |
|------|--------|
| "Script not found" | בדוק שה-script קיים ב- `T-tools/scripts/` |
| Agent לא רץ בזמן הקבוע | בדוק ש-Task Scheduler פועל, או הרץ ידנית `python agent-scheduler.py check` |
| No execution log | תן לסוכן זמן לרוץ לפחות פעם אחת |
| Python not found | בדוק שיש לך Python 3.14+ מותקן, וב-PATH |

---

## 🔄 Integration עם Agents

### Paid Search Agent (יום שישי בבוקר)
```
[6:00 AM] Scheduler מריץ generate_weekly_report.py
           ↓
[6:05 AM] Pulled: GA4 + GSC + Google Ads + CLARITY data
           ↓
[6:10 AM] Saved: B-brain/ads-performance/[DATE]-weekly-summary.md
           ↓
[Paid Search Manager קורא ביום שישי בשעות העבודה]
```

### UX Expert Agent (יום שני בבוקר)
```
[8:00 AM] Scheduler מריץ ux_expert_analysis.py
           ↓
[8:05 AM] Analyzed: Landing pages, friction points, conversions
           ↓
[8:15 AM] Saved: B-brain/ux-analysis/[DATE]-ux-recommendations.md
           ↓
[UX Expert ו-Paid Search Manager שוקלים שינויים יום ב']
```

---

## 💡 Advanced: On-Demand Triggers

אם אתה צריך להריץ סוכן מיד (לא בלוח הזמנים):

```bash
# Run paid search now
python agent-scheduler.py run paid_search

# Run UX expert now
python agent-scheduler.py run ux_expert
```

מעולה למצבי דחיפות או בדיקות!

---

## 🎓 Next Steps

1. ✅ **Test locally** — `python agent-scheduler.py list`
2. ✅ **Run on demand** — `python agent-scheduler.py run paid_search`
3. ✅ **Set up Windows Task Scheduler** — לאוטומציה מלאה
4. ✅ **Check log** — `python agent-scheduler.py log`

---

## שאלות?

זה מערכת פשוטה ועוצמתית:
- ✅ קל לעדכן (ערוך JSON)
- ✅ קל לראות מה קרה (execution log)
- ✅ קל להריץ ידנית (on-demand)
- ✅ קל להכניס לאוטומציה (Task Scheduler)

**בהצלחה!** 🚀
