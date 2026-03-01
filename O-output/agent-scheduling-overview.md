# Agent Scheduling Overview - System Architecture

## 🏗️ תזמון אוטומטי של Agents

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT SCHEDULER                              │
│              (בודק כל בוקר אם צריך להריץ משהו)                 │
└─────────────────────────────────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐    ┌──────────────────────┐
        │  Is it FRIDAY?       │    │  Is it MONDAY?       │
        │  At 6:00 AM?         │    │  At 8:00 AM?         │
        └──────────────────────┘    └──────────────────────┘
                    │                         │
                   YES                       YES
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐    ┌──────────────────────┐
        │  PAID SEARCH AGENT   │    │  UX EXPERT AGENT     │
        │  ↓                   │    │  ↓                   │
        │  Pull GA4 data       │    │  Analyze landing     │
        │  Pull GSC data       │    │  pages               │
        │  Pull Ads data       │    │  ↓                   │
        │  Pull CLARITY data   │    │  Identify friction   │
        │  ↓                   │    │  ↓                   │
        │  Create weekly       │    │  Create UX           │
        │  summary report      │    │  recommendations     │
        └──────────────────────┘    └──────────────────────┘
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐    ┌──────────────────────┐
        │  B-brain/            │    │  B-brain/            │
        │  ads-performance/    │    │  ux-analysis/        │
        │  [DATE]-weekly-      │    │  [DATE]-ux-          │
        │  summary.md          │    │  recommendations.md  │
        └──────────────────────┘    └──────────────────────┘
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐    ┌──────────────────────┐
        │  PAID SEARCH MANAGER │    │  UX EXPERT & PAID    │
        │  Reads report        │    │  SEARCH MANAGER      │
        │  Updates campaigns   │    │  Reviews & plans     │
        │  Optimizes bids      │    │  landing page changes│
        └──────────────────────┘    └──────────────────────┘
```

---

## 📅 Weekly Rhythm

```
WEEK VIEW:

┌─────────────────────────────────────────────────────────────┐
│ SUNDAY         MONDAY         ...      FRIDAY        SATURDAY │
│               [UX Expert]                [Paid Search]         │
│               @ 8:00 AM                 @ 6:00 AM              │
│                                                                 │
│ UX WORK:       Recommendations ─→─→─→─→ Applied in Pages      │
│                                                                 │
│ PAID SEARCH:   ←─── Data from CLARITY ←───┤ New Report         │
│                ├─→ Ad Copy Variations                           │
│                └─→ Keyword Updates                             │
│                                                                 │
│ HUMAN WORK:    Read UX Recs   ...       Read Paid Search Data  │
│                (Monday)                 (Friday morning)       │
└─────────────────────────────────────────────────────────────┘
```

---

## ⏰ Daily Timeline (כמו שיעבד זה)

### **Sunday Night – Sunday 23:59**
```
Nothing scheduled
User can run agents manually if needed
```

### **Monday 08:00 AM**
```
[TRIGGER] Agent Scheduler checks: Is it Monday at 08:00? YES!
          ↓
[RUN] UX Expert Agent
      ├─ Reads B-brain/clarity-analysis/
      ├─ Analyzes landing page performance
      ├─ Checks conversion funnel data
      ├─ Identifies friction points
      └─ Creates: B-brain/ux-analysis/[DATE]-ux-recommendations.md

[OUTPUT] UX Recommendations saved
         ├─ "Landing page X has 60% drop-off at step Y"
         ├─ "CTA button should be moved above fold"
         ├─ "Form is too long, try 3 fields instead of 7"
         └─ "Mobile experience breaks on iPhone"

[WAIT] Paid Search Manager & UX Expert review during work day
```

### **Monday-Thursday**
```
Paid Search Manager & UX Expert:
- Discuss recommendations
- Make design changes
- Update landing pages
- Plan new ad variations
- Prepare for Friday data pull
```

### **Friday 06:00 AM**
```
[TRIGGER] Agent Scheduler checks: Is it Friday at 06:00? YES!
          ↓
