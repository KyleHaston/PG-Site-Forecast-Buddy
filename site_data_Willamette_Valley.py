# Compass Points -------------------------------------------------------------------------------------------------------
# Abbreviation	Middle azimuth
# N	      0.000°
# NNE	 22.500°
# NE	 45.000°
# ENE	 67.500°
# E	     90.000°
# ESE	112.500°
# SE	135.000°
# SSE	157.500°
# S	    180.000°
# SSW	202.500°
# SW	225.000°
# WSW	247.500°
# W	    270.000°
# WNW	292.500°
# NW	315.000°
# NNW	337.500°
# N	    360.000°

# Willamette Valley
#     Chehalem
#     Gales Creek (Closed)
#     Gobblers (Closed)
#     Peterson Butte

OR_Willamette_Valley_sites = [
    # {'Name': 'Madrona',
    #  'Desc': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Los_Angeles',
    #  'windDirLower': 0, 'windDirUpper': 360,
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Chehalem',
     'Desc': 'Chehalem is a south-facing ridge. Salem winds south at 6-8 mph often mean soaring conditions here. ' +
             'Less than that and it\'s a sled ride, more than that and it\'s blown out. Often these winds will keep  ' +
             'you at launch level but to get above launch, you will need to find thermals. Paragliders must be +'
             'extremely careful when the wind is strong, as there are trees on both sides of launch and power lines  ' +
             'behind launch. The wind usually is stronger 20 feet above your wind meter. Many days here are hang  ' +
             'gliding only days, due to wind strength. Soaring flights of over an hour have been recorded here, and  ' +
             'they seem to happen most frequently in prefrontal and post frontal conditions.\n ' +
             'We have better flying sites. This site\'s main virtue is being close to town so that if you\'re  ' +
             'skunked, you feel only half as bad. The main disadvantages of flying here are: 1) the ridge is  ' +
             'shallow, so you need a lot of wind to soar, which doesn\'t leave much margin of safety if the wind  ' +
             'picks up; 2) the main LZ is a long glide out from launch and there are times when a paraglider will  ' +
             'not be able to glide all the way there forcing a landing at the smaller, sloping  alternate LZ; and  ' +
             '3) there are power lines to cross on the way to both the main and alternate LZs and paragliders  ' +
             'often have to cross them low. That said, there are days that pilots can get to 5000’ and go XC.' +
             'LZ: 45.3368, -122.9961    Bailout: 45.3471, -123.0021',
     'lat': '45.355200', 'lon': '-122.997500', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 180, 'windDirUpper': 270,  # I'm picking from S to W. TODO: Get real wind dirs.
     'windLower': 5, 'windUpper': 10,  # from site guide description
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Peterson Butte',
     'Desc': 'SITE IS OPEN FROM 11/1 THROUGH 5/31. Other times closed for fire hazard. There is a keypad at the ' +
             'gate now. You need the combo to access. Be off the property before sunset. Susan Wheeler is the ' +
             'current manager of the family’s land. Mark Wahl is the livestock manager, 541-905-6064.  Call ' +
             'him if see dead or distressed sheep.  There are hundreds of sheep on the property so drive slow.' +
             'Site Protocol: USHPA MEMBERSHIP REQUIRED, no flying alone, rated pilots only, no group training, ' +
             'leave gates as found (closed), no driving off of paved road except to park at microwave station, no ' +
             'firearms or hunting, no dogs allowed, no fires, no motorcycles, drive slowly and be courteous to the ' +
             'animals (that may be standing in the middle of the road).',
     'lat': '44.510043', 'lon': '-122.968919', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 180, 'windDirUpper': 270,  # I'm picking from S to W. TODO: Get real wind dirs.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

]
