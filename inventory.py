class Card:
    def __init__(self, count, name, edition, foil):
        self.count = count
        self.name = name
        self.edition = edition
        self.foil = foil

    def showInfo(self):
        return "{}, {}, {}, {}".format(self.count, self.name, self.edition, self.foil)
