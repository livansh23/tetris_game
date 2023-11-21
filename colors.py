class Colors:
    black = (0,0,0) # Color of the empty cell
    orange = (226, 116, 17)
    green = (47, 230, 23)
    red = (232, 18, 18)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    grey = (35, 45, 63)
    light_grey = (211, 211, 211)


    @classmethod # This is a python decorator which can call a method on eitire class rather than one instance of class
    def get_cell_colors(cls):
            return[ cls.black, cls.orange, cls.green, cls.red, cls.yellow, cls.purple, cls.cyan, cls.blue]

        