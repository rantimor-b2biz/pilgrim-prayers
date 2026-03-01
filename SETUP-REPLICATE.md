# הגדרת Replicate לפרויקט Pilgrim

## שלב 1: התקנת Python

1. הורד Python מ: **https://www.python.org/downloads/**
2. **חשוב מאוד**: בזמן ההתקנה, סמן ✅ **"Add Python to PATH"**
3. אחרי ההתקנה, פתח טרמינל חדש ובדוק:
   ```bash
   python --version
   ```

## שלב 2: התקנת Replicate

```bash
pip install replicate
```

## שלב 3: קבלת API Token

1. היכנס ל: https://replicate.com/account/api-tokens
2. צור טוקן חדש או העתק את הטוקן הקיים (מתחיל ב-`r8_`)

## שלב 4: הגדרת API Token

צור קובץ `.env` בתיקיית הראשית של Pilgrim:

**מיקום**: `C:\Users\rant\Documents\ran-workspace\Pilgrim\.env`

**תוכן**:
```
REPLICATE_API_TOKEN=r8_your_token_here
```

החלף את `r8_your_token_here` בטוקן האמיתי שלך.

## שלב 5: שימוש בסקריפט

### בדיקת סטטוס הפרויקטים
```bash
cd C:\Users\rant\Documents\ran-workspace\Pilgrim
python T-tools\scripts\generate-replicate.py --list
```

### יצירת תמונות לפרויקט בודד
```bash
python T-tools\scripts\generate-replicate.py 02-weekly-post-galilee-living-land
```

### יצירת תמונות לכל הפרויקטים
```bash
python T-tools\scripts\generate-replicate.py --all
```

### יצירת תמונות + וידאו
```bash
python T-tools\scripts\generate-replicate.py 02-weekly-post-galilee-living-land --video
```

### אופציות נוספות
```bash
# שימוש במודל מהיר וזול יותר (Flux Schnell)
python T-tools\scripts\generate-replicate.py --all --schnell

# יצירה מחדש גם אם קבצים כבר קיימים
python T-tools\scripts\generate-replicate.py --all --force

# הכל ביחד
python T-tools\scripts\generate-replicate.py --all --video --schnell
```

## מה הסקריפט עושה

הסקריפט קורא את קובץ `visual-brief.md` בכל פרויקט ו:

1. **מזהה תמונות**: מחפש כל כותרת `## Hero Image`, `## Inline Image 1`, וכו'
2. **מוציא Prompts**: מחלץ את ה-AI prompts מתוך code blocks
3. **יוצר תמונות**: שולח את ה-prompts ל-Replicate API
4. **שומר תמונות**: שומר בתיקיית `images/` של הפרויקט

### דוגמה למבנה
```
O-output/
  └── 02-weekly-post-galilee-living-land/
      ├── visual-brief.md          # קובץ הקלט
      ├── images/                   # תיקיית הפלט
      │   ├── hero.png
      │   ├── inline-1.png
      │   ├── inline-2.png
      │   └── newsletter-header.png
      └── videos/                   # אם השתמשת ב --video
          └── post-video.mp4
```

## פתרון בעיות

### Python לא מוכר
- וודא שהוספת Python ל-PATH בהתקנה
- נסה לפתוח טרמינל חדש
- נסה להריץ: `py` במקום `python`

### שגיאת API Token
```
ERROR: REPLICATE_API_TOKEN not found.
```
- בדוק שהקובץ `.env` נמצא בתיקיית Pilgrim
- בדוק שהטוקן נכתב נכון (מתחיל ב-`r8_`)

### אין visual-brief.md
```
ERROR: Could not find visual-brief.md
```
- הסקריפט עובד רק עם פרויקטים שיש להם `visual-brief.md`
- צור את הקובץ או בחר פרויקט אחר

## מודלים זמינים

### תמונות
- **Flux 1.1 Pro** (ברירת מחדל): איכות גבוהה, יקר יותר
- **Flux Schnell** (עם `--schnell`): מהיר וזול, איכות טובה

### וידאו
- **Hailuo-02** (ברירת מחדל): 6 שניות, איכות גבוהה

## עלויות משוערות

- תמונה אחת (Flux Pro): ~$0.04
- תמונה אחת (Flux Schnell): ~$0.003
- וידאו 6 שניות: ~$0.10

לפרויקט עם 4 תמונות + וידאו: ~$0.26 (Pro) או ~$0.11 (Schnell)

## מה הלאה?

1. התקן Python
2. התקן Replicate
3. הגדר API Token
4. הרץ: `python T-tools\scripts\generate-replicate.py --list`
5. בחר פרויקט: `python T-tools\scripts\generate-replicate.py 02-weekly-post-galilee-living-land`

---

**זקוק לעזרה?** בדוק את ה-README של הסקריפט:
```bash
python T-tools\scripts\generate-replicate.py
```
