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

    # OR Coast ---------------------------------------------------------------------------------------------------------
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

    {'Name': 'Cape Kiwanda',
     'lat': '45.220660', 'lon': '-123.973579', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 270, 'windDirUpper': 360,
     'windLower': 7, 'windUpper': 18,
     'link': 'https://goo.gl/maps/sVw9j7cgveAjgzu78',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data

    {'Name': 'Yaquina Head (North)',
     'lat': '44.67640', 'lon': '-124.07810', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 315, 'windDirUpper': 360,
     'windLower': 10, 'windUpper': 18,
     'link': 'https://goo.gl/maps/ymRCog5w39KDjwnK7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Yaquina Head (South)',
     'lat': '44.674939', 'lon': '-124.066994', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 180, 'windDirUpper': 225,
     'windLower': 10, 'windUpper': 15,
     'link': 'https://www.google.com/maps/dir/44.6738817,-124.0621217/44.6749517,-124.0669741/@44.6671123,-124.0672885,987a,35y,3.37h,39.37t/data=!3m1!1e3!4m2!4m1!3e2',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Rock Creek',
     'lat': '44.179333', 'lon': '-124.113083', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 202, 'windDirUpper': 293,  # SSW-WNW
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/Eo4vvoNXwBh8GPK78',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    # The Gorge --------------------------------------------------------------------------------------------------------
    # {'Name': 'Dog Mnt.',  # LZ @ 45.700861, -121.723264
    #                             'lat': '45.716782', 'lon': '-121.701887', 'timezone_str': 'America/Los_Angeles',
    #                             'windDirLower': 247, 'windDirUpper': 292,
    #                             'windLower': 3, 'windUpper': 12,
    #                             'link': 'https://goo.gl/maps/Wa2n4ygKNYXQsxuy9',
    #                             'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
    #                             'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Bingen',
     'lat': '45.7255', 'lon': '-121.446', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 0, 'windDirUpper': 360,  # TODO: Is this correct? Split into Bingen W and E? or similar?
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/zS1Fmr4DzzW54M8fA',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data

    {'Name': 'Eagle Caves',  # LZ in the school fields. See info. online.
     'lat': '45.622849', 'lon': '-121.234674', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 45, 'windDirUpper': 90,  # TODO: Ridge faces ENE. Using roughly this. Get real wind dirs.
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/5W7vhzUqXYXQ14vF9',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Cliffside',
     'lat': '45.724844', 'lon': '-120.726470', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 45, 'windDirUpper': 135,
     'windLower': 7, 'windUpper': 15,
     'link': 'https://goo.gl/maps/zgzczeHDBNyuRFhP7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},  # TODO: Fix wind data

   # Mnt Hood ----------------------------------------------------------------------------------------------------------
    {'Name': 'Bald Butte',
     'lat': '45.536542', 'lon': '-121.532970', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 247, 'windDirUpper': 293,  # WSW to WNW
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/ppcUwkmvWw6so2id7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    {'Name': 'Bald Butte North',  # LZ @: 45.5503, -121.5570
     'lat': '45.551200', 'lon': '-121.534900', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 270, 'windDirUpper': 315,
     # "The launch faces west, northwest. There is a second lower west face for higher wind launching. "
     'windLower': 5, 'windUpper': 15,  # TODO: Get real wind speeds
     'link': 'https://goo.gl/maps/C24ZWBsCJ8cMwvJK7',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': False, 'show_snowLevel': False},

    # Central OR -------------------------------------------------------------------------------------------------------
    # Pine Mountain Sites (Desert Air Riders - Paragliding Central Oregon)
    # https://docs.google.com/document/d/1OE0ICBCPaOSHbljiof710qh_ET75tyd358h27jz4xpI/edit
    {'Name': 'Pine Ridge',  # LZ @ TBD
     'lat': '44.423912', 'lon': '-121.066997', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 310, 'windDirUpper': 360,
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/TeDWcKQ8k5gMN2UM6',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': False},

    # https://docs.google.com/document/d/17eNwgcEzoAyrTJLESKELOqp9eNICrVljCQ-aHkrY4Gg/edit
    # https://www.google.com/maps/d/u/0/viewer?mid=1YpxFboEQkS78zbKCXbfX_uhn4Vo&ll=43.84679298310765%2C-120.96279087463729&z=12
    {'Name': 'Pine Mnt: Training Hill',  # "Rock L" Parking LZ @ 43.83716, -120.93033
     'lat': '43.833422', 'lon': '-120.926337', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 310, 'windDirUpper': 360,
     'windLower': 2, 'windUpper': 18,
     'link': 'https://goo.gl/maps/1esfGRRhDW395dS1A',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': False},

    {'Name': 'Pine Mnt: West PG Launch',  # "Rock L" Parking LZ @ 43.83716, -120.93033 (yes, same LZ as training hill)
     'lat': '43.821283', 'lon': '-120.93145', 'timezone_str': 'America/Los_Angeles',
     'windDirLower': 270, 'windDirUpper': 350,
     'windLower': 5, 'windUpper': 15,
     'link': 'https://goo.gl/maps/ukb7WYabzFop7ZGH8',
     'show_dewpoint': False, 'show_rh': False, 'show_skyCover': True,
     'show_pop': True, 'show_qpf': True, 'show_snowAmt': True, 'show_snowLevel': False},
     ]
