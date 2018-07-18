from xml.dom import minidom
from operator import itemgetter
import os

PLAYER_DIRECTORY = "Resources/Players"


class Player:
    def __init__(self, file):
        sep = "."
        self.name = file.split(sep, 1)[0]

        doc = minidom.parse(PLAYER_DIRECTORY + "/" + file)
        abilities_group = doc.getElementsByTagName("abilities")[0]
        ability_groups = abilities_group.getElementsByTagName("ability")
        for ability_group in ability_groups:
            name_group = ability_group.getElementsByTagName("short")[0]
            name = name_group.firstChild.nodeValue

            modifier_group = ability_group.getElementsByTagName("modifier")[0]
            modifier = modifier_group.firstChild.nodeValue

            if name == "WIS":
                self.wisdom = int(modifier)

        skills_group = doc.getElementsByTagName("skills")[0]
        skill_groups = skills_group.getElementsByTagName("skill")
        for skill_group in skill_groups:
            name_group = skill_group.getElementsByTagName("name")[0]
            name = name_group.firstChild.nodeValue

            skill_mod_group = skill_group.getElementsByTagName("skill_mod")[0]
            skill_mod = skill_mod_group.firstChild.nodeValue

            if name == "Listen":
                self.listen = int(skill_mod)
            elif name == "Spot":
                self.spot = int(skill_mod)
            elif name == "Sense Motive":
                self.sense_motive = int(skill_mod)


class Players:
    def __init__(self):
        self.player_list = []
        for file in os.listdir(PLAYER_DIRECTORY):
            if file.endswith(".xml"):
                self.player_list.append(Player(file))

    def print_formatted(self, character, value):
        print(character + ": " + str(value))

    def get_sense_motive(self):
        super_list = []
        for player in self.player_list:
            sub_list = []
            sub_list.append(player.name)
            sub_list.append(player.sense_motive)
            super_list.append(sub_list)

        super_list = sorted(super_list, key=itemgetter(1), reverse=True)

        for character in super_list:
            self.print_formatted(character[0], character[1])

    def get_spot(self):
        super_list = []
        for player in self.player_list:
            sub_list = []
            sub_list.append(player.name)
            sub_list.append(player.spot)
            super_list.append(sub_list)

        super_list = sorted(super_list, key=itemgetter(1), reverse=True)

        for character in super_list:
            self.print_formatted(character[0], character[1])


    def get_listen(self):
        super_list = []
        for player in self.player_list:
            sub_list = []
            sub_list.append(player.name)
            sub_list.append(player.listen)
            super_list.append(sub_list)

        super_list = sorted(super_list, key=itemgetter(1), reverse=True)

        for character in super_list:
            self.print_formatted(character[0], character[1])
