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
        return f'Name: {self.name} - {self.running_time} min | Likes: {self.likes}'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - {self.seasons} seasons | Likes: {self.likes}'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def listing(self):
        return self._programs

    @property
    def size(self):
        return len(self._programs)


avengers = Film('avengers - infinity war', 2018, 160)
dark = Series('Dark', 2019, 3)
punisher = Series('Punisher', 2017, 2)
ironman = Film('Ironman 3', 2013, 180)

avengers.add_likes()
avengers.add_likes()
avengers.add_likes()

punisher.add_likes()
punisher.add_likes()
punisher.add_likes()
punisher.add_likes()

ironman.add_likes()
ironman.add_likes()

dark.add_likes()

program_list = [avengers, dark, punisher, ironman]
my_playlist = Playlist('Maratona', program_list)

for program in my_playlist.listing:
    print(program)

print(f'Tamnho Playlist: {my_playlist.size}')
