# Per http://cascadeparaglidingclub.org/site-guide/
# Columbia River Gorge
#     Bald Butte
#     Bald Butte North
#     Bingen
#     Cliffside
#     Dalles Mtn Ranch (Closed)
#     Dog Mtn/Gorge (Closed)
#     Doug’s Beach (Closed)
#     Eagle Caves
#     Hamilton Mountain (Closed)
#
# Willamette Valley
#     Chehalem
#     Gales Creek (Closed)
#     Gobblers (Closed)
#     Peterson Butte
#
# Coast Range
#     Marys Peak
#     Mt. Hebo (Closed)
#     Prairie Peak (Closed)
#
# Coast
#     Angora Knob  (Closed)
#     Area B
#     Cape Kiwanda
#     Cape Lookout State Park
#     Cape Perpetua (not a CPC site)
#     Ecola State Park (closed)
#     Neahkahnie (Closed)
#     Oceanside
#     Rock Creek (not a CPC site)
#     Saddle Mtn (Closed)
#     Sand Lake Dunes
#     Sollie Smith/Kilchis
#     Yaquina Head north (not a CPC site)
#     Yaquina Head south (not a CPC site)
#
# Cascades
#     Hoover Ridge
#     Mount St. Helens (not a CPC site)
#     Mount Hood (not a CPC site)
#     Silver Star
#     Toutle River Valley (Closed)
#
# Southern Oregon
#     Woodrat (RVHPA site)
#
# South-Central Oregon
#     Abert Rim (not a CPC site)
#     Lakeview (not a CPC site)
#     Winter Ridge (not a CPC site)
#
# Central Oregon
#     Pine Mountain (DAR site)
#
# Eastern Oregon
#     Mt. Howard (not a CPC site)
#
# Other sites
#     Kiting sites (not a CPC site)

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

sites = [
    {'Name': 'Yaquina Head',
                                'lat': '44.67640', 'lon': '-124.07810', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 270, 'windDirUpper': 360,
                                'windLower': 7, 'windUpper': 15,
                                'link': 'https://goo.gl/maps/ymRCog5w39KDjwnK7',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data
    {'Name': 'Cliffside',
                                'lat': '45.724844', 'lon': '-120.726470', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 45, 'windDirUpper': 135,
                                'windLower': 7, 'windUpper': 15,
                                'link': 'https://goo.gl/maps/zgzczeHDBNyuRFhP7',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data
    {'Name': 'Bingen',
                                'lat': '45.7255', 'lon': '-121.446', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 0, 'windDirUpper': 360,  # TODO: Is this correct? Split into Bingen W and E? or similar?
                                'windLower': 5, 'windUpper': 15,
                                'link': 'https://goo.gl/maps/zS1Fmr4DzzW54M8fA',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data

    {'Name': 'Cape Kiwanda',
                                'lat': '45.220660', 'lon': '-123.973579', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 270, 'windDirUpper': 360,
                                'windLower': 7, 'windUpper': 18,
                                'link': 'https://goo.gl/maps/sVw9j7cgveAjgzu78',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data
    {'Name': 'Area B',
                                'lat': '46.178162', 'lon': '-123.980713', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 205, 'windDirUpper': 290,
                                'windLower': 12, 'windUpper': 14,
                                'link': 'https://goo.gl/maps/Bpuv5dnaroBKFQCq9',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Oceanside',
                                'lat': '45.4654', 'lon': '-123.9710', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 202, 'windDirUpper': 270,  # SSW to W
                                'windLower': 5, 'windUpper': 15,
                                'link': 'https://goo.gl/maps/UtU2svqZ9vVuQSqG8',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Rock Creek',
                                'lat': '44.179333', 'lon': '-124.113083', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 202, 'windDirUpper': 293,  # SSW-WNW
                                'windLower': 5, 'windUpper': 15,
                                'link': 'https://goo.gl/maps/Eo4vvoNXwBh8GPK78',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Bald Butte',
                                'lat': '45.536542', 'lon': '-121.532970', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 247, 'windDirUpper': 293,  #WSW to WNW
                                'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
                                'link': 'https://goo.gl/maps/ppcUwkmvWw6so2id7',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Bald Butte North',  # LZ @: 45.5503, -121.5570
                                'lat': '45.551200', 'lon': '-121.534900', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 270, 'windDirUpper': 315,  # "The launch faces west, northwest. There is a second lower west face for higher wind launching. "
                                'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
                                'link': 'https://goo.gl/maps/C24ZWBsCJ8cMwvJK7',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Eagle Caves',  # LZ in the school fields. See info. online.
                                'lat': '45.622849', 'lon': '-121.234674', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 45, 'windDirUpper': 90,   # TODO: Ridge faces ENE. Using roughly this. Get real wind dirs.
                                'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
                                'link': 'https://goo.gl/maps/5W7vhzUqXYXQ14vF9',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
    {'Name': 'Dog Mnt.',  # LZ @ 45.700861, -121.723264
                                'lat': '45.716782', 'lon': '-121.701887', 'timezone_str': 'America/Los_Angeles',
                                'windDirLower': 247, 'windDirUpper': 292,
                                'windLower': 3, 'windUpper': 12,
                                'link': 'https://goo.gl/maps/Wa2n4ygKNYXQsxuy9',
                                'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
                                'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},
         ]
