# hs-scraper-toolkit

A comprehensive toolkit for scraping high school sports data from various athletic websites including MaxPreps and Athletic.net.

## Features

- **MaxPreps Roster Scraping**: Extract detailed roster information including player names, numbers, positions, grades, and more
- **Athletic.net Track & Field Data**: Scrape athlete rosters and event schedules for track & field and cross country
- **Flexible Filtering**: Filter data by sport, gender, season, and competition level
- **Easy Integration**: Simple Python classes with pandas DataFrame outputs

## Installation

```bash
# Install from local directory
pip install .

# Install with development dependencies
pip install -e ".[dev]"
```

## Dependencies

- `beautifulsoup4>=4.9.0` - HTML parsing
- `requests>=2.25.0` - HTTP requests
- `pandas>=1.3.0` - Data manipulation
- `selenium>=4.0.0` - Web automation (for Athletic.net)

## Quick Start

### MaxPreps Roster Scraping

```python
from hs_scraper_toolkit.Athletics.MaxPrepRoster import MaxPrepRoster

# Initialize scraper with team URL
scraper = MaxPrepRoster("https://www.maxpreps.com/il/chicago/northside-mustangs")

# Scrape all available sports
roster_data = scraper.scrape()

# Filter by specific criteria
basketball_data = scraper.scrape(
    sports=['basketball'],
    genders=['boys'],
    seasons=['winter'],
    levels=['varsity']
)

print(f"Found {len(roster_data)} athletes")
print(roster_data.head())
```

### Athletic.net Track & Field Scraping

```python
from hs_scraper_toolkit.Athletics.AthleticNetTrackField import AthleticNetTrackField

# Initialize scraper with team URL
scraper = AthleticNetTrackField("https://www.athletic.net/team/19718")

# Scrape athlete rosters
athletes = scraper.scrape_athletes(['cross-country', 'track-and-field-outdoor'])

# Scrape event schedules
events = scraper.scrape_events(['cross-country'], [2024, 2025])

print(f"Found {len(athletes)} athletes")
print(f"Found {len(events)} events")
```

## Athletics Module

### MaxPrepRoster

Scrapes roster data from MaxPreps team pages.

**Supported Data:**
- Athlete names and jersey numbers
- Sports, seasons, and competition levels
- Player positions and grade levels
- Gender categories

**Supported Sports:** All sports available on MaxPreps (basketball, football, soccer, etc.)

### AthleticNetTrackField

Scrapes track & field and cross country data from Athletic.net using Selenium WebDriver.

**Supported Data:**
- Athlete rosters with names and gender
- Event schedules with dates and locations
- Meet information and venues

**Supported Sports:**
- Cross Country (`cross-country`)
- Outdoor Track & Field (`track-and-field-outdoor`) 
- Indoor Track & Field (`track-and-field-indoor`)

**Requirements:**
- ChromeDriver must be installed and accessible in PATH
- Stable internet connection (scraping may take several minutes)

## Data Output

Both scrapers return pandas DataFrames with standardized column structures:

### Athlete Data Columns
- `name`: Athlete name
- `number`: Jersey number (0 for Athletic.net)
- `sport`: Sport type
- `season`: Season (fall/winter/spring)
- `level`: Competition level (varsity/jv/freshman)
- `gender`: Gender (boys/girls)
- `grade`: Grade level (9/10/11/12 or N/A)
- `position`: Player position (N/A for track/field)

### Event Data Columns (Athletic.net only)
- `name`: Event/meet name
- `date`: Event date
- `time`: Event time
- `gender`: Gender category
- `sport`: Sport type
- `level`: Competition level
- `opponent`: Opposing teams
- `location`: Event venue
- `home`: Home event indicator

## Examples

See the `example/main.py` file for comprehensive usage examples.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues, questions, or contributions, please visit the GitHub repository.
