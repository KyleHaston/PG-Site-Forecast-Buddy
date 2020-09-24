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
OR_test_sites = [
    # {'Name': '', 'Region': '',
    #  'Info': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Los_Angeles',
    #  'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Hagg Lake Section D Kiting Site?', 'Region': 'Portland, OR',
     'Info': '',
     'lat': '45.557533', 'lon': '-123.163262', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 170, 'windDirUpper': 190,  # Looks like S wind would be good. TODO: Get real wind dirs
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/99EhKfsW8RnPVLb26',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Hagg Lake Section C Kiting Site?', 'Region': 'Portland, OR',
     'Info': '',
     'lat': '45.491223', 'lon': '-123.214454', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 135, 'windDirUpper': 315,  # Looks like SE to NW wind would be good. TODO: Get real wind dirs
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/cyow81VTEg2Grq8c9',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Scoggins Creek Hill Kiting Site?', 'Region': 'Portland, OR',
     'Info': '',
     'lat': '45.455049', 'lon': '-123.177427', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 45, 'windDirUpper': 112,  # Looks like ESE to NE wind would be good. TODO: Get real wind dirs
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/ek7UAKWPFsvj5o7B6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Summit Ave Hilltop Kiting Site?', 'Region': 'Portland, OR',
     'Info': '',
     'lat': '45.467514', 'lon': '-123.266701', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
     'windLower': 4, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/XvR1ZwFQSSnZcRvHA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Tygh?', 'Region': 'Tygh Ridge, OR',
     'Info': 'Launch @ 3330\' LZ @ 2860\'',
     # LZ: 45.305733, -121.110091
     'lat': '45.299156', 'lon': '-121.090714', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 315, 'windDirUpper': 45,  # Guessing NW to NE possible. Need to check it out in person.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/geH72q5sw6JKMSYM9',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': True},

    {'Name': 'Tygh West', 'Region': 'Tygh Ridge, OR',
     'Info': 'Launch @ 3180\' LZ @ 2780\'',
     # LZ: 45.302160, -121.122778
     'lat': '45.295592', 'lon': '-121.112203', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 293, 'windDirUpper': 360,  # Guessing WNW to N possible. Need to check it out in person.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/baA7rEYLL1y63QPG8',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': True},

    {'Name': 'Tygh South', 'Region': 'Tygh Ridge, OR',
     'Info': 'Launch @ 3500\' LZ @ 2700\' Seems like wind straight from South would provide sustained ridge lift.',
     # LZ: 45.272168, -121.105821
     'lat': '45.291153', 'lon': '-121.114031', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 112, 'windDirUpper': 225,  # Guessing ESE to SW possible. Need to check it out in person.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/VB9RRvayz9YZTUwYA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': True},

    {'Name': 'St Helens Hill', 'Region': 'St Helens, OR',
     'Info': 'Launch @ 530\' LZ is soccer field @ 90\' 45.898552, -122.815175',
     'lat': '45.894219', 'lon': '-122.824575', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 45, 'windDirUpper': 90,  # Guessing NE to E. Need to check it out in person.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/K6jBn7cLMKUBYv188',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': True},

    {'Name': 'Laughlin Hills', 'Region': 'North Central OR',
     'Info': 'Test Site! Launch from Foreman Point and land on Sunflower Flat '
             '\nSee Also: https://www.dfw.state.or.us/maps/wildlife_areas/whiteriver.pdf',
     'lat': '45.086833', 'lon': '-121.400501', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 135, 'windDirUpper': 225,  # SE to SW TODO: Get real wind dirs
     'windLower': 0, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/BkoYdzQ4P8sptQeC6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': False},

    {'Name': 'Graveyard Butte', 'Region': 'North Central OR',
     'Info': 'Test Site! Launch from Graveyard Butte Camp on BLM land'
             '\nSee Also: https://www.dfw.state.or.us/maps/wildlife_areas/whiteriver.pdf',
     'lat': '45.153447', 'lon': '-121.302184', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 135, 'windDirUpper': 225,  # SE to SW TODO: Get real wind dirs
     'windLower': 0, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/8Gj3uD2RoRkjLq6n6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': False},

]
