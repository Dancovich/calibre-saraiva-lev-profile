import os
from calibre.customize.profiles import OutputProfile

class CybookOdyssey(OutputProfile):

    author      = 'Danilo Costa Viana'
    name        = 'Cybook Odyssey'
    short_name  = 'cybookodyssey'
    description = _('This profile is intended for the Cybook Odyssey and Cybook Odyssey Frontlight 2 devices.')

    screen_size               = (758, 1024)
    comic_screen_size         = (750, 856)
    dpi                       = 213
    fbase                     = 29
    fsizes                    = [17, 20, 23, 26, 29, 32, 35, 38, 41, 47, 53, 59, 65, 71, 76, 82, 88, 94, 100, 106]
    touchscreen               = True

