class Palette:
    """
    This class is a color palette. Should let us try different color schemes easily.
    """
    def __init__(self, in_string):

        if in_string == 'darkmode':  # TODO: This is a garbage palette; just an example. Make it nice. Add seasonal palettes. Pumpkin spice latte, etc.
            # Default, dark background, light text, red/green/grey color scheme
            Palette.bdclr = '#003545'
            Palette.bkgnd = '#003545'
            Palette.warn = '#ed6363'
            Palette.good = '#3c6562'
            Palette.lame = '#00454a'
            Palette.text = '#aaaaaa'
            Palette.title = '#cccccc'
            Palette.desc = '#aaaaaa'

        else:  # default
            # Default, white background, dark text, red/green/grey color scheme
            Palette.bdclr = '#ffffff'
            Palette.bkgnd = '#fafafa'
            Palette.warn = '#ffcccc'
            Palette.good = '#ccffcc'
            Palette.lame = '#cccccc'
            Palette.text = '#000000'
            Palette.title = '#0000ff'
            Palette.desc = '#999999'
