# Example implementation of hs-scraper-toolkit package
# 
# Method 1: For local development (current setup)
# Add the package root to Python path to import modules directly
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Athletics.MaxPrepRosterScraper import MaxPrepRosterScraper

# Method 2: After installing the package (pip install .)
# Uncomment the line below and comment out the lines above
# from hs_scraper_toolkit.Athletics.MaxPrepRosterScraper import MaxPrepRosterScraper

MyRosterScraper = MaxPrepRosterScraper("https://www.maxpreps.com/il/chicago/northside-mustangs")
print(MyRosterScraper.scrape())
print(MyRosterScraper.roster)