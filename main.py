


def readFile(filename):
    data = list()
    with open(filename) as f:
        for line in f:
            data.append(line.rstrip())
    
    return data

print readFile("expanded")


"""from pptree import *

shame = Node("shame")

conscience = Node("conscience", shame)
selfdisgust = Node("selfdisgust", shame)
embarrassment = Node("embarrassment", shame)

selfconsciousness = Node("selfconsciousness", embarrassment)
shamefacedness = Node("shamefacedness", embarrassment)
chagrin = Node("chagrin", embarrassment)
discomfiture = Node("discomfiture", embarrassment)
abashment = Node("abashment", embarrassment)
confusion = Node("confusion", embarrassment)
  
print_tree(shame)"""