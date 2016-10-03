#!/usr/bin/python
# originially run with python 2.6.6
# Using the API from https://developers.wargaming.net/reference/
# Acquired the original data set like this:
#   curl 'https://api.worldoftanks.com/wot/encyclopedia/vehicles/?application_id=demo' | python -m json.tool > wot_api_vehicles.json
#   curl 'https://api.worldoftanks.com/wot/encyclopedia/info/?application_id=demo' | python -m json.tool > wot_api_info.json
#   curl 'https://api.worldoftanks.com/wot/encyclopedia/arenas/?application_id=demo' | python -m json.tool > wot_api_arenas.json
#   curl 'https://api.worldoftanks.com/wot/encyclopedia/provisions/?application_id=demo' | python -m json.tool > wot_api_provisions.json
#   curl 'https://api.worldoftanks.com/wot/encyclopedia/modules/?application_id=demo&nation=france&type=vehicleRadio' | python -m json.tool > wot_api_modules-france-vehicleRadio.json
#     Where the module type can be:
module_types = ['vehicleRadio', 'vehicleEngine', 'vehicleGun', 'vehicleChassis', 'vehicleTurret']
#     And the nations can be:
nations = ['france', 'germany', 'uk', 'usa', 'ussr', 'china', 'japan', 'czech']

import os, sys, shlex, json, re
from pprint import pprint

with open('wot_api_vehicles.json') as json_file:
    json = json.load(json_file)

print( type(json) )
print( json.keys() )
wot_veh_dat = json.get('data')
print( wot_veh_dat.keys() )
wot_veh_dat_6721 = wot_veh_dat.get('6721')
print( wot_veh_dat_6721.keys() )
print( wot_veh_dat_6721['guns'] )
pprint( wot_veh_dat_6721 )




