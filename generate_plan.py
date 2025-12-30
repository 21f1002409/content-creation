#!/usr/bin/env python3
"""
365-Day Content Production Plan Generator

This script generates a complete 365-day content production plan based on
a configuration file specifying the series details.
"""

import json
import csv
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Any
import os


class ContentPlanGenerator:
    """Generate 365-day content production plans."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize with configuration."""
        self.config = config
        self.series_overview = config.get('series_overview', {})
        self.content_themes = config.get('content_themes', [])
        self.content_hooks = config.get('content_hooks', [])
        self.seed_ideas = config.get('seed_ideas', [])
        
    def generate_daily_content(self, day_number: int, date: datetime) -> Dict[str, Any]:
        """Generate content plan for a specific day."""
        # Cycle through themes
        if self.content_themes:
            theme_index = (day_number - 1) % len(self.content_themes)
            theme = self.content_themes[theme_index]
        else:
            theme = "General"
        
        # Generate title/topic based on seed ideas and day
        # Note: day_number is 1-based (starts at 1, not 0)
        if self.seed_ideas and day_number <= len(self.seed_ideas):
            topic = self.seed_ideas[day_number - 1]  # Convert to 0-based index
        else:
            # Generate based on theme and hooks
            if self.content_hooks:
                hook = self.content_hooks[(day_number - 1) % len(self.content_hooks)]
            else:
                hook = ""
            topic = f"{hook} {theme}".strip()
        
        content = {
            'day': day_number,
            'date': date.strftime('%Y-%m-%d'),
            'day_of_week': date.strftime('%A'),
            'theme': theme,
            'topic': topic,
            'format': self.series_overview.get('format', ''),
            'duration_length': self.series_overview.get('duration_length', ''),
            'style': self.series_overview.get('style', ''),
            'target_audience': self.series_overview.get('target_audience', ''),
        }
        
        # Add optional production notes (check monthly first as it's more specific)
        # Note: Using 30-day cycles (not calendar months) for consistent production milestones
        if day_number % 30 == 0:
            content['notes'] = 'Monthly milestone - consider special content'
        elif day_number % 7 == 0:
            content['notes'] = 'Weekly recap/review day'
        else:
            content['notes'] = ''
            
        return content
    
    def generate_365_plan(self, start_date: str = None) -> List[Dict[str, Any]]:
        """Generate complete 365-day plan."""
        if start_date:
            current_date = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            current_date = datetime.now()
        
        plan = []
        for day in range(1, 366):
            daily_content = self.generate_daily_content(day, current_date)
            plan.append(daily_content)
            current_date += timedelta(days=1)
        
        return plan
    
    def export_to_json(self, plan: List[Dict[str, Any]], output_file: str):
        """Export plan to JSON file."""
        output_data = {
            'series_overview': self.series_overview,
            'total_days': len(plan),
            'content_plan': plan
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ JSON plan exported to: {output_file}")
    
    def export_to_csv(self, plan: List[Dict[str, Any]], output_file: str):
        """Export plan to CSV file."""
        if not plan:
            return
        
        fieldnames = list(plan[0].keys())
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(plan)
        
        print(f"✓ CSV plan exported to: {output_file}")
    
    def export_to_markdown(self, plan: List[Dict[str, Any]], output_file: str):
        """Export plan to Markdown file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# 365-Day Content Production Plan\n\n")
            f.write(f"## Series Overview\n\n")
            for key, value in self.series_overview.items():
                f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
            f.write(f"\n---\n\n")
            
            # Write daily content
            current_month = None
            for item in plan:
                # Add month header
                month = datetime.strptime(item['date'], '%Y-%m-%d').strftime('%B %Y')
                if month != current_month:
                    f.write(f"\n## {month}\n\n")
                    current_month = month
                
                f.write(f"### Day {item['day']} - {item['date']} ({item['day_of_week']})\n\n")
                f.write(f"- **Theme**: {item['theme']}\n")
                f.write(f"- **Topic**: {item['topic']}\n")
                f.write(f"- **Format**: {item['format']}\n")
                if item.get('notes'):
                    f.write(f"- **Notes**: {item['notes']}\n")
                f.write(f"\n")
        
        print(f"✓ Markdown plan exported to: {output_file}")


def load_config(config_file: str) -> Dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {e}")
        exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate a 365-day content production plan',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_plan.py --config my_series.json
  python generate_plan.py --config my_series.json --start-date 2025-01-01
  python generate_plan.py --config my_series.json --format json --output my_plan.json
  python generate_plan.py --config my_series.json --format all
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='Path to configuration JSON file'
    )
    
    parser.add_argument(
        '--start-date',
        type=str,
        help='Start date for the plan (YYYY-MM-DD format). Defaults to today.'
    )
    
    parser.add_argument(
        '--format',
        type=str,
        choices=['json', 'csv', 'markdown', 'all'],
        default='all',
        help='Output format (default: all)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (extension will be added based on format)'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    print(f"Loading configuration from: {args.config}")
    config = load_config(args.config)
    
    # Generate plan
    print("Generating 365-day content plan...")
    generator = ContentPlanGenerator(config)
    plan = generator.generate_365_plan(start_date=args.start_date)
    print(f"✓ Generated {len(plan)} days of content")
    
    # Determine output file base name
    if args.output:
        output_base = args.output.rsplit('.', 1)[0]
    else:
        config_name = os.path.basename(args.config).rsplit('.', 1)[0]
        output_base = f"{config_name}_365day_plan"
    
    # Export to specified format(s)
    if args.format in ['json', 'all']:
        generator.export_to_json(plan, f"{output_base}.json")
    
    if args.format in ['csv', 'all']:
        generator.export_to_csv(plan, f"{output_base}.csv")
    
    if args.format in ['markdown', 'all']:
        generator.export_to_markdown(plan, f"{output_base}.md")
    
    print(f"\n✓ Content production plan complete!")


if __name__ == '__main__':
    main()
