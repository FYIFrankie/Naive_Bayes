

def classify(data, class_val):

    separte = {}
    separte[-1] = []
    separte[1] = []

    for point in data:
        if point[class_val] == 1:
            separte[1].append(point)
        else:
            separte[-1].append(point)
    return separte