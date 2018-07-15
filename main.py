from Resources.Regions import region
from Resources.Taverns import tavern

current_region = region.Region()
current_region.set_region('Murann')

building = tavern.Tavern(current_region)
building.display()

