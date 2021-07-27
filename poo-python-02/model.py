class Film:
    def __init__(self, name, year, running_time):
        self.name = name
        self.year = year
        self.running_time = running_time


class Series:
    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons


avengers = Film('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - running_time: {avengers.running_time}')

dark = Series('Dark', 2019, 3)
print(f'Name: {dark.name} - Year: {dark.year} '
      f'- Seasons: {dark.seasons}')
