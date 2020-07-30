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
    #  'Desc': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Los_Angeles',
    #  'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Mt St Helens', 'Region': 'WA',
     'Desc': '',
     'lat': '46.191353', 'lon': '-122.195606', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 135, 'windDirUpper': 225,  # SE to SW
     'windLower': 0, 'windUpper': 12,
     'link': 'https://goo.gl/maps/nH5HZUzb2SzUJhsw6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': True},
]
