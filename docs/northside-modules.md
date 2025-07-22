# Northside College Prep Modules

This document provides detailed documentation for the Northside College Prep specific scraping modules included in the hs-scraper-toolkit.

## Overview

The Northside modules are designed to scrape data from Northside College Prep's specific websites and platforms. These modules serve as examples of school-specific implementations and demonstrate how to extend the toolkit for custom school websites.

## Modules

### AthleticsSchedule

The `AthleticsSchedule` class scrapes athletics schedule data from the Northside Prep Athletics website.

#### Features

- **Dynamic Content Loading**: Uses Selenium WebDriver to handle JavaScript-rendered content
- **Intelligent Scrolling**: Automatically scrolls through the page to load all events
- **Comprehensive Data Extraction**: Captures date, time, sport, gender, level, opponent, location, and home/away status
- **Structured Output**: Returns data in a pandas DataFrame for easy analysis

#### Usage

```python
from hs_scraper_toolkit.Northside.AthleticsSchedule import AthleticsSchedule

# Initialize the scraper
scraper = AthleticsSchedule()

# Scrape the athletics schedule
schedule_data = scraper.scrape()

print(f"Found {len(schedule_data)} scheduled events")
print(schedule_data.head())
```

#### Data Structure

The scraper returns a pandas DataFrame with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `date` | str | Event date (e.g., "January 15, 2025") |
| `time` | str | Event time (e.g., "3:30 PM") |
| `gender` | str | Gender category ("boys", "girls", "coed") |
| `sport` | str | Sport name (e.g., "Basketball", "Soccer") |
| `level` | str | Competition level ("varsity", "jv", "freshman") |
| `opponent` | str | Opposing team name |
| `location` | str | Venue/location of the event |
| `home` | bool | True if home game, False if away |

#### Technical Details

- **WebDriver**: Uses Chrome WebDriver in headless mode
- **Scrolling Strategy**: Implements intelligent scrolling with content detection
- **Selectors**: Uses CSS selectors to target specific elements:
  - Events: `h2.mb-1.font-heading.text-xl`
  - Dates: `h3.uppercase`
  - Times: `p.text-base.font-bold[data-testid*="time"]`
  - Sports: `p.text-base.font-bold[data-testid*='activity-name']`
  - Locations: `p.text-sm.font-medium[data-testid*='venue']`
  - Levels/Genders: `div.text-sm.font-medium.text-core-contrast.text-opacity-80.xl\:text-base[data-testid*='gender-level']`
  - Home/Away: `div.inline-flex.items-center.gap-1`

#### Example Output

```python
     date      time  gender      sport    level         opponent              location  home
0  Jan 15   3:30 PM    boys Basketball  varsity  Lane Tech Eagles   Northside College...  True
1  Jan 18   6:00 PM   girls     Soccer       jv      Lincoln Park  Lincoln Park Field... False
2  Jan 20  11:00 AM    boys   Swimming  varsity    Whitney Young    Whitney Young Aqua... False
```

#### Requirements

- **ChromeDriver**: Must be installed and accessible in system PATH
- **Selenium**: For web automation and dynamic content loading
- **BeautifulSoup**: For HTML parsing after page load
- **Pandas**: For data structure and manipulation

### GeneralEvent

The `GeneralEvent` class scrapes general school events from the Northside College Prep main website calendar.

#### Features

- **Multi-Month/Year Support**: Can scrape events across multiple months and years
- **Calendar Integration**: Extracts events from the school's JSP-based calendar system
- **Flexible Date Range**: Customizable month and year ranges for targeted scraping
- **Event Metadata**: Captures event names, dates, times, and creation source

#### Usage

```python
from hs_scraper_toolkit.Northside.GeneralEvent import GeneralEvent

# Initialize with default range (all months, 2025-2026)
scraper = GeneralEvent()

# Or specify custom ranges
scraper = GeneralEvent(
    months=range(1, 7),  # January through June
    years=range(2025, 2026)  # 2025 only
)

# Scrape events
events_data = scraper.scrape()

print(f"Found {len(events_data)} school events")
print(events_data.head())
```

#### Data Structure

The scraper returns a pandas DataFrame with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `date` | str | Event date in MM/DD/YYYY format |
| `time` | str | Event time or "All Day" for full-day events |
| `name` | str | Event name/title |
| `createdBy` | str | Source of the event (always "Northside College Prep Calendar") |

#### Technical Details

- **HTTP Requests**: Uses the requests library for efficient data fetching
- **URL Pattern**: Accesses calendar via JSP parameters: 
  ```
  https://www.northsideprep.org/apps/events/view_calendar.jsp?id=0&m={month-1}&y={year}
  ```
- **Error Handling**: Implements robust error handling for network issues
- **Selectors**: Targets calendar-specific CSS classes:
  - Event cells: `div.day.prev` and `div.day.prev.weekend`
  - Event links: `a.eventInfoAnchor`
  - Date labels: `span.dayLabel`
  - Event times: `span.edEventDate`

#### Example Output

```python
        date      time                    name                        createdBy
0   1/15/2025   8:00 AM         Parent Teacher Conferences  Northside College Prep Calendar
1   1/18/2025   All Day             Martin Luther King Day  Northside College Prep Calendar
2   1/22/2025   7:00 PM                Science Fair Setup  Northside College Prep Calendar
```

#### Requirements

- **Requests**: For HTTP requests to the calendar system
- **BeautifulSoup**: For HTML parsing
- **Pandas**: For data structure and manipulation

## Installation & Setup

These modules are included in the main hs-scraper-toolkit package:

```bash
pip install hs-scraper-toolkit
```

For the AthleticsSchedule module specifically, ensure ChromeDriver is installed:

```bash
# macOS (using Homebrew)
brew install chromedriver

# Linux (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install chromium-chromedriver

# Windows
# Download from https://chromedriver.chromium.org/
```

## Contributing School-Specific Modules

These Northside modules serve as templates for creating scrapers for other schools. To contribute a new school module:

1. **Create a new directory** under `hs_scraper_toolkit/` with your school name
2. **Follow the established patterns**:
   - Use pandas DataFrames for output
   - Implement proper error handling
   - Include comprehensive docstrings
   - Use consistent naming conventions
3. **Add documentation** following this template
4. **Submit a pull request** with your implementation

See the main README's contributing section for detailed guidelines.

## Troubleshooting

### Common Issues

1. **ChromeDriver Not Found** (AthleticsSchedule)
   - Ensure ChromeDriver is installed and in PATH
   - Check Chrome browser version compatibility

2. **Network Timeouts** (GeneralEvent)
   - Check internet connection
   - Verify school website accessibility
   - Consider implementing retry logic

3. **Selector Changes**
   - Website updates may break selectors
   - Inspect page elements to update CSS selectors
   - Report issues via GitHub

### Performance Tips

1. **AthleticsSchedule**:
   - Scrolling can take 2-5 minutes for full year
   - Consider running during off-peak hours
   - Monitor memory usage for large datasets

2. **GeneralEvent**:
   - Limit month/year ranges for faster execution
   - Implement caching for repeated requests
   - Use concurrent requests (with rate limiting)

## Support

For issues specific to these modules:
- Check the main [GitHub Issues](https://github.com/NCP-Stampede/hs-scraper-toolkit/issues)
- Include specific error messages and module names
- Provide sample data/URLs when possible
