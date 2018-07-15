import csv
import random
from enum import Enum

ARCHAIC = 'archaic'
WESTRON = 'westron'
NORTHISH = 'northish'
SOUTHRON = 'southron'


class SurnameGroup(Enum):
    DESERTFOLK = 0
    FARMFOLK = 1
    FOODMAKERS = 2
    FROZENLANDS = 3
    GARMETMAKERS = 4
    ISLANDERS = 5
    MASONS = 6
    MINERS = 7
    MERCHANTS = 8
    ARCANE = 9
    RIVERFOLK = 10
    SEAFOLK = 11
    SMITHS = 12
    SOLDIERS = 13
    STABLEHANDS = 14
    SWAMPFOLK = 15
    TOWNFOLK = 16
    WOODSFOLK = 17


surname_group = ['desertfolk', 'farmfolk', 'foodmakers', 'frozenlands', 'garmetmakers', 'islanders', 'masons', 'miners',
                 'merchants', 'arcane', 'riverfolk', 'seafolk', 'smiths', 'soldiers', 'stablehands', 'swampfolk',
                 'townfolk', 'woodsfolk']

MALE = 'Male'
FEMALE = 'Female'

FIRST_NAME_DIRECTORY = "Resources/Names/First/"
SURNAME_DIRECTORY = "Resources/Names/Last/"


def get_first_name(region, gender=None):
    with open(FIRST_NAME_DIRECTORY + region + '.csv') as name_file:
        reader = csv.reader(name_file, delimiter=',', quotechar='|')
        if gender:
            name_list = []
            for row in reader:
                if row[1] == gender:
                    name_list.append(row[0])
            name = random.choice(name_list).strip()
        else:
            selection = random.choice(list(reader))
            name = selection[0]
            gender = selection[1]
        return name.strip(), gender.strip()


def get_surname(group):
    with open(SURNAME_DIRECTORY + surname_group[group.value] + '.csv') as name_file:
        reader = csv.reader(name_file, delimiter=',', quotechar='|')
        name_list = []
        for row in reader:
            name_list.append(row[0])
        return random.choice(name_list).strip()