[RUN] Paid Search Agent
      ├─ Runs: python generate_weekly_report.py
      ├─ Pulls: GA4 (1045 page views, 23 conversions)
      ├─ Pulls: GSC (400 organic clicks, top keywords)
      ├─ Pulls: Google Ads (campaign performance)
      ├─ Pulls: CLARITY (heatmaps, session recordings, funnels)
      └─ Creates: B-brain/ads-performance/[DATE]-weekly-summary.md

[OUTPUT] Complete Weekly Report saved
         ├─ All performance metrics
         ├─ Top performing content
         ├─ User behavior patterns
         ├─ Friction points for optimization
         └─ Ready for analysis

[WAIT] Paid Search Manager reviews during work day
       ├─ Analyzes performance trends
       ├─ Identifies winning keywords
       ├─ Plans next week's ad variations
       ├─ Adjusts budgets if needed
       └─ Updates M-memory/learning-log.md with insights
```

### **Friday-Sunday**
```
Planning phase:
- Next week's ad copy
- Keyword expansions
- Landing page optimizations
- Budget adjustments
- Follow-up on UX recommendations

Ready for next week's cycle!
```

---

## 🔧 Manual Overrides (כשצריך להריץ עכשיו)

```
Scenario: You made changes to a landing page on Wednesday
          and want to test UX impact immediately

Command:  python agent-scheduler.py run ux_expert

Result:   UX Expert runs NOW (not waiting for Monday)
          You get immediate feedback on changes
          Compare with previous Monday's report
```

---

## 📊 Configuration

### Current Schedule (Default)

| Agent | Day | Time | Script | Frequency |
|-------|-----|------|--------|-----------|
| **Paid Search** | Friday | 6:00 AM | generate_weekly_report.py | Weekly |
| **UX Expert** | Monday | 8:00 AM | ux_expert_analysis.py | Weekly |

### How to Change

**File:** `T-tools/agent-schedule.json`

```json
{
  "paid_search": {
    "enabled": true,
    "day_of_week": "friday",    ← Change to Monday, Saturday, etc.
    "hour": 6,                   ← Change to 9, 14, 20, etc. (0-23)
    "minute": 0,                 ← Change to 30, 45, etc. (0-59)
    "script": "generate_weekly_report.py"
  },
  "ux_expert": {
    "enabled": true,
    "day_of_week": "monday",
    "hour": 8,
    "minute": 0,
    "script": "ux_expert_analysis.py"
  }
}
```

---

## 🚨 What if I Add More Agents?

Simple! Just add to `agent-schedule.json`:

```json
{
  "paid_search": { ... },
  "ux_expert": { ... },
  "new_agent": {
    "enabled": true,
    "day_of_week": "wednesday",
    "hour": 10,
    "minute": 0,
    "script": "new_agent_script.py"
  }
}
```

Scheduler automatically picks it up!

---

## 🎯 System Benefits

✅ **No manual intervention** — Agents run automatically
✅ **Consistent rhythm** — Same time every week, no surprises
✅ **Async work** — Agents don't block each other
✅ **Audit trail** — See execution log anytime
✅ **Easy to override** — Manual runs when needed
✅ **Scalable** — Add more agents to schedule easily
✅ **Aligned with humans** — Humans read reports during work hours

---

## 💻 Windows Task Scheduler Setup (Optional Automation)

If you want it to run completely unattended:

```
Task: "Pilgrim Prayers Agent Scheduler"
Trigger: Daily at 6:00 AM
Action: Run C:\Python\python.exe
Arguments: "C:\...\T-tools\scripts\agent-scheduler.py" check
```

Then your Agents will run automatically every day without you doing anything!

---

## 🔍 Monitoring

Check execution anytime:

```bash
# What happened this week?
python agent-scheduler.py log

# What's scheduled?
python agent-scheduler.py list

# Run something now (emergency/testing)
python agent-scheduler.py run paid_search
```

---

## 🎓 Summary

| Question | Answer |
|----------|--------|
| **Do agents run automatically?** | Yes, on their set schedule |
| **Can I run them manually?** | Yes, `python agent-scheduler.py run [name]` |
| **What if I miss a scheduled run?** | It's OK - the next run will happen on schedule |
| **Can I add more agents?** | Yes, just update agent-schedule.json |
| **How do I verify they ran?** | Check the execution log |

---

**Your system is now fully automated and ready to work while you sleep!** 😴🚀
