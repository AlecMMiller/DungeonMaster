from Resources.Regions import region
from Resources.Names import name
from Resources.Taverns import tavern
from Resources.Characters import character

SPLASH_TEXT = "______                                   ___  ___          _            \n" \
              "|  _  \                                  |  \/  |         | |\n" \
              "| | | |_   _ _ __   __ _  ___  ___  _ __ | .  . | __ _ ___| |_ ___ _ __ \n" \
              "| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \| |\/| |/ _` / __| __/ _ \ '__|\n" \
              "| |/ /| |_| | | | | (_| |  __/ (_) | | | | |  | | (_| \__ \ ||  __/ |  \n" \
              "|___/  \__,_|_| |_|\__, |\___|\___/|_| |_\_|  |_/\__,_|___/\__\___|_|   \n" \
              "                    __/ |                                               \n" \
              "                   |___/                            Technomancery \n\n"


class Browser:
    def __init__(self):
        print(SPLASH_TEXT)
        self.region = region.Region()
        self.last_command = None
        self.current_building = None
        self.current_character = None

    def run(self):
        packet = input("> ").split()

        try:
            command = packet[0]
            self.last_command = packet
        except IndexError:
            packet = self.last_command
            command = packet[0]

        if command == "region":
            try:
                self.region.set_region(packet[1])
            except IndexError:
                print("Region command requires region argument")

        elif command == "name":
            try:
                gender = packet[1].title()
                if gender != name.FEMALE and gender != name.MALE:
                    print(gender + " not recognised")
                    gender = None
            except IndexError:
                gender = None
            try:
                first, gender = name.get_first_name(self.region.name_region, gender=gender)
                surname = name.get_surname(self.region.get_surname_group())
                print(first + " " + surname)
            except TypeError:
                print("No region set")

        elif command == "tavern":
            try:
                self.current_building = tavern.Tavern(self.region)
                self.current_building.display()
            except TypeError:
                print("No region set")

        elif command == "char":
            self.current_character = character.Character(self.region)

            description = self.current_character.get_description()
            print(description)



