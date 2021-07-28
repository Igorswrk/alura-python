class Film:
    def __init__(self, name, year, running_time):
        self.__name = name.title()
        self.year = year
        self.running_time = running_time
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


avengers = Film('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - running_time: {avengers.running_time}')

dark = Series('Dark', 2019, 3)
print(f'Name: {dark.name} - Year: {dark.year} '
      f'- Seasons: {dark.seasons}')
