import csv
import random
from Resources.Regions import region
from Resources.Characters import character

MAIN_DIRECTORY = "Resources/Taverns/"

MODIFIER_DIRECTORY = MAIN_DIRECTORY + "modifiers.csv"
NOUN_DIRECTORY = MAIN_DIRECTORY + "nouns.csv"

DESC_START_DIRECTORY = MAIN_DIRECTORY + "desc_start.csv"
DESC_ENTER_DIRECTORY = MAIN_DIRECTORY + "enter.csv"
DESC_BARKEEPER_DIRECTORY = MAIN_DIRECTORY + "barkeeper.csv"

HUMAN = "Human"
OBJECT = "Object"


class Tavern:
    def __init__(self, current_region, mood=None, fill=None):
        self.region = current_region
        assert isinstance(current_region, region.Region)

        self.name = get_tavern_name()

        self.owner = None

        self.flavor_text = None
        self.mood = mood
        self.fill = fill

    def get_flavor_text(self):
        start_text, self.mood = get_desc_start(self.mood)
        self.flavor_text = start_text.replace("@", self.name)

        enter_text, self.mood, self.fill = get_desc_enter(self.mood, self.fill)
        self.flavor_text = self.flavor_text + " " + enter_text

        barkeep_text, self.mood, self.fill = get_desc_barkeeper(self.mood, self.fill)

        self.owner = character.Character(self.region, mood=self.mood)

        barkeep_text = barkeep_text.replace("$", self.owner.get_description())
        barkeep_text = barkeep_text.replace("#", self.owner.get_pronoun())
        self.flavor_text = self.flavor_text + " " + barkeep_text

    def display(self):
        print(self.name + "\n\n")

        if not self.flavor_text:
            self.get_flavor_text()

        print(self.flavor_text)


def get_tavern_name():
    method = random.randint(0, 2)

    if method == 1:
        name = _get_modifier_noun()
    else:
        name = _get_owner_noun()

    return name


def get_desc_start(mood=None):
    with open(DESC_START_DIRECTORY) as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        if mood:
            name_list = []
            for row in reader:
                if row[1] == mood:
                    name_list.append(row[0])
            start = random.choice(name_list).strip()
        else:
            selection = random.choice(list(reader))
            start = selection[0]
            mood = selection[1]
        return start.strip(), mood.strip()


def get_desc_enter(mood=None, fill=None):
    with open(DESC_ENTER_DIRECTORY) as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        desc_list = []
        for row in reader:
            if not mood or row[1] == mood:
                desc_list.append(row)
        selection = random.choice(desc_list)
        text = selection[0]
        if not mood:
            mood = selection[1]
        if not fill:
            try:
                fill = selection[2]
            except IndexError:
                fill = None
        return text.strip(), mood, fill


def get_desc_barkeeper(mood=None, fill=None):
    with open(DESC_BARKEEPER_DIRECTORY) as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        desc_list = []
        for row in reader:
            if (not mood or row[1] == mood) and (not fill or row[2] == fill):
                desc_list.append(row)
        selection = random.choice(desc_list)
        text = selection[0]
        if not mood:
            mood = selection[1]
        if not fill:
            try:
                fill = selection[2]
            except IndexError:
                fill = None
        print(mood)
        return text.strip(), mood, fill


def _get_modifier_noun():
    modifier, requirement = _get_modifier()
    noun = _get_noun(requirement=requirement)

    return "The " + modifier + " " + noun


def _get_owner_noun():
    owner = _get_noun(requirement=HUMAN)
    noun = _get_noun(requirement=OBJECT)

    return "The " + owner + "'s " + noun


def _get_modifier():
    with open(MODIFIER_DIRECTORY) as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        selection = random.choice(list(reader))
        modifier = selection[0]
        try:
            requirement = selection[1].strip()
        except IndexError:
            requirement = None

        return modifier, requirement


def _get_noun(requirement=None):
    with open(NOUN_DIRECTORY) as name_file:
        reader = csv.reader(name_file, delimiter=',', quotechar='|')
        name_list = []
        for row in reader:
            if not requirement or row[1] == requirement:
                name_list.append(row[0])
        return random.choice(name_list).strip()

