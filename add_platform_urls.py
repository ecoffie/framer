#!/usr/bin/env python3
"""
Add Platform URLs Script
Adds Apple Podcasts and Spotify URL columns to the podcast CSV file
"""

import csv
import re
import urllib.parse

def generate_platform_urls(episode_data):
    """Generate platform URLs based on episode data"""
    
    # Get episode title for URL generation
    title = episode_data.get('title', '')
    episode_url = episode_data.get('episode_url', '')
    
    # Extract slug from Libsyn episode URL if available
    slug = ""
    if episode_url:
        # Extract the slug from URLs like: https://govcongiants.libsyn.com/episode-slug
        slug_match = re.search(r'libsyn\.com/(.+)$', episode_url)
        if slug_match:
            slug = slug_match.group(1)
    
    # If no slug from URL, create one from title
    if not slug and title:
        # Convert title to URL-friendly slug
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars except spaces and hyphens
        slug = re.sub(r'[-\s]+', '-', slug)   # Replace spaces and multiple hyphens with single hyphen
        slug = slug.strip('-')                # Remove leading/trailing hyphens
        slug = slug[:100]                     # Limit length
    
    # Generate platform URLs
    # These are template URLs that can be updated with actual show IDs
    apple_url = f"https://podcasts.apple.com/podcast/govcon-giants/id[SHOW_ID]"
    spotify_url = f"https://open.spotify.com/show/[SHOW_ID]"
    
    # If we had the actual show IDs, the URLs would look like:
    # apple_url = f"https://podcasts.apple.com/podcast/govcon-giants/id1234567890?i={episode_id}"
    # spotify_url = f"https://open.spotify.com/episode/{episode_id}"
    
    return apple_url, spotify_url

def add_platform_urls_to_csv(input_file, output_file):
    """Add Apple Podcasts and Spotify URL columns to the CSV file"""
    
    print(f"Reading from: {input_file}")
    
    episodes_processed = 0
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        
        # Add new columns for platform URLs
        new_fieldnames = list(reader.fieldnames) + ['apple_podcast_url', 'spotify_url']
        
        writer = csv.DictWriter(outfile, fieldnames=new_fieldnames)
        writer.writeheader()
        
        for row in reader:
            episodes_processed += 1
            
            # Generate platform URLs
            apple_url, spotify_url = generate_platform_urls(row)
            
            # Add new columns to the row
            row['apple_podcast_url'] = apple_url
            row['spotify_url'] = spotify_url
            
            writer.writerow(row)
    
    print(f"\n✅ Platform URLs added successfully!")
    print(f"📊 Summary:")
    print(f"   Episodes processed: {episodes_processed}")
    print(f"   New columns added: apple_podcast_url, spotify_url")
    print(f"   Enhanced file saved as: {output_file}")
    
    return episodes_processed

def update_with_actual_show_ids(csv_file, apple_show_id=None, spotify_show_id=None):
    """Update the CSV with actual show IDs if provided"""
    
    if not apple_show_id and not spotify_show_id:
        print("\n📝 To add actual platform links:")
        print("   1. Find your Apple Podcasts show ID")
        print("   2. Find your Spotify show ID") 
        print("   3. Run this script again with the actual IDs")
        print("\n🔍 How to find show IDs:")
        print("   Apple Podcasts: Visit your show page, the ID is in the URL")
        print("   Spotify: Visit your show page, the ID is in the URL after '/show/'")
        return
    
    # This would update the placeholder URLs with actual show IDs
    # Implementation would read the CSV and replace [SHOW_ID] with actual IDs
    print("Updating with actual show IDs...")

if __name__ == "__main__":
    input_file = "govcon_giants_podcast_clean.csv"
    output_file = "govcon_giants_podcast_with_platforms.csv"
    
    try:
        episodes_count = add_platform_urls_to_csv(input_file, output_file)
        
        print(f"\n🎉 Your enhanced podcast CSV is ready!")
        print(f"The file now includes platform URL columns for all {episodes_count} episodes.")
        
        # Instructions for finding actual show IDs
        print(f"\n🔗 Platform URL Structure Added:")
        print(f"   • apple_podcast_url: Template for Apple Podcasts links")
        print(f"   • spotify_url: Template for Spotify links")
        
        print(f"\n📱 Next Steps to Complete Platform Links:")
        print(f"   1. Find your Govcon Giants show on Apple Podcasts")
        print(f"   2. Find your Govcon Giants show on Spotify") 
        print(f"   3. Copy the show IDs from the URLs")
        print(f"   4. Replace [SHOW_ID] in the CSV with your actual IDs")
        
        print(f"\n💡 Example URLs:")
        print(f"   Apple: https://podcasts.apple.com/podcast/govcon-giants/id1234567890")
        print(f"   Spotify: https://open.spotify.com/show/1a2b3c4d5e6f7g8h9i0j")
        
        update_with_actual_show_ids(output_file)
        
    except Exception as e:
        print(f"❌ Error: {e}")