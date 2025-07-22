# Contributing to hs-scraper-toolkit

Thank you for your interest in contributing to the hs-scraper-toolkit! We especially welcome contributions of school-specific scrapers that can help other developers and schools.

## Table of Contents

- [Getting Started](#getting-started)
- [Contributing School-Specific Scrapers](#contributing-school-specific-scrapers)
- [Code Standards](#code-standards)
- [Documentation Requirements](#documentation-requirements)
- [Submission Process](#submission-process)
- [Community Guidelines](#community-guidelines)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Basic knowledge of web scraping (BeautifulSoup, Selenium, requests)
- Pandas for data manipulation

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/hs-scraper-toolkit.git
   cd hs-scraper-toolkit
   ```
3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b add-[school-name]-scrapers
   ```

## Contributing School-Specific Scrapers

### Why We Need Your School's Scrapers

Every school has unique websites, data structures, and platforms. By contributing scrapers for your school:

- You help other students, parents, and developers access athletic and event data
- Your code serves as a template for schools with similar website structures
- You contribute to building the most comprehensive high school data toolkit available

### Supported School Types

We welcome scrapers for all types of educational institutions:

- **Public Schools**: District websites, state athletics associations
- **Private Schools**: Independent school platforms and custom sites  
- **Charter Schools**: Network-specific platforms (KIPP, Success Academy, etc.)
- **Specialized Schools**: Magnet schools, STEM academies, arts schools
- **Regional Systems**: County or regional athletics platforms

### What Data to Scrape

#### Athletics Data
- **Schedules**: Game dates, times, opponents, locations, home/away status
- **Rosters**: Player names, numbers, positions, grades, photos
- **Results**: Scores, statistics, standings, tournament results
- **News/Announcements**: Athletic department updates, awards, recruiting news

#### Academic/General Events
- **School Calendar**: Important dates, holidays, testing schedules
- **Events**: Performances, fundraisers, meetings, conferences
- **Announcements**: General school news and updates

#### Standards Data
- **Test Scores**: State testing results, SAT/ACT averages (if public)
- **Demographics**: School size, graduation rates (if public)

### Directory Structure for School Modules

Create your school's module following this structure:

```
hs_scraper_toolkit/
└── YourSchoolName/           # Use PascalCase, no spaces
    ├── __init__.py          # Required: import your main classes
    ├── AthleticsSchedule.py # Athletics calendar/schedule scraper
    ├── GeneralEvent.py      # School events and calendar
    ├── RosterData.py        # Team rosters (optional)
    ├── NewsData.py          # School news/announcements (optional)
    └── README.md            # School-specific documentation
```

### Implementation Guidelines

#### 1. Class Structure

Each scraper should follow this basic pattern:

```python
import pandas as pd
from selenium import webdriver  # or requests for static content
from bs4 import BeautifulSoup
import time

class YourSchoolAthleticsSchedule:
    """
    Scraper for [School Name] athletics schedule.
    
    This class scrapes athletic event data from [School Name]'s 
    athletics website at [URL].
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the scraper.
        
        Args:
            **kwargs: Additional configuration options
        """
        # Initialize DataFrame with standard columns
        self.schedule = pd.DataFrame(columns=[
            "date", "time", "gender", "sport", "level", 
            "opponent", "location", "home"
        ])
    
    def scrape(self) -> pd.DataFrame:
        """
        Scrape athletics schedule data.
        
        Returns:
            pd.DataFrame: Schedule data with standardized columns
            
        Raises:
            requests.RequestException: If unable to fetch data
            ValueError: If data parsing fails
        """
        # Your scraping implementation here
        return self.schedule
```

#### 2. Standard DataFrame Columns

Use these standardized column names for consistency:

**Athletics Schedule Data:**
- `date`: Event date (string, readable format)
- `time`: Event time (string, e.g., "3:30 PM")
- `gender`: "boys", "girls", "coed", or "mixed"
- `sport`: Sport name (e.g., "Basketball", "Soccer")
- `level`: "varsity", "jv", "freshman", "sophomore", etc.
- `opponent`: Opposing team name
- `location`: Venue/address
- `home`: Boolean (True for home games)

**General Events Data:**
- `date`: Event date
- `time`: Event time or "All Day"
- `name`: Event name/title
- `description`: Event description (optional)
- `location`: Event location (optional)
- `createdBy`: Source/creator of event

**Roster Data:**
- `name`: Player name
- `number`: Jersey number (int, or 0 if not available)
- `sport`: Sport name
- `season`: "fall", "winter", "spring"
- `level`: Competition level
- `gender`: Gender category
- `grade`: Grade level (9, 10, 11, 12, or "N/A")
- `position`: Player position ("N/A" if not applicable)

#### 3. Error Handling

Implement robust error handling:

```python
import requests
from selenium.common.exceptions import WebDriverException

def scrape(self):
    try:
        # Scraping logic here
        pass
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return self.schedule  # Return empty DataFrame
    except WebDriverException as e:
        print(f"WebDriver error: {e}")
        return self.schedule
    except Exception as e:
        print(f"Unexpected error: {e}")
        return self.schedule
```

#### 4. Rate Limiting and Ethics

- **Add delays** between requests: `time.sleep(1)` minimum
- **Respect robots.txt** when possible
- **Use headless browsers** for Selenium to reduce resource usage
- **Implement retries** with exponential backoff for failed requests
- **Cache results** when appropriate to reduce server load

### Code Quality Standards

#### Python Style
- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Write **comprehensive docstrings** for all classes and methods
- Use **meaningful variable names** and avoid single-letter variables

#### Dependencies
- Use the **minimum required dependencies**
- Prefer `requests` over `selenium` when possible (faster, lighter)
- Only use `selenium` for JavaScript-heavy sites that require it
- List all dependencies in your module's docstring

#### Example Quality Implementation

```python
from typing import Optional, List
import pandas as pd
import requests
from bs4 import BeautifulSoup

class ExampleSchoolSchedule:
    """
    Athletics schedule scraper for Example High School.
    
    Scrapes data from https://example-school.edu/athletics
    
    Dependencies:
        - requests>=2.25.0
        - beautifulsoup4>=4.9.0
        - pandas>=1.3.0
    """
    
    def __init__(self, base_url: str = "https://example-school.edu") -> None:
        """Initialize scraper with configurable base URL."""
        self.base_url = base_url
        self.schedule = pd.DataFrame(columns=[
            "date", "time", "gender", "sport", "level", 
            "opponent", "location", "home"
        ])
    
    def scrape(self, sports: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Scrape athletics schedule.
        
        Args:
            sports: List of sports to filter by (optional)
            
        Returns:
            DataFrame with schedule data
        """
        # Implementation here
        return self.schedule
```

## Documentation Requirements

### 1. Module README.md

Create a `README.md` file in your school's directory with:

```markdown
# [School Name] Scrapers

Brief description of your school and the scrapers provided.

## Available Scrapers

- **AthleticsSchedule**: Description of what it scrapes
- **GeneralEvent**: Description of what it scrapes
- **[OtherScrapers]**: Additional scrapers

## Requirements

- List any special requirements (ChromeDriver, etc.)
- Any authentication or access limitations

## Usage Examples

[Provide clear code examples]

## Data Sources

- List the specific URLs your scrapers target
- Mention any website-specific quirks or limitations

## Troubleshooting

Common issues and solutions specific to your school's websites.
```

### 2. Inline Documentation

- **Class docstrings**: Explain what the scraper does and what sites it targets
- **Method docstrings**: Document parameters, return values, and exceptions
- **Inline comments**: Explain complex logic or website-specific workarounds

### 3. Usage Examples

Include working examples in your documentation:

```python
# Simple usage
from hs_scraper_toolkit.YourSchool.AthleticsSchedule import AthleticsSchedule

scraper = AthleticsSchedule()
data = scraper.scrape()
print(f"Found {len(data)} events")

# Advanced usage with filtering
data = scraper.scrape(sports=['basketball', 'soccer'])
basketball_games = data[data['sport'] == 'Basketball']
```

## Submission Process

### 1. Pre-Submission Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] All classes have comprehensive docstrings
- [ ] Error handling is implemented
- [ ] DataFrames use standard column names
- [ ] README.md is created with examples
- [ ] Code has been tested with actual school website

### 2. Pull Request Requirements

When submitting your pull request:

1. **Title**: "Add [School Name] scrapers"
2. **Description** should include:
   - Name and location of your school
   - What data your scrapers collect
   - Any special requirements or limitations
   - Links to the websites being scraped (if public)
   - Screenshots of sample output (optional but helpful)

3. **Changes Made**:
   - List all files added
   - Mention any changes to existing files
   - Note any new dependencies

### 3. Review Process

Your contribution will be reviewed for:
- **Code quality**: Style, documentation, error handling
- **Functionality**: Does it work as described?
- **Standards compliance**: Follows established patterns
- **Documentation**: Clear and comprehensive

We may request changes or improvements before merging. This is normal and helps maintain code quality!

## Community Guidelines

### Be Respectful
- Respect your school's terms of service and robots.txt
- Don't include any private or sensitive information
- Be considerate of website server resources

### Be Helpful
- Write clear documentation for future users
- Respond to questions about your scrapers
- Help troubleshoot issues when possible

### Be Collaborative
- Welcome feedback and suggestions
- Consider implementing requested features
- Help review other contributors' school scrapers

## Getting Help

### Questions?
- **GitHub Discussions**: Ask general questions about contributing
- **GitHub Issues**: Report bugs or request features
- **Code Review**: Tag maintainers in your PR for faster review

### Resources
- **Existing Examples**: Look at `hs_scraper_toolkit/Northside/` for patterns
- **Main Documentation**: See the main README.md for overall project info
- **Web Scraping Help**: Python requests/BeautifulSoup/Selenium documentation

## Recognition

Contributors of school-specific scrapers will be:
- Listed in the main README.md
- Credited in their module's documentation  
- Mentioned in release notes
- Invited to help review future school contributions

Thank you for helping build the most comprehensive high school data toolkit available!
