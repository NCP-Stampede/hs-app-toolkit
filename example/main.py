#!/usr/bin/env python3
"""
Example usage of hs-scraper-toolkit modules.

This script demonstrates how to use various scrapers in the toolkit,
including general athletics scrapers and school-specific modules.

Requirements:
    - ChromeDriver installed and in PATH (for Athletic.net and Athletics Schedule)
    - Internet connection
    - hs-scraper-toolkit package installed
"""

import pandas as pd
import sys
import os

# Method 1: For local development (current setup)
# Add the package root to Python path to import modules directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Athletics.MaxPrepRoster import MaxPrepRoster
from Athletics.AthleticNetTrackField import AthleticNetTrackField
from Northside.AthleticsSchedule import AthleticsSchedule
from Northside.GeneralEvent import GeneralEvent

# Method 2: After installing the package (pip install .)
# Uncomment the lines below and comment out the lines above
# from hs_scraper_toolkit.Athletics.MaxPrepRoster import MaxPrepRoster
# from hs_scraper_toolkit.Athletics.AthleticNetTrackField import AthleticNetTrackField
# from hs_scraper_toolkit.Northside.AthleticsSchedule import AthleticsSchedule
# from hs_scraper_toolkit.Northside.GeneralEvent import GeneralEvent

def main():
    """Run examples of all available scrapers."""
    
    print("=== HS Scraper Toolkit Examples ===\n")
    
    # Example 1: MaxPreps Roster Scraping
    print("1. MaxPreps Roster Scraping")
    print("-" * 30)
    try:
        maxprep_scraper = MaxPrepRoster("https://www.maxpreps.com/il/chicago/northside-mustangs")
        
        # Scrape all sports
        print("Scraping all sports...")
        all_roster_data = maxprep_scraper.scrape()
        print(f"Found {len(all_roster_data)} total athletes")
        
        # Filter by specific criteria
        print("Scraping basketball only...")
        basketball_data = maxprep_scraper.scrape(
            sports=['basketball'],
            genders=['boys'],
            seasons=['winter'],
            levels=['varsity']
        )
        print(f"Found {len(basketball_data)} basketball players")
        if not basketball_data.empty:
            print(basketball_data.head())
            
    except Exception as e:
        print(f"Error with MaxPreps scraper: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Athletic.net Track & Field
    print("2. Athletic.net Track & Field")
    print("-" * 30)
    try:
        athletic_scraper = AthleticNetTrackField("https://www.athletic.net/team/19718")
        
        # Scrape athletes
        print("Scraping athletes...")
        athletes = athletic_scraper.scrape_athletes(['cross-country'])
        print(f"Found {len(athletes)} cross country athletes")
        
        # Scrape events
        print("Scraping events...")
        events = athletic_scraper.scrape_events(['cross-country'], [2024])
        print(f"Found {len(events)} events")
        
        if not athletes.empty:
            print("\nSample athlete data:")
            print(athletes.head())
            
    except Exception as e:
        print(f"Error with Athletic.net scraper: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Northside Athletics Schedule
    print("3. Northside College Prep - Athletics Schedule")
    print("-" * 45)
    try:
        athletics_scraper = AthleticsSchedule()
        
        print("Scraping athletics schedule (this may take 2-5 minutes)...")
        print("The scraper will automatically scroll through all events...")
        
        schedule_data = athletics_scraper.scrape()
        print(f"Found {len(schedule_data)} scheduled events")
        
        if not schedule_data.empty:
            print("\nSample schedule data:")
            print(schedule_data[['date', 'sport', 'opponent', 'location', 'home']].head())
            
            # Show some statistics
            print(f"\nSchedule Statistics:")
            print(f"Sports: {schedule_data['sport'].nunique()}")
            print(f"Unique opponents: {schedule_data['opponent'].nunique()}")
            print(f"Home games: {schedule_data['home'].sum()}")
            print(f"Away games: {(~schedule_data['home']).sum()}")
            
    except Exception as e:
        print(f"Error with Athletics Schedule scraper: {e}")
        print("Note: This scraper requires ChromeDriver to be installed")
    
    print("\n" + "="*50 + "\n")
    
    # Example 4: Northside General Events
    print("4. Northside College Prep - General Events")
    print("-" * 42)
    try:
        # Scrape events for first half of 2025
        events_scraper = GeneralEvent(
            months=range(1, 7),  # January through June
            years=range(2025, 2026)  # 2025 only
        )
        
        print("Scraping general school events...")
        events_data = events_scraper.scrape()
        print(f"Found {len(events_data)} school events")
        
        if not events_data.empty:
            print("\nSample events data:")
            print(events_data.head())
            
            # Show events by month
            events_data['month'] = pd.to_datetime(events_data['date']).dt.month
            monthly_counts = events_data['month'].value_counts().sort_index()
            print(f"\nEvents by month:")
            for month, count in monthly_counts.items():
                month_name = pd.to_datetime(f"2025-{month:02d}-01").strftime("%B")
                print(f"  {month_name}: {count} events")
                
    except Exception as e:
        print(f"Error with General Events scraper: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 5: Data Analysis
    print("5. Example Data Analysis")
    print("-" * 25)
    print("Once you have the data, you can perform various analyses:")
    
    analysis_examples = """
    # Filter data
    home_basketball = schedule_data[
        (schedule_data['sport'] == 'Basketball') & 
        (schedule_data['home'] == True)
    ]
    
    # Group by sport
    sports_summary = schedule_data.groupby('sport').agg({
        'opponent': 'count',
        'home': 'sum'
    }).rename(columns={'opponent': 'total_games', 'home': 'home_games'})
    
    # Export to CSV
    schedule_data.to_csv('athletics_schedule.csv', index=False)
    events_data.to_csv('school_events.csv', index=False)
    
    # Combine with other data sources
    all_school_data = pd.concat([
        schedule_data[['date', 'name', 'location']].rename(columns={'sport': 'name'}),
        events_data[['date', 'name', 'location']]
    ], ignore_index=True)
    """
    
    print(analysis_examples)
    
    print("=== Examples Complete ===")
    print("\nFor more detailed documentation:")
    print("- README.md: General usage and installation")
    print("- docs/northside-modules.md: Detailed Northside module documentation")
    print("- CONTRIBUTING.md: Guidelines for adding your school's scrapers")

if __name__ == "__main__":
    main()