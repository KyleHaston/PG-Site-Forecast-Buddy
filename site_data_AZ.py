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

sites_AZ = [

    {'Name': 'Mustang Peak', 'Region': 'AZ',
     'Info': '(Don\'t launch in winds over 16 knots (18 mph)!  Or OTB you go).',
     'lat': '31.702867', 'lon': '-110.491925', 'timezone_str': 'America/Phoenix',
     'windDirLower': 200, 'windDirUpper': 290,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/u57arnppGL4LW3zh9',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': False,
     'show_pop': False, 'show_qpf': False, 'show_snowAmt': False},

    {'Name': 'Creedence', 'Region': 'AZ',
     'Info': '',
     'lat': '31.775972', 'lon': '-110.841174', 'timezone_str': 'America/Phoenix',
     'windDirLower': 240, 'windDirUpper': 340,
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/7gHv7R8Y26WUCweW8',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': False,
     'show_pop': False, 'show_qpf': False, 'show_snowAmt': False},

    {'Name': 'Sentinel Pk (A-Mnt) L1 SE Asphalt Ramp', 'Region': 'AZ',
     'Info': '',
     'lat': '32.208540', 'lon': '-110.994354', 'timezone_str': 'America/Phoenix',
     'windDirLower': 140, 'windDirUpper': 160,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/hsHTMhLtv1NstTpeA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Sentinel Pk (A-Mnt) L2, Top', 'Region': 'AZ',
     'Info': '',
     'lat': '32.210272', 'lon': '-110.992304', 'timezone_str': 'America/Phoenix',
     'windDirLower': 70, 'windDirUpper': 100,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/24XgbGPMCBVwNCw28',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Box Canyon', 'Region': 'AZ',
     'Info': 'Box Canyon Top Launch 31.817232, -110.78691\n' +
             'Box Canyon Mid Launch 31.821716, -110.782473\n' +
             'Box Canyon Lower Launch 31.821012, -110.7964\n' +
             'WNW to NW Winds are the good for all three launches.  Direct West winds can be dangerous at lower launch',
     'lat': '31.817232', 'lon': '-110.78691', 'timezone_str': 'America/Phoenix',
     'windDirLower': 290, 'windDirUpper': 320,
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/q32W85EgG7X3qifH7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Naranja Park Kiting Site', 'Region': 'AZ',
     'Info': '',
     'lat': '32.413797', 'lon': '-110.981150', 'timezone_str': 'America/Phoenix',
     'windDirLower': 0, 'windDirUpper': 360,
     'windLower': 5, 'windUpper': 20,
     'link': 'https://goo.gl/maps/xcAwRUZLiu7c1abu7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    # Near Flagstaff, AZ
    {'Name': 'Merriam Crater', 'Region': 'Northern AZ',
     'Info': '',
     'lat': '35.338916', 'lon': '-111.286283', 'timezone_str': 'America/Phoenix',
     'windDirLower': 315, 'windDirUpper': 45,  # NE to NW per Kurt
     'windLower': 0, 'windUpper': 12,  # per Kurt
     'link': 'https://goo.gl/maps/Sgwga7erGowTjjhE6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Apache Maid', 'Region': 'Northern AZ',
     'Info': '',
     'lat': '34.725802', 'lon': '-111.551234', 'timezone_str': 'America/Phoenix',
     'windDirLower': 135, 'windDirUpper': 225,  # SE to SW per Kurt
     'windLower': 5, 'windUpper': 10,  # per Kurt
     'link': 'https://goo.gl/maps/uswUhjMe394Qjs699',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    {'Name': 'Mount Elden', 'Region': 'Northern AZ',
     'Info': '',
     'lat': '35.240906', 'lon': '-111.607948', 'timezone_str': 'America/Phoenix',
     'windDirLower': 90, 'windDirUpper': 270,  # E to W (any southern direction is flyable) per Kurt
     'windLower': 0, 'windUpper': 12,  # per Kurt
     'link': 'https://goo.gl/maps/JEkG6TEe7g9rcdT77',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

    # {'Name': '', 'Region': '',
    #  'Info': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Phoenix',
    #  'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False},

]
