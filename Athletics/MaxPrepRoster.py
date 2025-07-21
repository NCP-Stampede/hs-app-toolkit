from bs4 import BeautifulSoup
import requests
import pandas as pd

class MaxPrepRoster:
    """
    Scraper for Max Preps roster data. This class fetches and parses roster information.
    It only supports sports that have a roster page available on the Max Preps website.
    Need to pass the full `url` of the TEAM PAGE to the constructor.
    You can access the roster data using the `roster` attribute after calling the `scrape()` method.

    Attributes:
        url (str): The base URL for the Max Preps roster. Example: https://www.maxpreps.com/il/chicago/northside-mustangs
        roster (pd.DataFrame): DataFrame to store the scraped roster information with columns:
            - name: Name of the athlete
            - number: Jersey number of the athlete
            - sport: Sport played by the athlete
            - season: Season of the sport (fall, winter, spring)
            - level: Level of play (varsity, jv, freshman)
            - gender: Gender of the athlete (boys, girls)
            - grade: Grade of the athlete (9, 10, 11, 12)
            - position: Position played by the athlete
    """

    # Initialization method for the MaxPrepRosterScraper class.
    # It sets the URL for the Max Preps roster and initializes an empty DataFrame for
    def __init__(self, url):
        """
        Initializes the MaxPrepRosterScraper with the provided URL.
        :param url: The base URL for the Max Preps roster page (String, e.g., https://www.maxpreps.com/il/chicago/northside-mustangs, REQUIRED).
        """
        self.url = url
        self.roster = pd.DataFrame(columns=["name", "number", "sport", "season", "level", "gender", "grade", "position"])

    # Method to scrape the roster data from the Max Preps website.
    # It fetches the HTML content, parses it, and extracts the roster information.
    def scrape(self, sports=None, genders=None, seasons=None, levels=None) -> pd.DataFrame:
        """
        Scrapes the roster data from the Max Preps website.
        This method fetches the HTML content of the roster page, parses it to find sports,
        and extracts the relevant roster information.
        If an error occurs during the request for sports, it prints an error message and returns.
        It populates the `roster` DataFrame with the relevant information.

        Parameters:
            sports (list): Optional parameter to specify sports to scrape. If None, it scrapes all available sports.
            genders (list): Optional parameter to specify genders to scrape. If None, it scrapes all available genders.
            seasons (list): Optional parameter to specify seasons to scrape. If None, it scrapes all available seasons.
            levels (list): Optional parameter to specify levels to scrape. If None, it scrapes all available levels.

        Returns:
            self.roster (pd.DataFrame): A DataFrame containing the scraped roster information with columns:
        """
        # Tries to fetch the HTML content from the provided URL.
        try:
            response = requests.get(self.url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
        except Exception as e:
            print(f"Error parsing HTML content: {e}")
            return
        
        # Finds all sports listed on the page and extracts their names.
        if sports is None:
            sports = soup.find_all('span', class_="sport-name")
            sports = [sport.get_text(strip=True).replace("& ", "").replace(" ", "-").lower() for sport in sports]
            sports = list(set(sports))

        # Defines the possible combinations of sports
        if genders is None:
            genders = ["girls", "boys"]
        if seasons is None:
            seasons = ["fall", "winter", "spring"]
        if levels is None:
            levels = ["varsity", "jv", "freshman"]

        # Iterates through each combination
        for sport in sports:
            for gender in genders:
                for season in seasons:
                    for level in levels:
                        # Handles the case where the URL might end with a slash
                        if self.url[-1] == "/":
                            self.url = self.url[:-1]

                        # Constructs the URL for the roster page based on the sport, gender, level, and season
                        url = f"{self.url}/{sport}/{gender}/{level}/{season}/roster/"
                        
                        # Fetches the HTML content of the roster page
                        # If an error occurs during the request, it continues to the next iteration
                        try:
                            response = requests.get(url, timeout=(10, 30))
                            response.raise_for_status()
                        except requests.RequestException as e:
                            continue

                        html_content = response.text
                        soup = BeautifulSoup(html_content, 'html.parser')

                        # Finds all player names on the specific iterated roster page
                        players = soup.find_all('a', class_="sc-51f90f89-0 hcqeYd name")
                        players = [player.get_text(strip=True) for player in players]
                        
                        if players:
                            # Extracts the row for each player
                            primary_tds = soup.find_all("td", class_="primary")
                            grades = []
                            positions = []
                            numbers = []

                            # Iterates through each player's row to extract their grade, position, and number
                            for td in primary_tds:
                                grade_td = td.find_next_sibling("td")
                                
                                if grade_td:
                                    grades.append(grade_td.get_text(strip=True))
                                    position_td = grade_td.find_next_sibling("td")
                                    
                                    if position_td:
                                        positions.append(position_td.get_text(strip=True))
                                    
                                    else:
                                        positions.append("N/A")
                                    
                                    number_td = td.find_previous_sibling("td")
                                    
                                    if number_td:
                                        number = number_td.get_text(strip=True)
                                        numbers.append(int(number) if number.isdigit() else 0)
                                    
                                    else:
                                        numbers.append(0)

                            # Appends each player's information to the roster DataFrame
                            for player in players:
                                athlete = {
                                    "name": player,
                                    "number": numbers[players.index(player)],
                                    "sport": sport,
                                    "season": season,
                                    "level": level,
                                    "gender": gender,
                                    "grade": grades[players.index(player)],
                                    "position": positions[players.index(player)]
                                }
                                self.roster = pd.concat([self.roster, pd.DataFrame([athlete])], ignore_index=True)

        # Returns the roster DataFrame containing all the scraped information
        return self.roster