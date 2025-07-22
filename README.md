# hs-scraper-toolkit

[![PyPI version](https://badge.fury.io/py/hs-scraper-toolkit.svg)](https://badge.fury.io/py/hs-scraper-toolkit)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive toolkit for scraping high school sports data from various athletic websites including MaxPreps and Athletic.net.

## Features

- **MaxPreps Roster Scraping**: Extract detailed roster information including player names, numbers, positions, grades, and more
- **Athletic.net Track & Field Data**: Scrape athlete rosters and event schedules for track & field and cross country
- **Flexible Filtering**: Filter data by sport, gender, season, and competition level
- **Easy Integration**: Simple Python classes with pandas DataFrame outputs
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

We welcome contributions! Here's how to get started:

1. Fork the repository on GitHub
2. Clone your fork locally: `git clone https://github.com/YOUR-USERNAME/hs-scraper-toolkit.git`
3. Create a feature branch: `git checkout -b feature-name`
4. Install development dependencies: `pip install -e ".[dev]"`
5. Make your changes and add tests if applicable
6. Run tests and ensure code quality
7. Commit your changes: `git commit -m "Add feature"`
8. Push to your fork: `git push origin feature-name`
9. Submit a pull request on GitHub

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

## Disclaimer

This tool is for educational and research purposes. Please respect the terms of service of the websites you scrape and implement appropriate rate limiting and ethical scraping practices.

## License

MIT License - see [LICENSE](LICENSE) file for details.
