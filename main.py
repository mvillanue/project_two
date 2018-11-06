
def headers():
    return ["cap-shape","cap-surface","cap-color","bruises","odor","gil-attachment","gill-spacing","gill-size","gill-color","salk-shape","stalk-root","stalk-surface-above-ring","stalk-surface-below-ring","stalk-color-above-ring","stalk-color-below-ring","veil-type","veil-color","ring-number","ring-type","spore-print-color","population","habitat"]

def readFile(filename):
    data = list()
    with open(filename) as f:
        for line in f:
            data.append(line.rstrip())
    
    return data

print readFile("expanded")


from pptree import *

"""shame = Node("shame")

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