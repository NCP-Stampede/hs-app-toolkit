import pandas as pd
import requests
from bs4 import BeautifulSoup

class GeneralEvent:
    def __init__(self, months=range(1,13), years=range(2025,2027)):
        self.months = months
        self.years = years
        self.events = pd.DataFrame(columns=["date", "time", "name", "createdBy"])

    def scrape(self):
        for month_num in self.months:
            for year_num in self.years:
                url = f"https://www.northsideprep.org/apps/events/view_calendar.jsp?id=0&m={month_num-1}&y={year_num}"
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                continue

            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')
            event_cells = soup.find_all('div', class_='day prev') + soup.find_all('div', class_='day prev weekend')

            for cell in event_cells:
                event_name = cell.find("a", class_="eventInfoAnchor")
                if event_name:
                    event_name = event_name.text.strip()
                    event_date = cell.find("span", class_="dayLabel").text.strip()
                    event_date = f"{month_num}/{event_date}/{year_num}"
                    event_time = cell.find("span", class_="edEventDate").text.strip() if cell.find("span", class_="edEventDate") else "All Day"

                    new_row = pd.DataFrame({
                        "date": [event_date],
                        "time": [event_time],
                        "name": [event_name],
                        "createdBy": ["Northside College Prep Calendar"]
                    })
                    self.events = pd.concat([self.events, new_row], ignore_index=True)
        return self.events