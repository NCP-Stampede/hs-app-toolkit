import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

class AthleticsSchedule:
    def __init__(self):
        self.schedule = pd.DataFrame(columns=["date", "time", "gender", "sport", "level", "opponent", "location", "home"])
    
    def scrape(self):
        url = "https://www.northsideprepathletics.com/schedule?year=2025-2026"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        time.sleep(5)
        
        print("Page loaded, starting to scroll...")
        
        previous_event_count = 0
        no_new_content_count = 0
        max_scroll_attempts = 20
        scroll_attempt = 0
        
        while scroll_attempt < max_scroll_attempts:
            current_events = driver.find_elements("css selector", "h2.mb-1.font-heading.text-xl")
            current_event_count = len(current_events)
            
            print(f"Scroll attempt {scroll_attempt + 1}: Found {current_event_count} events")
            
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            
            new_events = driver.find_elements("css selector", "h2.mb-1.font-heading.text-xl")
            new_event_count = len(new_events)
            
            if new_event_count == current_event_count:
                no_new_content_count += 1
                print(f"No new content loaded (attempt {no_new_content_count})")
                
                if no_new_content_count >= 3:
                    print("No new content for 3 attempts, assuming all content loaded")
                    break
            else:
                no_new_content_count = 0
                print(f"New content loaded: {new_event_count - current_event_count} new events")
            
            previous_event_count = new_event_count
            scroll_attempt += 1
        
        print(f"Finished scrolling after {scroll_attempt} attempts. Final event count: {len(driver.find_elements('css selector', 'h2.mb-1.font-heading.text-xl'))}")
        
        time.sleep(5)
        html_content = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html_content, 'html.parser')

        repeated_dates = soup.find_all('h3', class_='uppercase')
        exact_dates = [h3 for h3 in repeated_dates if h3.get('class') == ['uppercase']]
        dates = [h3.get_text(strip=True) for h3 in exact_dates]

        times = soup.select('p.text-base.font-bold[data-testid*="time"]')
        times = [p.get_text(strip=True) for p in times]

        sports = soup.select("p.text-base.font-bold[data-testid*='activity-name']")
        sports = [p.get_text(strip=True) for p in sports]

        locations = soup.select("p.text-sm.font-medium[data-testid*='venue']")
        locations = [p.get_text(strip=True) for p in locations]

        levels = soup.select("div.text-sm.font-medium.text-core-contrast.text-opacity-80.xl\\:text-base[data-testid*='gender-level']")
        levels = [p.get_text(strip=True).split()[1].lower() for p in levels]

        genders = soup.select("div.text-sm.font-medium.text-core-contrast.text-opacity-80.xl\\:text-base[data-testid*='gender-level']")
        genders = [p.get_text(strip=True).split()[0].lower() for p in genders] 

        opponents = soup.select('h2.mb-1.font-heading.text-xl')
        opponents = [h2.get_text(strip=True).replace("vs ", "").replace("at ", "") for h2 in opponents]

        home = soup.select("div.inline-flex.items-center.gap-1")
        home = [div.get_text(strip=True) for div in home]
        home = [item.lower() == "home" for item in home]
        
        length = len(dates)
        for i in range(length):
            new_row = pd.DataFrame({
                'date': [dates[i]],
                'time': [times[i]],
                'gender': [genders[i]],
                'sport': [sports[i]],
                'level': [levels[i]],
                'opponent': [opponents[i]],
                'location': [locations[i]],
                'home': [home[i]]
            })
            self.schedule = pd.concat([self.schedule, new_row], ignore_index=True)
        
        return self.schedule