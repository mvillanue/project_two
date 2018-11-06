def headers():
    return ["cap-shape","cap-surface","cap-color","bruises","odor","gil-attachment","gill-spacing","gill-size","gill-color","salk-shape","stalk-root","stalk-surface-above-ring","stalk-surface-below-ring","stalk-color-above-ring","stalk-color-below-ring","veil-type","veil-color","ring-number","ring-type","spore-print-color","population","habitat"]

def readFile(filename):
    data = list()
    with open(filename) as f:
        for line in f:
            data.append(line.rstrip().split(','))
    
    return data


def unique_vals(rows, col):
    return set([row[col] for row in rows])