#!/usr/bin/env python3
"""
RSS Feed to CSV Parser for Podcast Data
Converts Govcon Giants podcast RSS feed to CSV format for Framer website import
"""

import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import csv
import re
from urllib.parse import unquote
from datetime import datetime
import html

def clean_text(text):
    """Clean and format text content"""
    if not text:
        return ""
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove extra whitespace and normalize
    text = ' '.join(text.split())
    
    # Remove CDATA markers if present
    text = text.replace('<![CDATA[', '').replace(']]>', '')
    
    return text.strip()

def parse_duration(duration_str):
    """Convert duration string to minutes"""
    if not duration_str:
        return ""
    
    try:
        parts = duration_str.split(':')
        if len(parts) == 3:  # HH:MM:SS
            hours, minutes, seconds = map(int, parts)
            return hours * 60 + minutes + (1 if seconds > 30 else 0)  # Round up if > 30 seconds
        elif len(parts) == 2:  # MM:SS
            minutes, seconds = map(int, parts)
            return minutes + (1 if seconds > 30 else 0)
        else:
            return duration_str
    except:
        return duration_str

def format_date(date_str):
    """Convert RSS date to readable format"""
    if not date_str:
        return ""
    
    try:
        # Parse RSS date format: "Tue, 15 Jul 2025 10:00:00 +0000"
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%Y-%m-%d")
    except:
        return date_str

def extract_episode_number(title, itunes_episode):
    """Extract episode number from title or iTunes episode field"""
    if itunes_episode:
        return itunes_episode
    
    # Try to extract from title
    match = re.search(r'^(\d+)[:\-\s]', title)
    if match:
        return match.group(1)
    
    return ""

def parse_rss_to_csv(rss_url, output_file):
    """Parse RSS feed and convert to CSV"""
    
    print(f"Fetching RSS feed from: {rss_url}")
    
    # Fetch the RSS feed
    try:
        with urllib.request.urlopen(rss_url) as response:
            content = response.read()
    except urllib.error.URLError as e:
        print(f"Error fetching RSS feed: {e}")
        return False
    
    # Parse XML
    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return False
    
    # Find the channel
    channel = root.find('channel')
    if channel is None:
        print("No channel found in RSS feed")
        return False
    
    # Extract podcast metadata
    podcast_title = clean_text(channel.find('title').text if channel.find('title') is not None else "")
    podcast_description = clean_text(channel.find('description').text if channel.find('description') is not None else "")
    podcast_author = clean_text(channel.find('.//itunes:author', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if channel.find('.//itunes:author', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "")
    
    print(f"Parsing podcast: {podcast_title}")
    print(f"Author: {podcast_author}")
    
    # Prepare CSV data
    episodes = []
    
    # Find all items (episodes)
    items = channel.findall('item')
    print(f"Found {len(items)} episodes")
    
    for item in items:
        # Extract episode data
        title = clean_text(item.find('title').text if item.find('title') is not None else "")
        itunes_title = clean_text(item.find('.//itunes:title', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:title', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "")
        
        # Use iTunes title if available, otherwise regular title
        episode_title = itunes_title if itunes_title else title
        
        description = clean_text(item.find('description').text if item.find('description') is not None else "")
        content_encoded = clean_text(item.find('.//content:encoded', {'content': 'http://purl.org/rss/1.0/modules/content/'}).text if item.find('.//content:encoded', {'content': 'http://purl.org/rss/1.0/modules/content/'}) is not None else "")
        
        # Use content:encoded if available and longer, otherwise use description
        episode_description = content_encoded if len(content_encoded) > len(description) else description
        
        pub_date = format_date(item.find('pubDate').text if item.find('pubDate') is not None else "")
        
        # Audio file information
        enclosure = item.find('enclosure')
        audio_url = enclosure.get('url') if enclosure is not None else ""
        audio_length = enclosure.get('length') if enclosure is not None else ""
        audio_type = enclosure.get('type') if enclosure is not None else ""
        
        # iTunes specific fields
        duration = parse_duration(item.find('.//itunes:duration', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:duration', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "")
        
        episode_num = extract_episode_number(
            episode_title,
            item.find('.//itunes:episode', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:episode', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else ""
        )
        
        season = item.find('.//itunes:season', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:season', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "1"
        
        subtitle = clean_text(item.find('.//itunes:subtitle', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:subtitle', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "")
        
        keywords = clean_text(item.find('.//itunes:keywords', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:keywords', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else "")
        
        author = clean_text(item.find('.//itunes:author', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}).text if item.find('.//itunes:author', {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}) is not None else podcast_author)
        
        episode_url = clean_text(item.find('link').text if item.find('link') is not None else "")
        guid = clean_text(item.find('guid').text if item.find('guid') is not None else "")
        
        # Create episode record
        episode = {
            'episode_number': episode_num,
            'season': season,
            'title': episode_title,
            'subtitle': subtitle,
            'description': episode_description,
            'author': author,
            'publication_date': pub_date,
            'duration_minutes': duration,
            'audio_url': audio_url,
            'audio_file_size': audio_length,
            'audio_type': audio_type,
            'episode_url': episode_url,
            'keywords': keywords,
            'guid': guid
        }
        
        episodes.append(episode)
    
    # Sort episodes by episode number (if available) or by date
    episodes.sort(key=lambda x: (int(x['episode_number']) if x['episode_number'].isdigit() else 999, x['publication_date']), reverse=True)
    
    # Write to CSV
    if episodes:
        fieldnames = [
            'episode_number',
            'season', 
            'title',
            'subtitle',
            'description',
            'author',
            'publication_date',
            'duration_minutes',
            'audio_url',
            'audio_file_size',
            'audio_type',
            'episode_url',
            'keywords',
            'guid'
        ]
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(episodes)
        
        print(f"Successfully converted {len(episodes)} episodes to {output_file}")
        return True
    else:
        print("No episodes found to convert")
        return False

if __name__ == "__main__":
    rss_url = "https://feeds.libsyn.com/179924/rss"
    output_file = "govcon_giants_podcast.csv"
    
    success = parse_rss_to_csv(rss_url, output_file)
    
    if success:
        print(f"\n✅ Conversion complete! Your podcast data is now in '{output_file}'")
        print("\nColumns included:")
        print("- episode_number: Episode number")
        print("- season: Season number")
        print("- title: Episode title")
        print("- subtitle: Episode subtitle")
        print("- description: Full episode description")
        print("- author: Episode author")
        print("- publication_date: Published date (YYYY-MM-DD)")
        print("- duration_minutes: Duration in minutes")
        print("- audio_url: Direct link to audio file")
        print("- audio_file_size: Audio file size in bytes")
        print("- audio_type: Audio file MIME type")
        print("- episode_url: Episode page URL")
        print("- keywords: Episode keywords/tags")
        print("- guid: Unique episode identifier")
        print(f"\nThis CSV file is ready to import into your Framer website!")
    else:
        print("❌ Conversion failed")