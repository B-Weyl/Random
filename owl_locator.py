from matplotlib.pyplot import hot
import ebird_keys
from ebird.api import get_species_observations

# list of speciesCodes we want to get sightings for
owl_codes = ['grhowl', 'brdowl', 'easowl1', 'loeowl', 'sheowl', 'brnowl', 'nswowl']
# add the sighting to a list as (common Name, Location Name, Observation Date)
owl_locations = []

# loop through each owl code and get the sightings information
for oc in owl_codes:
    nearby = get_species_observations(ebird_keys.api_key, oc, 'US-DE')
    # extract the fields that we want
    for n in nearby:
        owl_locations.append((n['comName'], n['locName'], n['obsDt']))

# display the information in an easy to read format
for ol in owl_locations:
    print("{} seen/heard at {} on {}".format(ol[0], ol[1], ol[2]))




