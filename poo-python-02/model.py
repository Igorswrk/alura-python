class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def add_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Film(Program):
    def __init__(self, name, year, running_time):
        super().__init__(name, year)
        self.running_time = running_time


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Film('avengers - infinity war', 2018, 160)
dark = Series('Dark', 2019, 3)

avengers.add_likes()
avengers.add_likes()
avengers.add_likes()

dark.add_likes()
dark.add_likes()

print(f'Name: {avengers.name} - Likes: {avengers.likes}')

print(f'Name: {dark.name} - Likes: {dark.likes}')

