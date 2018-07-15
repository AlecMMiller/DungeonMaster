from Resources.Regions import region
from Resources.Names import name
import random
import csv

DESC_CHARACTERS = "Resources/Characters/character.csv"


class Character:
    def __init__(self, current_region, race=None, gender=None, mood=None):
        self.region = current_region
        self.assigned_gender = gender
        assert isinstance(current_region, region.Region)

        if not race:
            self.race = self.region.get_race()
        else:
            self.race = race

        self.race = region.race_list[self.race.value]

        self.first_name, self.gender = name.get_first_name(current_region.name_region, self.assigned_gender)
        self.surname = name.get_surname(current_region.get_surname_group())

        self.mood = mood

    def get_full_name(self):
        return self.first_name + " " + self.surname

    def cycle_name(self):
        self.first_name, self.gender = name.get_first_name(self.region.name_region, self.assigned_gender)
        self.surname = name.get_surname(self.region.get_surname_group())

    def get_possessive(self):
        if self.gender == name.MALE:
            return "his"
        else:
            return "her"

    def get_pronoun(self):
        if self.gender == name.MALE:
            return "he"
        else:
            return "she"

    def get_gender(self):
        if self.gender == name.MALE:
            return "man"
        else:
            return "woman"

    def get_description(self):
        with open(DESC_CHARACTERS) as file:
            reader = csv.reader(file, delimiter=';', quotechar='|')
            desc_list = []
            for row in reader:
                if (not self.mood or row[2] == self.mood or not row[2]) and (row[1] == self.get_gender() or not row[1]):
                    desc_list.append(row)
            selection = random.choice(desc_list)
            text = selection[0]
            text = text.replace("$", self.race)
            text = text.replace("#", self.get_gender())
            text = text.replace("*", self.get_possessive())
        return text