# 365-Day Content Production Plan Generator

A comprehensive tool for creating complete 365-day content production plans for various content formats including YouTube Shorts, TikTok, Instagram Reels, Blog posts, and Podcasts.

## Overview

This tool helps content creators plan an entire year of content by generating structured daily content plans based on configurable themes, hooks, and seed ideas. Perfect for maintaining consistency and ensuring you never run out of content ideas.

## Features

- ✅ Generate 365 days of content ideas
- ✅ Customizable themes and content hooks
- ✅ Multiple export formats (JSON, CSV, Markdown)
- ✅ Support for various content types (videos, blogs, podcasts)
- ✅ Theme rotation and variety
- ✅ Weekly and monthly milestone markers
- ✅ Pre-built example configurations

## Quick Start

### 1. Installation

No installation required! This is a standalone Python script. Just ensure you have Python 3.6+ installed:

```bash
python --version
```

### 2. Create Your Configuration

Copy the template and customize it for your series:

```bash
cp config_template.json my_series.json
```

Edit `my_series.json` with your series details:
- Niche/Topic
- Format (YouTube Shorts, Blog, Podcast, etc.)
- Duration/Length
- Style
- Target Audience
- Content Themes
- Content Hooks
- Seed Ideas (first 30-50 days)

### 3. Generate Your Plan

```bash
python generate_plan.py --config my_series.json
```

This will create three files:
- `my_series_365day_plan.json` - Complete plan in JSON format
- `my_series_365day_plan.csv` - Spreadsheet-friendly format
- `my_series_365day_plan.md` - Human-readable markdown format

## Usage Examples

### Basic Usage

```bash
# Generate plan with all output formats
python generate_plan.py --config examples/finance_shorts_example.json

# Generate only JSON format
python generate_plan.py --config my_series.json --format json

# Specify custom start date
python generate_plan.py --config my_series.json --start-date 2025-01-01

# Custom output filename
python generate_plan.py --config my_series.json --output my_custom_plan
```

### Available Options

- `--config` (required): Path to your configuration JSON file
- `--start-date` (optional): Start date in YYYY-MM-DD format (defaults to today)
- `--format` (optional): Output format - `json`, `csv`, `markdown`, or `all` (default: all)
- `--output` (optional): Custom output filename base (without extension)

## Example Configurations

The `examples/` directory contains ready-to-use configurations:

### 1. Personal Finance (YouTube Shorts/TikTok)
```bash
python generate_plan.py --config examples/finance_shorts_example.json
```
- **Format**: 60-second videos
- **Style**: Educational with comedic elements
- **Themes**: Budgeting, Investing, Debt Management, Side Hustles

### 2. Healthy Recipes (Instagram Reels)
```bash
python generate_plan.py --config examples/cooking_reels_example.json
```
- **Format**: 30-45 second videos
- **Style**: Fast-paced, visually appealing
- **Themes**: Quick meals, Meal prep, Healthy desserts

### 3. Productivity Blog Posts
```bash
python generate_plan.py --config examples/productivity_blog_example.json
```
- **Format**: 1200-1500 word articles
- **Style**: Conversational yet authoritative
- **Themes**: Time management, Morning routines, Goal setting

### 4. True Crime Podcast
```bash
python generate_plan.py --config examples/podcast_truecrime_example.json
```
- **Format**: 30-45 minute episodes
- **Style**: Narrative storytelling
- **Themes**: Unsolved mysteries, Cold cases, Forensics

## Configuration Guide

### Series Overview
Define the basic parameters of your content series:
```json
"series_overview": {
  "niche_topic": "Your specific niche",
  "format": "Platform and content type",
  "duration_length": "How long each piece is",
  "style": "Tone and approach",
  "target_audience": "Who you're creating for",
  "publishing_schedule": "Daily for 365 days"
}
```

