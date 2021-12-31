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

# WA Sites
WA_sites = [
    # {'Name': '', 'Region': '',
    #  'Info': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Los_Angeles',
    #  'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Bingen', 'Region': 'Columbia River Gorge',
     'Info': '',
     'lat': '45.7255', 'lon': '-121.446', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 225, 'windDirUpper': 315,  # SW to NW per Kyle
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/zS1Fmr4DzzW54M8fA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},  # TODO: Fix wind data

    {'Name': 'Cliffside', 'Region': 'Columbia River Gorge',
     'Info': '',
     'lat': '45.724844', 'lon': '-120.726470', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 45, 'windDirUpper': 135,
     'windLower': 7, 'windUpper': 15,
     'link': 'https://goo.gl/maps/zgzczeHDBNyuRFhP7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},  # TODO: Fix wind data

    {'Name': 'Mt St Helens', 'Region': 'WA',
     'Info': '',
     'lat': '46.191353', 'lon': '-122.195606', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 135, 'windDirUpper': 225,  # SE to SW
     'windLower': 0, 'windUpper': 12,
     'link': 'https://goo.gl/maps/nH5HZUzb2SzUJhsw6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True},

    {'Name': 'Fort Flagler-Harmon', 'Region': '',
     'Info': 'takeoff	Cliff launch with deep rotor boundary. Landing: Campground at the west end of bluff, beach '
             '(do not walk back up the bluff), or top landing (requires much skill)'
             'Weather: Wind is too strong when white caps start to appear on water. Spring and late fall are best.'
             'Tends to get thermal blocked in summer. Rules: P3 with cliff launch experience recommended. '
             'Access: - Comments: Beautifully place to fly but, one of the more difficult places to launch from. '
             'Contact: Rainier Paragliding Club Web: http://www.rainierparaglidingclub.org/',
     'lat': '48.102900', 'lon': '-122.697000', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 315, 'windDirUpper': 45,  # NW to NE
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/PsPf9xHZgUsB6e4e8',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

]
