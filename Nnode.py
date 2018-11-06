class Nnode:

    def __init__(self, question, true_node, false_node):
        self.question = question
        self.true_node = true_node
        self.false_node = false_node

    def __str__(self):
        return self.question