### Content Themes
List 5-10 recurring themes that will rotate throughout the year:
```json
"content_themes": [
  "Theme 1",
  "Theme 2",
  "Theme 3"
]
```

### Content Hooks
Engaging formats or angles for your content (10-15 recommended):
```json
"content_hooks": [
  "Top 5",
  "How to",
  "Common mistakes",
  "Behind the scenes"
]
```

### Seed Ideas
Pre-written topics for the first 30-50 days to ensure strong starts:
```json
"seed_ideas": [
  "Day 1: Introduction to [topic]",
  "Day 2: Why [topic] matters"
]
```

## Output Formats

### JSON Format
Complete structured data including all metadata:
- Easy to parse programmatically
- Includes series overview
- Full daily content details

### CSV Format
Spreadsheet-compatible format:
- Import into Excel, Google Sheets
- Easy filtering and sorting
- Perfect for project management tools

### Markdown Format
Human-readable format:
- Beautiful formatting
- Organized by month
- Easy to review and share

## Best Practices

### Planning Your Series

1. **Start with Seed Ideas**: Plan the first 30-50 days in detail
2. **Use Theme Variety**: 7 themes works well (one per day of week)
3. **Mix Content Hooks**: Rotate between educational, entertaining, and inspirational
4. **Consider Milestones**: The generator marks weekly (day 7, 14, etc.) and monthly (day 30, 60, etc.) milestones
5. **Stay Flexible**: Use the plan as a guide, but adapt based on trends and audience feedback

### Content Strategy

- **Batch Production**: Group similar content types together
- **Evergreen Content**: Focus on topics that remain relevant
- **Trending Topics**: Leave room for timely content
- **Audience Engagement**: Incorporate feedback and requests
- **Analytics Review**: Adjust themes based on performance

## Customization Tips

### Adding More Variety

1. **Expand Seed Ideas**: The more seed ideas you provide (up to 100+), the more unique your first quarter will be
2. **Increase Theme Count**: More themes = more variety in rotation
3. **Diverse Hooks**: Mix question formats, list formats, and narrative formats
4. **Sub-themes**: Consider creating variations within themes

### Adapting for Different Platforms

**Short-Form Video (TikTok, Shorts, Reels)**
- Focus on hooks in first 3 seconds
- Keep topics single-focused
- Use trending audio/formats

**Blog Posts**
- Expand on "how-to" and "guide" formats
- Include detailed step-by-step content
- Optimize for SEO keywords

**Podcasts**
- Plan for longer narrative arcs
- Schedule interview episodes
- Build series within the series

## Workflow Integration

### With Project Management Tools

Import CSV into:
- Trello (using CSV import)
- Asana (using CSV import)
- Monday.com (using CSV import)
- Notion (using database import)

### With Content Calendars

The output includes:
- Dates and day of week
- Themes for color-coding
- Notes for special days

### With Analytics

Track performance by:
- Theme (which themes perform best)
- Content hook (which formats resonate)
- Day of week (when audience is most active)

## FAQ

**Q: Do I need to follow the plan exactly?**
A: No! Use it as a flexible guide. Adapt based on trends, feedback, and inspiration.

**Q: Can I generate multiple plans?**
A: Yes! Create different config files for different content series.

**Q: What if I want to change my plan mid-year?**
A: Generate a new plan starting from your current date, or manually edit the exported files.

**Q: Can I use this for multiple platforms?**
A: Absolutely! Generate a plan for each platform or repurpose one plan across platforms.

**Q: How do I handle holidays or special events?**
A: Manually edit specific days in the exported CSV or JSON file, or use the notes field.

## Contributing

This is a simple tool designed to be easily customizable. Feel free to:
- Modify the generator logic
- Add new output formats
- Create additional example configurations
- Share your configurations with the community

## License

Free to use for personal and commercial content creation.

## Support

For issues or questions, please open an issue on the repository.

---

**Happy Creating! 🎥📝🎙️**

Start planning your content empire today and never run out of ideas again!