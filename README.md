# hs-scraper-toolkit

[![PyPI version](https://badge.fury.io/py/hs-scraper-toolkit.svg)](https://badge.fury.io/py/hs-scraper-toolkit)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive toolkit for scraping high school sports data from various athletic websites including MaxPreps and Athletic.net.

## Features

- **MaxPreps Roster Scraping**: Extract detailed roster information including player names, numbers, positions, grades, and more
- **Athletic.net Track & Field Data**: Scrape athlete rosters and event schedules for track & field and cross country
- **School-Specific Modules**: Pre-built scrapers for specific schools (Northside College Prep and more)
- **Flexible Filtering**: Filter data by sport, gender, season, and competition level
- **Easy Integration**: Simple Python classes with pandas DataFrame outputs
- **Extensible Design**: Framework for building custom school-specific scrapers
- **Production Ready**: Publicly available on PyPI with proper packaging

## Installation

The package is available on PyPI and can be installed with pip:

```bash
# Install from PyPI (recommended)
pip install hs-scraper-toolkit

# Install with development dependencies
pip install "hs-scraper-toolkit[dev]"

# Install from source (for development)
git clone https://github.com/NCP-Stampede/hs-scraper-toolkit.git
cd hs-scraper-toolkit
pip install -e ".[dev]"
```

## Dependencies

- `beautifulsoup4>=4.9.0` - HTML parsing
- `requests>=2.25.0` - HTTP requests
- `pandas>=1.3.0` - Data manipulation
- `selenium>=4.0.0` - Web automation (for Athletic.net)

## Quick Start

### Simple Import

```python
# Easy import from the main package
from hs_scraper_toolkit import AthleticNetTrackField, MaxPrepRoster

# Or import from specific modules
from hs_scraper_toolkit.Athletics.MaxPrepRoster import MaxPrepRoster
from hs_scraper_toolkit.Athletics.AthleticNetTrackField import AthleticNetTrackField

# School-specific modules
from hs_scraper_toolkit.Northside.AthleticsSchedule import AthleticsSchedule
from hs_scraper_toolkit.Northside.GeneralEvent import GeneralEvent
```

### MaxPreps Roster Scraping

```python
from hs_scraper_toolkit import MaxPrepRoster

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
from hs_scraper_toolkit import AthleticNetTrackField

# Initialize scraper with team URL
scraper = AthleticNetTrackField("https://www.athletic.net/team/19718")

# Scrape athlete rosters
athletes = scraper.scrape_athletes(['cross-country', 'track-and-field-outdoor'])

# Scrape event schedules
events = scraper.scrape_events(['cross-country'], [2024, 2025])

print(f"Found {len(athletes)} athletes")
print(f"Found {len(events)} events")
```

## School-Specific Modules

### Northside College Prep

The toolkit includes pre-built scrapers for Northside College Prep's specific websites:

#### Athletics Schedule Scraping

```python
from hs_scraper_toolkit.Northside.AthleticsSchedule import AthleticsSchedule

# Initialize scraper
scraper = AthleticsSchedule()

# Scrape athletics schedule (uses Selenium for dynamic content)
schedule_data = scraper.scrape()

print(f"Found {len(schedule_data)} scheduled events")
print(schedule_data[['date', 'sport', 'opponent', 'location']].head())
```

#### General School Events

```python
from hs_scraper_toolkit.Northside.GeneralEvent import GeneralEvent

# Initialize scraper (default: all months, 2025-2026)
scraper = GeneralEvent()

# Or specify custom date ranges
scraper = GeneralEvent(
    months=range(1, 7),  # January through June
    years=range(2025, 2026)  # 2025 only
)

# Scrape school events
events_data = scraper.scrape()

print(f"Found {len(events_data)} school events")
print(events_data.head())
```

**Note**: The Athletics Schedule scraper requires ChromeDriver to be installed and accessible in your system PATH.

For detailed documentation on school-specific modules, see [docs/northside-modules.md](docs/northside-modules.md).

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
- ChromeDriver must be installed and accessible in PATH for Selenium WebDriver
- Stable internet connection (scraping may take several minutes for large datasets)
- Python 3.7 or higher

## Package Information

- **Version**: 1.0.1
- **Author**: Tanmay Garg
- **License**: MIT
- **PyPI**: [hs-scraper-toolkit](https://pypi.org/project/hs-scraper-toolkit/)
- **Repository**: [GitHub](https://github.com/NCP-Stampede/hs-scraper-toolkit)

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

We welcome contributions! This project especially encourages developers to contribute scrapers for their own school's websites.

### Contributing School-Specific Scrapers

**We want YOUR school's scrapers!** If you've built a scraper for your high school's athletics website, calendar system, or any other school-specific platform, we'd love to include it in the toolkit.

#### Why Contribute Your School's Scrapers?

- **Help Other Schools**: Your implementation can serve as a template for similar school websites
- **Build Your Portfolio**: Get your code featured in a public package used by others
- **Learn Best Practices**: Collaborate with other developers and improve your scraping skills
- **Give Back**: Help build a comprehensive toolkit for the high school sports community

#### How to Contribute a School-Specific Scraper

1. **Create Your Module Structure**
   ```
   hs_scraper_toolkit/
   └── YourSchoolName/
       ├── __init__.py
       ├── AthleticsSchedule.py
       ├── EventCalendar.py
       └── RosterData.py (optional)
   ```

2. **Follow the Established Patterns**
   - Use pandas DataFrames for all output data
   - Implement proper error handling and logging
   - Include comprehensive docstrings and type hints
   - Use consistent naming conventions (see existing modules)
   - Handle dynamic content with appropriate tools (Selenium for JS, requests for static)

3. **Include Documentation**
   - Create a detailed README for your school's modules
   - Document all available methods and data structures
   - Provide usage examples and common troubleshooting tips
   - List any special requirements (ChromeDriver, API keys, etc.)

4. **Example Implementation Structure**
   ```python
   import pandas as pd
   from selenium import webdriver
   # or from requests import get

   class YourSchoolAthleticsSchedule:
       def __init__(self):
           self.schedule = pd.DataFrame(columns=["date", "time", "sport", "opponent", "location"])
       
       def scrape(self):
           # Your scraping logic here
           return self.schedule
   ```

#### Schools We'd Love to See

- **Public School Districts**: CPS, NYC DOE, LAUSD, and other major districts
- **Private Schools**: Independent schools with unique website structures  
- **Charter Schools**: KIPP, Success Academy, and other charter networks
- **Specialized Schools**: Magnet schools, art schools, STEM academies
- **Regional Powerhouses**: Schools known for specific sports or academics

#### What to Include in Your Contribution

- **Multiple Data Types**: Athletics, academics, general events, announcements
- **Robust Scraping**: Handle pagination, dynamic loading, authentication if needed
- **Data Standardization**: Follow existing column naming conventions
- **Error Handling**: Graceful failures with informative error messages
- **Documentation**: Clear examples and troubleshooting guides

### General Contribution Guidelines

1. Fork the repository on GitHub
2. Clone your fork locally: `git clone https://github.com/YOUR-USERNAME/hs-scraper-toolkit.git`
3. Create a feature branch: `git checkout -b add-[school-name]-scrapers`
4. Install development dependencies: `pip install -e ".[dev]"`
5. **Add your school's directory and modules**
6. **Update documentation and README**
7. Run tests and ensure code quality
8. Commit your changes: `git commit -m "Add [School Name] scrapers"`
9. Push to your fork: `git push origin add-[school-name]-scrapers`
10. Submit a pull request with detailed description

### Development Setup

```bash
# Clone the repository
git clone https://github.com/NCP-Stampede/hs-scraper-toolkit.git
cd hs-scraper-toolkit

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest

# Format code
black .

# Lint code
flake8 .
```

### Questions About Contributing?

- **Check existing issues** for school requests or similar implementations
- **Open a discussion** on GitHub to propose your school before starting
- **Look at the Northside modules** (`hs_scraper_toolkit/Northside/`) as examples
- **Ask questions** in GitHub Issues or Discussions - we're here to help!

We're excited to see scrapers for schools across the country. Every contribution helps build a more comprehensive toolkit for the high school community!

## Changelog

### Version 1.0.1 (Latest)
- Fixed package structure for proper PyPI distribution
- Added easy import from main package (`from hs_scraper_toolkit import ...`)
- Improved documentation and examples
- Added comprehensive .gitignore
- Published to PyPI

### Version 1.0.0
- Initial release
- MaxPreps roster scraping
- Athletic.net track & field scraping
- Basic package structure

## Support

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/NCP-Stampede/hs-scraper-toolkit/issues)
- **Discussions**: Ask questions or discuss usage on [GitHub Discussions](https://github.com/NCP-Stampede/hs-scraper-toolkit/discussions)
- **PyPI**: Visit the [PyPI package page](https://pypi.org/project/hs-scraper-toolkit/)
- **Contributing Schools**: See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on adding your school's scrapers

## School Contributions Wanted! 🏫

We're actively seeking contributors to add scrapers for their high school websites! Whether your school uses:

- **Custom athletics platforms** (TeamUp, SportsEngine, etc.)
- **District-wide systems** (CPS, NYC DOE, LAUSD)
- **School-specific websites** with unique structures
- **Regional athletics associations** 

Your contribution can help students, parents, and developers across the country access their school data programmatically.

**Current School Modules:**
- ✅ **Northside College Prep** (Chicago, IL) - Athletics Schedule & General Events

**Schools We'd Love to See:**
- 🎯 **Lane Tech College Prep** (Chicago, IL)
- 🎯 **Whitney Young Magnet** (Chicago, IL) 
- 🎯 **Walter Payton College Prep** (Chicago, IL)
- 🎯 **Lincoln Park High School** (Chicago, IL)
- 🎯 **Your School Here!**

See our [detailed contribution guide](CONTRIBUTING.md) for step-by-step instructions on adding your school's scrapers.

## Disclaimer

This tool is for educational and research purposes. Please respect the terms of service of the websites you scrape and implement appropriate rate limiting and ethical scraping practices.

## License

MIT License - see [LICENSE](LICENSE) file for details.
