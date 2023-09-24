class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, x):
        if x in self.pouch_contents:
            print("object already in pouch")
        else:
            self.pouch_contents.append(x)

    def __str__(self):
        if len(self.pouch_contents) == 0:
            return "The kangaroo's pouch is empty."
        else:
            return "The kangaroo's pouch contains: "\
                  + str(self.pouch_contents)
