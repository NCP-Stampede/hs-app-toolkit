# [School Name] Scrapers Template

Use this template when creating scrapers for your school. Replace [School Name] with your actual school name throughout this file.

## School Information

- **School Name**: [Full School Name]
- **Location**: [City, State]
- **School Type**: [Public/Private/Charter]
- **Website**: [School website URL]
- **Athletics Site**: [Athletics website URL if different]

## Available Scrapers

### AthleticsSchedule

Brief description of what athletics data this scraper collects.

**Data Source**: [URL of the athletics schedule page]

**Features**:
- [List key features, e.g., "Dynamic content loading", "Multi-sport support"]
- [Any special capabilities]

**Requirements**:
- [List any special requirements like ChromeDriver, authentication, etc.]

### GeneralEvent

Brief description of what general school events this scraper collects.

**Data Source**: [URL of the school calendar/events page]

**Features**:
- [List key features]
- [Date range capabilities]

**Requirements**:
- [List any special requirements]

## Installation & Usage

```python
# Import your school's modules
from hs_scraper_toolkit.[SchoolName].AthleticsSchedule import AthleticsSchedule
from hs_scraper_toolkit.[SchoolName].GeneralEvent import GeneralEvent

# Athletics Schedule Example
athletics_scraper = AthleticsSchedule()
schedule_data = athletics_scraper.scrape()
print(f"Found {len(schedule_data)} athletic events")
print(schedule_data.head())

# General Events Example  
events_scraper = GeneralEvent()
events_data = events_scraper.scrape()
print(f"Found {len(events_data)} school events")
print(events_data.head())
```

## Data Structure

### Athletics Schedule DataFrame

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `date` | str | Event date | "January 15, 2025" |
| `time` | str | Event time | "3:30 PM" |
| `gender` | str | Gender category | "boys", "girls", "coed" |
| `sport` | str | Sport name | "Basketball" |
| `level` | str | Competition level | "varsity", "jv", "freshman" |
| `opponent` | str | Opposing team | "Lincoln High School" |
| `location` | str | Venue/location | "Home Gym" |
| `home` | bool | Home game indicator | True, False |

### General Events DataFrame

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `date` | str | Event date | "1/15/2025" |
| `time` | str | Event time | "7:00 PM" or "All Day" |
| `name` | str | Event name | "Parent Teacher Conferences" |
| `createdBy` | str | Event source | "[School Name] Calendar" |

## Technical Implementation

### Web Scraping Approach

- **Static Content**: Uses `requests` + `BeautifulSoup`
- **Dynamic Content**: Uses `selenium` + `ChromeDriver`
- **Rate Limiting**: [Describe any rate limiting implemented]

### CSS Selectors Used

**Athletics Schedule**:
- Events: `[CSS selector for events]`
- Dates: `[CSS selector for dates]`
- Times: `[CSS selector for times]`
- Sports: `[CSS selector for sports]`
- [Other key selectors]

**General Events**:
- Event containers: `[CSS selector]`
- Event titles: `[CSS selector]`
- Event dates: `[CSS selector]`
- [Other key selectors]

### Error Handling

- Network timeouts: [How handled]
- Missing elements: [How handled]
- Dynamic content loading: [How handled]

## Website-Specific Notes

### Known Issues

- [List any known issues with the school's website]
- [Workarounds implemented]
- [Limitations of the current implementation]

### Performance Considerations

- **Expected runtime**: [Typical scraping time]
- **Memory usage**: [Approximate memory requirements]
- **Rate limiting**: [Recommendations for respectful scraping]

### Website Changes

- **Last verified**: [Date when scrapers were last tested]
- **Change frequency**: [How often the website structure changes]
- **Contact**: [School IT contact if available/relevant]

## Sample Output

### Athletics Schedule Sample

```
     date      time  gender      sport    level         opponent              location  home
0  Jan 15   3:30 PM    boys Basketball  varsity  Lane Tech Eagles   [School Name] Gym  True
1  Jan 18   6:00 PM   girls     Soccer       jv      Lincoln Park  Lincoln Park Field False
2  Jan 20  11:00 AM    boys   Swimming  varsity    Whitney Young    Whitney Young Pool False
```

### General Events Sample

```
        date      time                    name                        createdBy
0   1/15/2025   8:00 AM         Parent Teacher Conferences  [School Name] Calendar
1   1/18/2025   All Day             Martin Luther King Day  [School Name] Calendar
2   1/22/2025   7:00 PM                Science Fair Setup  [School Name] Calendar
```

## Testing

### Test Cases

- [ ] Scrapes current athletics schedule successfully
- [ ] Handles empty/no events gracefully
- [ ] Correctly parses all data fields
- [ ] Error handling works for network issues
- [ ] Performance is acceptable (< [X] minutes)

### Manual Testing Steps

1. [Step-by-step testing instructions]
2. [How to verify data accuracy]
3. [How to test error conditions]

## Troubleshooting

### Common Issues

1. **ChromeDriver Not Found** (if using Selenium)
   - Solution: [Installation instructions]

2. **Network Timeouts**
   - Solution: [Check connection, retry logic]

3. **Selector Changes**
   - Solution: [How to update selectors]

4. **School-Specific Issues**
   - [Any issues specific to your school's website]
   - [Solutions or workarounds]

## Contributing

If you encounter issues with this school's scrapers:

1. Check if the school's website has changed
2. Update selectors if necessary
3. Test thoroughly before submitting changes
4. Update this documentation

## Maintenance

- **Primary Maintainer**: [Your name/GitHub username]
- **Last Updated**: [Date]
- **Next Review**: [Suggested review date]

---

**Note**: This template should be customized for your specific school's implementation. Remove any sections that don't apply and add school-specific details where needed.
