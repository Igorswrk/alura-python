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

    def __str__(self):
        return f'Name: {avengers.name} - {avengers.running_time} min | Likes: {avengers.likes}'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {avengers.name} - {dark.seasons} seasons | Likes: {avengers.likes}'


avengers = Film('avengers - infinity war', 2018, 160)
dark = Series('Dark', 2019, 3)

avengers.add_likes()
avengers.add_likes()
avengers.add_likes()

dark.add_likes()
dark.add_likes()

program_list = [avengers, dark]

for program in program_list:
    print(program)
