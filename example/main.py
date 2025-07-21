from Athletics.MaxPrepRosterScraper import MaxPrepRosterScraper

MyRosterScraper = MaxPrepRosterScraper("https://www.maxpreps.com/il/chicago/northside-mustangs")
MyRosterScraper.scrape()
print(MyRosterScraper.roster)