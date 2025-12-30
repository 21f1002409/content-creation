# Quick Start Guide

Get your 365-day content plan in 3 minutes!

## Step 1: Choose an Example (1 minute)

Pick the example closest to your content type:

```bash
# Personal Finance Short Videos
cp examples/finance_shorts_example.json my_series.json

# Healthy Cooking Videos
cp examples/cooking_reels_example.json my_series.json

# Productivity Blog Posts
cp examples/productivity_blog_example.json my_series.json

# True Crime Podcast
cp examples/podcast_truecrime_example.json my_series.json
```

## Step 2: Customize (1 minute)

Edit `my_series.json` and replace:
- `[NICHE/TOPIC]` with your specific niche
- Themes with your content pillars
- First 15-50 seed ideas with your actual topics

**Minimum required:**
- Change the niche_topic
- Add at least 5 themes
- Add at least 10 seed ideas

## Step 3: Generate (30 seconds)

```bash
python generate_plan.py --config my_series.json
```

**Done!** You'll get:
- ✅ `my_series_365day_plan.json` - Complete data
- ✅ `my_series_365day_plan.csv` - Import to Excel/Sheets
- ✅ `my_series_365day_plan.md` - Beautiful readable format

## What Next?

### Import to Your Tools

**Google Sheets / Excel:**
1. Open Google Sheets or Excel
2. File → Import → Upload `*_365day_plan.csv`
3. Done! Sort, filter, add notes

**Trello / Asana / Monday:**
1. Create a new project
2. Import the CSV file
3. Each day becomes a card/task

**Notion:**
1. Create a database
2. Import CSV
3. Use calendar view for planning

### Start Creating!

- Pick your first week of content
- Batch film/write similar topics together
- Stay 2-3 weeks ahead in production
- Review and adjust monthly

### Tips for Success

1. **Don't follow blindly** - Use as inspiration, adapt to trends
2. **Batch create** - Film/write multiple pieces in one session
3. **Stay flexible** - Swap days based on trending topics
4. **Track performance** - Note which themes perform best
5. **Engage audience** - Ask for topic suggestions

## Need Help?

- See full README.md for detailed documentation
- Check examples/ folder for more configurations
- Customize the generator for your specific needs

---

**You're all set! Start creating amazing content! 🚀**
