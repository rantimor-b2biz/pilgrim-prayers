# CLARITY Integration Setup Guide

## What is This?

This integration connects your **Paid Search Agent** to Microsoft Clarity data. Every week, the system will pull:
- **Heatmaps** — Where users click and scroll
- **Session recordings** — Engagement patterns
- **Conversion funnels** — Where users drop off

All data is analyzed for **ad copy optimization** and **landing page insights**.

---

## Step 1: Get Your CLARITY Credentials

### From Microsoft Clarity Dashboard:

1. Go to **https://clarity.microsoft.com/**
2. Sign in with your account
3. Select your **Pilgrim Prayers project**
4. Go to **Settings** → **Project settings**
5. Copy your **Project ID** (looks like: `1234567890`)

### Get Your API Key:

1. In Clarity, go to **Settings** → **API & integrations**
2. Look for **API Token** or **Access Token**
3. If you don't see it, request one:
   - Click "Generate new token"
   - Give it a name: "Paid Search Agent"
   - Copy the token (you'll only see it once!)

---

## Step 2: Add Your Credentials

Open this file:
```
B-brain/google-auth/clarity-config.json
```

Replace the values:

**BEFORE:**
```json
{
  "api_key": "YOUR_CLARITY_API_KEY_HERE",
  "project_id": "YOUR_PROJECT_ID_HERE"
}
```

**AFTER (example):**
```json
{
  "api_key": "sk_live_abc123xyz456...",
  "project_id": "1234567890"
}
```

Save the file. **Do not share this file!** It contains your private API key.

---

## Step 3: Test the Integration

Run this command:

```bash
cd "C:\Users\rant\Documents\ran-workspace\Pilgrim Prayers\T-tools\scripts"
python clarity_integration.py
```

**Expected output:**

```
============================================================
[DATA] CLARITY Integration for Paid Search Agent
============================================================

[*] Fetching heatmap data from CLARITY...
[OK] Fetched heatmap data: 5 pages tracked
[*] Fetching session recording insights...
[OK] Fetched 42 top engagement sessions
[*] Fetching conversion funnel analysis...
[OK] Fetched funnel analysis: 3 funnels tracked
[*] Analyzing user behavior patterns...
[OK] Analysis saved to: B-brain/clarity-analysis/2026-02-22-clarity-analysis.md
```

---

## Step 4: Integrate Into Weekly Report

The script is already added to the weekly report generator!

Every Friday, run:

```bash
python generate_weekly_report.py
```

It will now pull:
1. ✅ GA4 data (1045 page views this week)
2. ✅ GSC data (400 organic clicks)
3. ✅ Google Ads data
4. ✅ **CLARITY data (NEW)** — User behavior patterns

All combined into one report: `B-brain/ads-performance/[DATE]-weekly-summary.md`

---

## What Each Data Point Means

### Heatmaps
- **Click count** — How many times users click on elements
- **Scroll depth** — How far down the page users scroll (%)
- **Red/orange areas** — Hot spots where users interact most

**For Ads:** If users are clicking low on the page, your CTA might be in the wrong place!

### Session Recordings
- **Engagement score** — How much user scrolled, clicked, interacted
- **Duration** — How long they stayed
- **Behavior** — What they did (scrolled, clicked, typed, etc.)

**For Ads:** High-engagement sessions show what messaging works!

### Conversion Funnels
- **Steps** — Each stage of your funnel (e.g., Landing → Browse → Pray → Donate)
- **Drop-off %** — What % of users left at each step
- **High drop-off** — Where you're losing people

**For Ads:** If 60% drop off at step 2, your landing page copy might need to change!

---

## Troubleshooting

### Error: "CLARITY config file not found"
**Fix:** Create the config file at:
```
B-brain/google-auth/clarity-config.json
```

### Error: "403 Forbidden" or "Invalid API key"
**Fix:**
1. Check your API key is correct (no extra spaces!)
2. Check the project ID matches
3. Get a new API key from Clarity dashboard
4. Update the config file

### Error: "Project not found"
**Fix:** Make sure the project ID is correct. Get it from Clarity Settings.

### No heatmap data returned
**Possible reasons:**
1. Clarity tracking not installed on your site
2. Not enough user data yet (can take a few hours)
3. Heatmaps are turned off for certain pages

**Check:** Go to Clarity dashboard → make sure heatmaps are enabled for your pages.

---

## What Happens With Your Data?

✅ **Data is stored locally** — Only on your machine in `B-brain/clarity-analysis/`
✅ **Data is private** — Never shared with anyone
✅ **Data is used for** — Analyzing what users do, improving ad copy
✅ **API key is protected** — Keep `clarity-config.json` in `.gitignore` (don't commit it!)

---

## Next Steps

1. ✅ Set up your credentials (see Step 1-2 above)
2. ✅ Test the integration: `python clarity_integration.py`
3. ✅ Run weekly report: `python generate_weekly_report.py`
4. ✅ Read the CLARITY analysis in `B-brain/clarity-analysis/`
5. ✅ Use insights to improve ad copy in Paid Search Agent

---

## Questions?

If you need help:
- **API issues?** Check Microsoft Clarity documentation
- **Python errors?** Make sure Python 3.14+ is installed
- **Feature requests?** Let me know what data you need!

**Remember:** The more data CLARITY has, the better the insights. Give it a week to accumulate behavioral data before expecting deep patterns.
