#!/usr/bin/env python3
"""
Clean CSV Script - Remove Daily Windup Episodes
Filters out Daily Windup episodes from the podcast CSV file
"""

import csv
import re

def clean_podcast_csv(input_file, output_file):
    """Remove Daily Windup episodes from the CSV file"""
    
    print(f"Reading from: {input_file}")
    
    total_episodes = 0
    kept_episodes = 0
    removed_episodes = 0
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            total_episodes += 1
            
            # Check if this is a Daily Windup episode
            is_daily_windup = False
            
            # Check keywords field
            keywords = row.get('keywords', '').lower()
            if 'thedailywindup' in keywords or 'daily windup' in keywords:
                is_daily_windup = True
            
            # Check title and description for additional Daily Windup references
            title = row.get('title', '').lower()
            description = row.get('description', '').lower()
            
            if ('daily windup' in title or 'daily windup' in description or
                'the daily windup' in title or 'the daily windup' in description):
                is_daily_windup = True
            
            if is_daily_windup:
                removed_episodes += 1
                print(f"Removing: {row.get('title', 'Unknown title')[:50]}...")
            else:
                kept_episodes += 1
                writer.writerow(row)
    
    print(f"\n✅ Cleaning complete!")
    print(f"📊 Summary:")
    print(f"   Total episodes processed: {total_episodes}")
    print(f"   Episodes kept: {kept_episodes}")
    print(f"   Daily Windup episodes removed: {removed_episodes}")
    print(f"   Clean file saved as: {output_file}")
    
    return kept_episodes, removed_episodes

if __name__ == "__main__":
    input_file = "govcon_giants_podcast.csv"
    output_file = "govcon_giants_podcast_clean.csv"
    
    try:
        kept, removed = clean_podcast_csv(input_file, output_file)
        print(f"\n🎉 Your clean podcast CSV is ready!")
        print(f"The new file contains {kept} main podcast episodes.")
        print(f"All {removed} Daily Windup episodes have been removed.")
    except Exception as e:
        print(f"❌ Error: {e}")