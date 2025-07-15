# Govcon Giants Podcast RSS to CSV Conversion

## Summary
Successfully converted your Govcon Giants podcast RSS feed to CSV format for import into your Framer website.

## Files Generated
- **`govcon_giants_podcast_with_platforms.csv`** - **🔥 FINAL FILE** - Enhanced CSV with Apple Podcasts and Spotify URLs (693KB, 341 episodes)
- **`govcon_giants_podcast_clean.csv`** - Clean CSV file with main podcast episodes only (660KB, 342 rows including header)
- **`govcon_giants_podcast.csv`** - Original CSV file with all episodes including Daily Windup (900KB, 507 rows including header)
- **`rss_to_csv_parser.py`** - Python script used for RSS conversion (reusable for future updates)
- **`clean_csv.py`** - Python script used to remove Daily Windup episodes
- **`add_platform_urls.py`** - Python script used to add Apple Podcasts and Spotify URL columns

## Source Data
- **RSS Feed URL:** https://feeds.libsyn.com/179924/rss
- **Podcast:** Govcon Giants
- **Host:** Eric Coffie
- **Total Episodes:** 506 episodes converted (341 main episodes + 165 Daily Windup episodes removed)

## CSV Structure
The enhanced CSV contains 16 columns with comprehensive episode data and platform URLs:

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
| `apple_podcast_url` | Apple Podcasts URL template |
| `spotify_url` | Spotify URL template |

## Data Processing Features
The conversion and cleaning scripts include:
- ✅ HTML tag removal and text cleaning
- ✅ Date format standardization (YYYY-MM-DD)
- ✅ Duration conversion to minutes
- ✅ Episode number extraction from titles
- ✅ UTF-8 encoding for special characters
- ✅ Proper CSV escaping for commas in content
- ✅ **Daily Windup episode filtering** (165 episodes removed from clean version)
- ✅ **Apple Podcasts and Spotify URL columns** (ready for platform integration)

## Sample Data
Here's what the clean episodes look like (Daily Windup episodes removed):

**Latest Main Episode:** "$4 BILLION Under Management?! How I Got Access to the Top Private Equity Investors!"
- Published: 2025-03-13
- Duration: 6 minutes
- Author: Eric Coffie

**Recent Episode:** "$100,000 Business Funding Approved? Here's What You're Missing!"
- Published: 2025-01-25
- Duration: 10 minutes
- Author: Eric Coffie

## Using with Framer
Your enhanced CSV file is now ready to import into Framer:
1. Open your Framer project
2. Go to CMS Collections
3. **Import the `govcon_giants_podcast_with_platforms.csv` file** (🔥 RECOMMENDED - includes Apple Podcasts & Spotify URLs)
4. Map the columns to your desired content fields
5. Use the data to build dynamic podcast pages with platform links

**Platform URLs:** The CSV includes template URLs for Apple Podcasts and Spotify. To complete the setup:
- Find your show's Apple Podcasts ID and replace `[SHOW_ID]` in the apple_podcast_url column
- Find your show's Spotify ID and replace `[SHOW_ID]` in the spotify_url column

## Future Updates
To update your podcast data in the future:
1. Run the RSS parser: `python3 rss_to_csv_parser.py`
2. Clean the data: `python3 clean_csv.py` (removes Daily Windup episodes)
3. Add platform URLs: `python3 add_platform_urls.py`
4. Re-import the updated `govcon_giants_podcast_with_platforms.csv` into Framer
5. Your website will automatically reflect the latest episodes

## Technical Notes
- The script uses Python's standard library (no external dependencies required)
- Episodes are sorted by episode number and date (newest first)
- All text content is cleaned and properly escaped for CSV format
- Audio URLs point directly to MP3 files hosted on Libsyn

Your enhanced podcast data is now ready for your Framer website! 🎉

**🔥 Quick Start:** Use `govcon_giants_podcast_with_platforms.csv` - it contains 341 main podcast episodes with Apple Podcasts and Spotify URL columns, perfect for your website!