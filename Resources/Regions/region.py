import csv
from enum import Enum
import random
from Resources.Names import name

REGION_DIRECTORY = "Resources/Regions/breakdown.csv"

race_list = ['human', 'halfling', 'dwarf', 'elf', 'gnome', 'half-orc', 'half-elf']


class Races(Enum):
    HUMAN = 0
    HALFLING = 1
    DWARF = 2
    ELF = 3
    GNOME = 4
    HALF_ORC = 5
    HALF_ELF = 6


class Region:
    def __init__(self):
        self.race_breakdown = None
        self.surname_breakdown = None
        self.name_region = None

    def set_region(self, region):
        region = region.title()
        region_data = None

        with open(REGION_DIRECTORY) as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for row in reader:
                if row[0] == region:
                    region_data = row

        if region_data:
            self.race_breakdown = list(map(int, region_data[21:30]))
            self.surname_breakdown = list(map(int, region_data[3:21]))
            self.name_region = region_data[2].lower()
        else:
            print("No region " + region)

    def get_race(self):
        race_total = sum(self.race_breakdown)

        selection = random.randint(1, race_total+1)
        got_race = Races.HUMAN

        for race, population in enumerate(self.race_breakdown):
            if population >= selection:
                got_race = Races(race)
                break
            else:
                selection -= population

        return got_race

    def get_surname_group(self):
        surname_total = sum(self.surname_breakdown)

        selection = random.randint(0, surname_total)
        for group, population in enumerate(self.surname_breakdown):
            if population >= selection:
                return name.SurnameGroup(group)
            else:
                selection -= population

        return 0

