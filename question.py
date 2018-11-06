class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        return val == self.value

    def __repr__(self):

        condition = "=="

        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))