class Palette:
    """
    This class is a color palette. Should let us try different color schemes easily.
    """
    def __init__(self, in_string):

        if in_string == 'darkmode':  # TODO: This is a garbage palette; just an example. Make it nice. Add seasonal palettes. Pumpkin spice latte, etc.
            # Default, dark background, light text, red/green/grey color scheme
            self.bdclr = '#003545'
            self.bkgnd = '#003545'
            self.warn = '#ed6363'
            self.rain = '#b3d9ff'
            self.good = '#3c6562'
            self.lame = '#00454a'
            self.text = '#aaaaaa'
            self.title = '#cccccc'
            self.desc = '#aaaaaa'

        else:  # default
            # Default, white background, dark text, red/green/grey color scheme
            self.bdclr = '#ffffff'
            self.bkgnd = '#fafafa'
            self.warn = '#ffcccc'
            self.rain = '#b3d9ff'
            self.good = '#ccffcc'
            self.lame = '#cccccc'
            self.text = '#000000'
            self.title = '#0000ff'
            self.desc = '#555555'
