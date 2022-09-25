from project_exam.horse_race import HorseRace
from project_exam.horse_specification.appaloosa import Appaloosa
from project_exam.horse_specification.thoroughbred import Thoroughbred
from project_exam.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        valid_types = ["Appaloosa", "Thoroughbred"]
        if horse_type not in valid_types:
            return
        if self.find_by_name(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        horse = self.horse_maker(horse_type, horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        if self.find_by_name(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = self.jockey_maker(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        created_races = []
        race = self.race_maker(race_type)
        if race.race_type in created_races:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(race)
        created_races.append(race.race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        if not self.find_by_name(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = self.find_jockeys(jockey_name, self.jockeys)
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        horse = self.find_horses(horse_type, self.horses)
        if horse.is_taken or horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        horse_race = self.find_races(race_type, self.horse_races)
        if horse_race not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if not self.find_by_name(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = self.find_jockeys(jockey_name, self.jockeys)
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in self.horse_races:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        self.horse_races.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        pom = 0
        best_speed = 0
        horse_race = self.find_races(race_type, self.horse_races)
        if horse_race not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        for jockey in self.jockeys:
            if jockey.horse.speed > pom:
                pom = jockey.horse.speed
                best_speed = pom
        return f"The winner of the {race_type} race, with a speed of {best_speed}km/h is {jockey.name}! Winner's horse: {jockey.horse.name}. "

    @staticmethod
    def horse_maker(type, name, speed):
        if type == "Appaloosa":
            horse = Appaloosa(name, speed)
        else:
            horse = Thoroughbred(name, speed)
        return horse

    @staticmethod
    def find_by_name(name, collection):
        for given_name in collection:
            if given_name.name == name:
                return True
        return False

    @staticmethod
    def jockey_maker(name, age):
        jockey = Jockey(name, age)
        return jockey

    @staticmethod
    def race_maker(type):
        return HorseRace(type)

    @staticmethod
    def find_jockeys(name, collection):
        for jockey in collection:
            if jockey.name == name:
                return jockey

    @staticmethod
    def find_horses(type, collection):
        for index in range(len(collection) - 1, -1, -1):
            horse = collection[index]
            if horse.__class__.__name__ == type:
                return horse

    @staticmethod
    def find_races(type, collection):
        for race in collection:
            if race.race_type == type:
                return race
