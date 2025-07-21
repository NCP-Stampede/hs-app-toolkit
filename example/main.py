# Example implementation of hs-scraper-toolkit package
# 
# Method 1: For local development (current setup)
# Add the package root to Python path to import modules directly
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Athletics.MaxPrepRoster import MaxPrepRoster
from Athletics.AthleticNetTrackField import AthleticNetTrackField

# Method 2: After installing the package (pip install .)
# Uncomment the lines below and comment out the lines above
# from hs_scraper_toolkit.Athletics.MaxPrepRoster import MaxPrepRoster
# from hs_scraper_toolkit.Athletics.AthleticNetTrackField import AthleticNetTrackField

# Example usage of MaxPrepRoster
print("=== MaxPreps Roster Scraper Example ===")
maxprep_scraper = MaxPrepRoster("https://www.maxpreps.com/il/chicago/northside-mustangs")
roster_data = maxprep_scraper.scrape()
print(f"Scraped {len(roster_data)} athletes from MaxPreps")
print(roster_data.head())

print("\n=== Athletic.net Track & Field Scraper Example ===")
# Example usage of AthleticNetTrackField
# Note: This requires ChromeDriver and may take several minutes to complete
athletic_net_scraper = AthleticNetTrackField("https://www.athletic.net/team/19718")

# Scrape athlete roster
print("Scraping athletes...")
athletes_data = athletic_net_scraper.scrape_athletes(['cross-country'])
print(f"Scraped {len(athletes_data)} athletes from Athletic.net")
print(athletes_data.head())

# Scrape event schedule
print("Scraping events...")
events_data = athletic_net_scraper.scrape_events(['cross-country'], [2024])
print(f"Scraped {len(events_data)} events from Athletic.net")
print(events_data.head())