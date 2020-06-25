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
     'Desc': '(Don\'t launch in winds over 16 knots (18 mph)!  Or OTB you go).',
     'lat': '31.702867', 'lon': '-110.491925', 'timezone_str': 'America/Phoenix',
     'windDirLower': 200, 'windDirUpper': 290,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/u57arnppGL4LW3zh9',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': False,
     'show_pop': False, 'show_qpf': False, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Creedence', 'Region': 'AZ',
     'Desc': '',
     'lat': '31.775972', 'lon': '-110.841174', 'timezone_str': 'America/Phoenix',
     'windDirLower': 240, 'windDirUpper': 340,
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/7gHv7R8Y26WUCweW8',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': False,
     'show_pop': False, 'show_qpf': False, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Sentinel Pk (A-Mnt) L1 SE Asphalt Ramp', 'Region': 'AZ',
     'Desc': '',
     'lat': '32.208540', 'lon': '-110.994354', 'timezone_str': 'America/Phoenix',
     'windDirLower': 140, 'windDirUpper': 160,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/hsHTMhLtv1NstTpeA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Sentinel Pk (A-Mnt) L2, Top', 'Region': 'AZ',
     'Desc': '',
     'lat': '32.210272', 'lon': '-110.992304', 'timezone_str': 'America/Phoenix',
     'windDirLower': 70, 'windDirUpper': 100,
     'windLower': 5, 'windUpper': 16,
     'link': 'https://goo.gl/maps/24XgbGPMCBVwNCw28',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Box Canyon', 'Region': 'AZ',
     'Desc': 'Box Canyon Top Launch 31.817232, -110.78691\n' +
             'Box Canyon Mid Launch 31.821716, -110.782473\n' +
             'Box Canyon Lower Launch 31.821012, -110.7964\n' +
             'WNW to NW Winds are the good for all three launches.  Direct West winds can be dangerous at lower launch',
     'lat': '31.817232', 'lon': '-110.78691', 'timezone_str': 'America/Phoenix',
     'windDirLower': 290, 'windDirUpper': 320,
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/q32W85EgG7X3qifH7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Naranja Park Kiting Site', 'Region': 'AZ',
     'Desc': '',
     'lat': '32.413797', 'lon': '-110.981150', 'timezone_str': 'America/Phoenix',
     'windDirLower': 0, 'windDirUpper': 360,
     'windLower': 5, 'windUpper': 20,
     'link': 'https://goo.gl/maps/xcAwRUZLiu7c1abu7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    # {'Name': '', 'Region': '',
    #  'Desc': '',
    #  'lat': '', 'lon': '', 'timezone_str': 'America/Phoenix',
    #  'windDirLower': 0, 'windDirUpper': 360,  # TODO: Get real wind dirs
    #  'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
    #  'link': '',
    #  'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #  'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

]
