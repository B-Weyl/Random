from matplotlib.pyplot import hot
import ebird_keys
from ebird.api import get_species_observations
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


# list of speciesCodes we want to get sightings for
owl_codes = ['grhowl', 'brdowl', 'easowl1', 'loeowl', 'sheowl', 'brnowl', 'nswowl']
# add the sighting to a list as (common Name, Location Name, Observation Date. link to checklist)
owl_locations = []



# loop through each owl code and get the sightings information
for oc in owl_codes:
    nearby = get_species_observations(ebird_keys.api_key, oc, 'US-DE')
    # extract the fields that we want
    for n in nearby:
        if 'howMany' in n:
            count = n['howMany']
        else:
            count = 'X'
            
        owl_locations.append((n['comName'], n['locName'], n['obsDt'], count, 'https://www.ebird.org/checklist/' + n['subId']))  

x = ColorTable(theme=Themes.DEFAULT)
x.field_names = ['species', 'location', 'date', 'count', 'checklist']

# display the information in an easy to read format
for ol in owl_locations:
    x.add_row([ol[0], ol[1], ol[2], ol[3], ol[4]])
    # print("{} seen/heard at {} on {} {}".format(ol[0], ol[1], ol[2], ol[3]))
print(x)








