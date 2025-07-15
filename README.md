# Govcon Giants Podcast RSS to CSV Conversion

## Summary
Successfully converted your Govcon Giants podcast RSS feed to CSV format for import into your Framer website.

## Files Generated
- **`govcon_giants_podcast.csv`** - Main CSV file with all episode data (900KB, 507 rows including header)
- **`rss_to_csv_parser.py`** - Python script used for conversion (reusable for future updates)

## Source Data
- **RSS Feed URL:** https://feeds.libsyn.com/179924/rss
- **Podcast:** Govcon Giants
- **Host:** Eric Coffie
- **Total Episodes:** 506 episodes converted

## CSV Structure
The generated CSV contains 14 columns with comprehensive episode data:

| Column | Description |
|--------|-------------|
| `episode_number` | Episode number |
| `season` | Season number |
| `title` | Episode title |
| `subtitle` | Episode subtitle |
| `description` | Full episode description (cleaned HTML) |
| `author` | Episode author |
| `publication_date` | Published date (YYYY-MM-DD format) |
| `duration_minutes` | Duration in minutes |
| `audio_url` | Direct link to audio file |
| `audio_file_size` | Audio file size in bytes |
| `audio_type` | Audio file MIME type (audio/mpeg) |
| `episode_url` | Episode page URL |
| `keywords` | Episode keywords/tags |
| `guid` | Unique episode identifier |

## Data Processing Features
The conversion script includes:
- ✅ HTML tag removal and text cleaning
- ✅ Date format standardization (YYYY-MM-DD)
- ✅ Duration conversion to minutes
- ✅ Episode number extraction from titles
- ✅ UTF-8 encoding for special characters
- ✅ Proper CSV escaping for commas in content

## Sample Data
Here's what the first few episodes look like:

**Latest Episode:** "STOP Bidding on Everything! This Rookie Move Will Destroy Your Government Contract Strategy"
- Published: 2025-07-15
- Duration: 8 minutes
- Author: Eric Coffie

## Using with Framer
Your CSV file is now ready to import into Framer:
1. Open your Framer project
2. Go to CMS Collections
3. Import the `govcon_giants_podcast.csv` file
4. Map the columns to your desired content fields
5. Use the data to build your podcast pages dynamically

## Future Updates
To update your podcast data in the future:
1. Run the script again: `python3 rss_to_csv_parser.py`
2. Re-import the updated CSV into Framer
3. Your website will automatically reflect the latest episodes

## Technical Notes
- The script uses Python's standard library (no external dependencies required)
- Episodes are sorted by episode number and date (newest first)
- All text content is cleaned and properly escaped for CSV format
- Audio URLs point directly to MP3 files hosted on Libsyn

Your podcast data is now ready for your Framer website! 🎉