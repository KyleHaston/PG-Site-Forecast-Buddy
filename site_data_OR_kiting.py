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

# OR Kiting Sites
OR_kiting_sites = [
    {'Name': 'Madrona',
     'Desc': 'A grassy bowl in North Portland overlooking the Lower Willamette industrial area. John B has flown ' +
             'this site in the past, but others who have tried to kite have found the winds cross or gusty, ' +
             'which makes sense because it’s on the edge of a narrow river valley downwind from 1000’ hills…\n' +
             'Works Best When: SW (?), strength (?)n' +
             'Hazards: Becoming airborne with nowhere to land but warehouses, train tracks, power lines, street.n' +
             'Getting there: It’s right on the #35 bus line.' +
             'Address: 3100 N Willamette Blvd, Portland, OR 97217',
     'lat': '45.564995', 'lon': '-122.698436', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 225, 'windDirUpper': 270,  # "SW?" on site guide. Using SW to W based on overhead view of park
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/hiwsdrXuD79p6k6BA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Harbor View Park',
     'Desc': 'A large flat open field adjacent to the Lower Willamette River below the University of Portland. This ' +
             'is a cleaned-up Superfund site owned by the University and they are planning to develop sports fields ' +
             'in the next couple years (2012).\n Works Best When: S – W (?), strength (?) ' +
             'Hazards: Access may be difficult; roads are most likely gated at the top of the bluff – respect gates, ' +
             'fences, and construction areas.\nAddress: 5828 N Van Houten Ave., Portland, OR 97203' +
             'Getting there: Take the #35 bus or park above, and walk down.',
     'lat': '45.576937', 'lon': '-122.737738', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 180, 'windDirUpper': 270,  # S to W
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/YEfN9a5GWHDMczhr7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Stuart Caruk\'s Hay Field in Vancouver',
     'Desc': 'Description: A hay field by the weigh scales in Vancouver Washington, about 15 miles north of the ' +
             'Columbia River bridge on I-5. The winds are consistent and there is a porta-john just on the other side' +
             'of the fence at the weigh scales.' +
             'Works Best When: Any direction.\n' +
             'Hazards: Getting dragged, stray golf balls (Stu has given his permission to let golfers know they are ' +
             'trespassing if they come on his property to retrieve their balls, especially if they complain that you ' +
             'are causing a distraction or hit his building!). Of course don’t use the field if there is hay ' +
             'growing: contact Stu at 360-887-1930 first if you have any doubt.\n' +
             'Address: 1799 NW 289th St. Ridgefield, WA 98642\n' +
             'Getting there: From I-5 about 15 miles north of the Columbia River take exit 14 and wiggle your way ' +
             'North to the SE corner of the Tri Mountain Golf course, and turn left. Park on the turnaround and hike ' +
             'across the ditch with your gear.',
     'lat': '45.830265', 'lon': '-122.691838', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 360,  # 'Works Best When: Any direction.'
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    # {'Name': 'G\'s Paramotor Spot (Permission problems here, do not use for now.)',
    #  'Desc': 'Description: An empty industrial lot near the confluence of the Willamette and Columbia rivers. ' +
    #          'Used for paramotoring and excellent for kiting: “Especially good if you actually want to improve ' +
    #          'since it’s not a nice low cut flat grass park.  It’s a sandy soft lumpy area about super huge size ' +
    #          'and has killer manicured grass fold up areas only big enough for two or three wings, but located at ' +
    #          'three corners of the area. Works in any wind direction and usually isn’t blown out although can be ' +
    #          'strong in the afternoons. Partially affected by the weather system "Columbia," but it is one full ' +
    #          'mile from the river.  It’s a strangely serene place among monoliths of industry\n' +
    #          'Works Best When: Any direction.\n' +
    #          'Hazards: Lombard Street\n' +
    #          'Address: 14510 N Lombard St., Portland, OR 97203\n' +
    #          'Getting there: Drive out past St. Johns toward Smith and Bybee lakes and Kelley Point Park, on either' +
    #          'Marine Drive or Lombard Street.',
    #  'lat': '45.6331888889', 'lon': '-122.767152778', 'timezone_str': 'America/Los_Angeles',
    #  'windDirLower': 0, 'windDirUpper': 360,  # Works Best When: Any direction.
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Kelley Point Park',
     'Desc': 'Description: A Portland Parks and Rec park at the confluence of the Willamette and Columbia Rivers ' +
             'that is mostly wooded but has some open grassy areas and gentle hills that could work well in the  ' +
             'right wind directions, and it has beach access along the rivers.\n ' +
             'Works Best When: N-NW (?)\n' +
             'Hazards: Trees, picnickers, water.\n' +
             'Address: N Kelly Point Park Rd, Portland, Oregon 9720\n' +
             'Getting there: Follow N Marine Dr. to the end of the island. Park in the lot and hike out through ' +
             'the park.',
     'lat': '45.649331', 'lon': '-122.764136', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 45,  # Works Best When: N-NW.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Dickinson Park / Crestwood',
     'Desc': 'Description: (Thanks Sarge.) Dickinson City Park is near the Tigard Fred Meyer off SW 55th. ' +
             'A little playground on the E side has a really nice built-up plateau that gives a good spot to ' +
             'kite &/or launch your wing.  The place is approximately 8-10 acres of sloping open area that faces ' +
             'W-SW and it\'s possible to get short hops when the wind is right. With the playground you should be ' +
             'able to take the kids along and let them play while you play too. -fun! The city keeps the grass ' +
             'mowed pretty well, so there\'s no bushes, etc. to get in the way.  This place is a sparsely used site, ' +
             'so you won\'t have issues like you can run into when you want to do some kiting at some of the local ' +
             'high school playgrounds\n' +
             'Works Best When: SW-W Don’t go if the wind is S, NW, N, or any kind of E.\n' +
             'Hazards: Dickinson Park is also a dog-walk area, ... watch your footing!\n' +
             'Address: 10500 SW 55th Ave., Portland OR 97219\n',
     'lat': '45.333', 'lon': '-122.940', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 225, 'windDirUpper': 270,
     'windLower': 7, 'windUpper': 12,
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Franklin High School',
     'Desc': 'Description: A high school in SE Portland at Division and 52nd with a large north-facing field.\n' +
             'Works Best When: NE-NW\n' +
             'Hazards: Glider-grabbin’ trees at the top of the hill.\n' +
             'Address: 5405 SE Woodward, Portland, OR 97206\n' +
             'Getting there: Access from the parking lot in the NE corner of the school, or at the end of ' +
             'SE Clinton St.',
     'lat': '45.503631', 'lon': '-122.605049', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 315, 'windDirUpper': 45,  # NE-NW # TODO: This won't work for wind direciton. Change dir check so it does.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'West Delta Park/Portland International Raceway',
     'Desc': 'Description: A large open grassy field between a wetland and the Portland International Raceway.' +
             'This is an off leash dog park so inspect before you kite.\n' +
             'Works Best When: Should work in any direction.\n' +
             'Hazards: Dogs\n' +
             'Address: 1809 N Broadacre Rd., Portland OR 97217\n' +
             'Getting there: Follow directions to Portland International Raceway, which is off I-5 at Exit 306-B.',
     'lat': '45.598443', 'lon': '-122.686866', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 360,  # "Wind should work form any direction."
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Spring Garden Park',
     'Desc': 'Description: A north-facing city park in SW Portland with a slight drop between Dolph Ct. and ' +
             'Spring Garden St.\n' +
             'Works Best When: N\n' +
             'Hazards: Dog waste.\n' +
             'Address: 3332 SW Spring Garden St, Portland, OR 97219\n' +
             'Getting there: It’s just north of the intersection of SW Barbur Blvd and 30th Ave.',
     'lat': '45.462447', 'lon': '-122.710863', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 45,  # N # TODO: This won't work for wind direciton. Change dir check so it does.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Hosford Middle School',
     'Desc': 'Description: A west-facing school field near SE Sherman and 27th with a slight hill facing SW and NW, ' +
             'plenty of room to walk about with a wing, no obstructions.\n' +
             'Works Best When: SW to NW 5 to 8 mph\n' +
             'Hazards: Dog waste. Crowded with kids during school hours.\n',
     'lat': '45.506005', 'lon': '-122.638162', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 225, 'windDirUpper': 315,  # SW to NW
     'windLower': 5, 'windUpper': 8,  # 5 to 8 mph
     'link': '',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
]
