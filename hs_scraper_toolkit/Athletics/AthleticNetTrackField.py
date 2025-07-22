from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


class AthleticNetTrackField:
    """
    Scraper for Athletic.net track and field data. This class fetches and parses meet results
    and athlete information from Athletic.net using Selenium WebDriver.
    
    This scraper is designed to work with Athletic.net team pages and supports scraping
    both event schedules and athlete rosters for cross country and track & field sports.
    
    Attributes:
        url (str): The base URL for the Athletic.net team page. Example: https://www.athletic.net/team/19718
        athletes (pd.DataFrame): DataFrame to store the scraped athlete information with columns:
            - name: Name of the athlete
            - number: Jersey number of the athlete (always 0 for Athletic.net)
            - sport: Sport played by the athlete (cross-country, track-and-field-outdoor, track-and-field-indoor)
            - season: Season of the sport (fall, winter, spring)
            - level: Level of play (varsity)
            - gender: Gender of the athlete (boys, girls)
            - grade: Grade of the athlete (N/A - not available from Athletic.net)
            - position: Position played by the athlete (N/A - not applicable for track/field)
        schedule (pd.DataFrame): DataFrame to store the scraped event schedule with columns:
            - name: Name of the meet/event
            - date: Date of the event
            - time: Time of the event (typically "All Day")
            - gender: Gender category (Boys, Girls)
            - sport: Sport type
            - level: Competition level (varsity)
            - opponent: Opposing teams (typically "Multiple Schools")
            - location: Event location/venue
            - home: Whether it's a home event (boolean)
    """
    
    def __init__(self, url):
        """
        Initializes the AthleticNetTrackField scraper with the provided URL.
        
        Args:
            url (str): The base URL for the Athletic.net team page (String, e.g., 
                      https://www.athletic.net/team/19718, REQUIRED).
                      
        Note:
            The URL should be the main team page on Athletic.net, not a specific sport page.
            The scraper will automatically append sport-specific paths as needed.
        """
        self.url = url
        self.athletes = pd.DataFrame(columns=["name", "number", "sport", "season", "level", "gender", "grade", "position"])
        self.schedule = pd.DataFrame(columns=["name", "date", "time", "gender", "sport", "level", "opponent", "location", "home"])

    def scrape_events(self, sports=['cross-country', 'track-and-field-outdoor', 'track-and-field-indoor'], years=[datetime.now().year, datetime.now().year + 1]) -> pd.DataFrame:
        """
        Scrapes event schedule data from Athletic.net for specified sports and years.
        
        This method navigates through Athletic.net team pages for each sport and year combination,
        clicks on individual events to extract location information, and compiles a comprehensive
        schedule of meets and competitions.
        
        Args:
            sports (list, optional): List of sports to scrape. Defaults to all track & field sports.
                Valid options: ['cross-country', 'track-and-field-outdoor', 'track-and-field-indoor']
            years (list, optional): List of years to scrape data for. Defaults to current and next year.
                
        Returns:
            pd.DataFrame: A DataFrame containing the scraped schedule information with columns:
                - name: Event name
                - date: Event date
                - time: Event time (typically "All Day")
                - gender: Gender category (Boys/Girls)
                - sport: Sport type
                - level: Competition level (varsity)
                - opponent: Opposing teams (typically "Multiple Schools")
                - location: Event location/venue
                - home: Whether it's a home event (boolean, typically False)
                
        Note:
            This method uses Selenium WebDriver in headless mode and may take several minutes
            to complete depending on the number of events. It automatically handles clicking
            on events to extract location data.
        """
        for sport in sports:
            for year in years:
                names = []
                dates = []

                if self.url[-1] == "/":
                    self.url = self.url[:-1]

                url = f"{self.url}/{sport}/{year}"

                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)

                wait = WebDriverWait(driver, 20)
                
                print("Waiting for events to load...")
                time.sleep(10)
                
                selectors_to_try = [
                    "div.px-2.w-100.d-flex.pointer",
                    "div[class*='px-2'][class*='pointer']",
                    "div.cal-item[class*='ng-tns']",
                    "[class*='cal-item'][class*='ng-star-inserted']"
                ]
                
                clickable_events = []
                for selector in selectors_to_try:
                    try:
                        elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        if elements:
                            print(f"Found {len(elements)} elements with selector: {selector}")
                            clickable_events = elements
                            break
                    except Exception as e:
                        print(f"Selector {selector} failed: {e}")
                        continue
                
                if not clickable_events:
                    print("No clickable events found with any selector")
                    driver.quit()
                    continue

                soup = BeautifulSoup(driver.page_source, 'html.parser')
                events = soup.select('div.px-2.w-100.d-flex.pointer')
                for event in events:
                    if event.find('span', class_="title"):
                        name = event.find('span', class_="title").get_text(strip=True)
                    if event.find('small', class_="date"):
                        dates.append(event.find('small', class_="date").get_text(strip=True))
                    boy_or_girl = event.find('img')
                    if event.find('img'):
                        if 'Girls' in boy_or_girl.get('ngbtooltip'):
                            names.append(name + " - Girls")
                        elif 'Boys' in boy_or_girl.get('ngbtooltip'):
                            names.append(name + " - Boys")

                names = [event.find('span', class_="title").get_text(strip=True) for event in events if event.find('span', class_="title")]
                dates = [event.find('small', class_="date").get_text(strip=True) for event in events if event.find('small', class_="date")]

                locations = []
                print(f"Found {len(clickable_events)} clickable events")
                
                for i, clickable_event in enumerate(clickable_events):
                    try:
                        print(f"Attempting to click event {i+1}")
                        
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", clickable_event)
                        time.sleep(2)
                        
                        wait.until(EC.element_to_be_clickable(clickable_event))
                        
                        try:
                            clickable_event.click()
                        except Exception as click_error:
                            print(f"Regular click failed, trying JavaScript click: {click_error}")
                            driver.execute_script("arguments[0].click();", clickable_event)
                        
                        time.sleep(3)
                        
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        
                        location_selectors = [
                            'div.cal-item.ng-tns-c342766986-3.ng-star-inserted.item-open',
                            'div[class*="item-open"]',
                            'div[class*="cal-item"][class*="item-open"]'
                        ]
                        
                        location_found = False
                        for loc_selector in location_selectors:
                            open_events = soup.select(loc_selector)
                            if open_events:
                                print(f"Found open event with selector: {loc_selector}")
                                for event in open_events:
                                    location_link = event.find('meet-venue-link')
                                    location_link = location_link.find('a')
                                    if location_link:
                                        location = location_link.get_text(strip=True)
                                        locations.append(location)
                                        print(f"Found location: {location}")
                                        location_found = True
                                break
                        
                        if not location_found:
                            print("No location found for this event")
                            locations.append("Location not found")
                        
                        try:
                            driver.execute_script("document.body.click();")
                            time.sleep(1)
                        except:
                            pass

                    except Exception as e:
                        print(f"Error clicking event {i+1}: {e}")
                        locations.append("Error retrieving location")

                for name in names:
                    if "girls" in name.lower():
                        new_row = pd.DataFrame({
                            "name": [name],
                            "date": [dates[names.index(name)]],
                            "time": ["All Day"],
                            "gender": ["Girls"],
                            "sport": [sport],
                            "level": ["varsity"],
                            "opponent": ["Multiple Schools"],
                            "location": [locations[names.index(name)]],
                            "home": [False],
                        })
                    elif "boys" in name.lower():
                        new_row = pd.DataFrame({
                            "name": [name],
                            "date": [dates[names.index(name)]],
                            "time": ["All Day"],
                            "gender": ["Boys"],
                            "sport": [sport],
                            "level": ["varsity"],
                            "opponent": ["Multiple Schools"],
                            "location": [locations[names.index(name)]],
                            "home": [False],
                        })
                    else:
                        new_row = pd.DataFrame({
                            "name": [name]*2,
                            "date": [dates[names.index(name)]]*2,
                            "time": ["All Day"]*2,
                            "gender": ["girls", "boys"],
                            "sport": [sport]*2,
                            "level": ["varsity"]*2,
                            "opponent": ["Multiple Schools"]*2,
                            "location": [locations[names.index(name)]]*2,
                            "home": [False]*2,
                        })

                    self.schedule = pd.concat([self.schedule, new_row], ignore_index=True)

        return self.schedule

    def scrape_athletes(self, sports=['cross-country', 'track-and-field-outdoor', 'track-and-field-indoor']) -> pd.DataFrame:
        """
        Scrapes athlete roster data from Athletic.net for specified sports.
        
        This method navigates through Athletic.net team pages for each sport,
        extracts athlete names and determines their gender based on team groupings.
        
        Args:
            sports (list, optional): List of sports to scrape athlete data for. 
                Defaults to all track & field sports.
                Valid options: ['cross-country', 'track-and-field-outdoor', 'track-and-field-indoor']
                
        Returns:
            pd.DataFrame: A DataFrame containing the scraped athlete information with columns:
                - name: Athlete name
                - number: Jersey number (always 0 for Athletic.net)
                - sport: Sport type
                - season: Sport season (fall/winter/spring)
                - level: Competition level (varsity)
                - gender: Athlete gender (boys/girls)
                - grade: Student grade (N/A - not available from Athletic.net)
                - position: Athlete position (N/A - not applicable for track/field)
        """

        for sport in sports:

            if self.url[-1] == "/":
                self.url = self.url[:-1]
            url = f"{self.url}/{sport}"

            try:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)

                print("Waiting for the page to load...")
                time.sleep(10)

                soup = BeautifulSoup(driver.page_source, 'html.parser')
            except Exception as e:
                print(f"Error parsing HTML content: {e}")
                continue

            columns = soup.find_all('div', class_='col-6 ng-star-inserted')

            for column in columns:
                athletes = column.find_all('span', class_='text-truncate')
                athletes = [athlete.get_text(strip=True) for athlete in athletes if athlete.get_text(strip=True)]
                
                gender = column.find('h4').get_text(strip=True).lower()

                if sport == "cross-country":
                    season = "fall"
                elif sport == "track-and-field-outdoor":
                    season = "spring"
                elif sport == "track-and-field-indoor":
                    season = "winter"
                
                for athlete in athletes:
                    new_row = pd.DataFrame({
                        "name": [athlete],
                        "number": [0],
                        "sport": [sport],
                        "season": [season],
                        "level": ["varsity"],
                        "gender": [gender],
                        "grade": ["N/A"],
                        "position": ["N/A"]
                    })
                    self.athletes = pd.concat([self.athletes, new_row], ignore_index=True)

        return self.athletes
