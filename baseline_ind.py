import csv
import sys, os

from PIL import Image

DATA_PATH = "../CS221"
LABEL_FILE = "../CS221/allAnnotations.csv"
NUM_ITERATIONS = 10

def featureExtractor(imagePath):
    #thresholds
    bt = 10
    gt = 10
    rt = 0

    rawpixels = []
    im = Image.open(imagePath)
    w, h = im.width, im.height
    blob = im.make_blob(format='RGB')
    pixels = img.load()

    featureVec = {}
    for i in range(0, img.size[0]):
        for j in range(0,img.size[1]):
            (r,g,b) = rawpixels[i]
            if b < bt and g < gt and r > rt:
                data[(r,g,b)] = 1

    return featureVec

def dotProduct(v1, v2):
    common_nonzero_indices = [index for index in v1 if index in v2]
    return sum([v1[index]*v2[index] for index in common_nonzero_indices])

def increment(v1, scale, v2):
    for elem in v2:
        v1[elem] += (scale * v2[elem])

def evaluate(examples, classifier):
    error = 0
    for x, y in examples:
        if classifier(x) != y:
            error += 1

    return float(error)/len(examples)

def SGD(trainExamples, testExamples):
    weights = {}  # feature => weight
    def grad(weights, trainExample):
        x = trainExample[0]
        y = trainExample[1]
        features = featureExtractor(x)
        features_scaled_y = {}
        for feature in features:
            features_scaled_y[feature] = features[feature]*y
        if dotProduct(weights, features_scaled_y) < 1:
            for value in features:
                features[value] *= -y
            return features
        else:
            return {}
    temp = []
    for i in range(0,len(trainExamples)):
        tEx = trainExamples[i]
        if os.path.isfile(tEx[0]) == True:
            temp.append(tEx)

    numIters = NUM_ITERATIONS
    for i in range(numIters):
        step_size = 0.00225
        for trainExample in temp:
            gradient = grad(weights, trainExample)
            increment(weights, -step_size, gradient)

        trainError = evaluate(temp, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
        print trainError
        # testError = evaluatePredictor(testExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
        # print trainError, testError
    return weights

def get_image_labels():
    label_tuples = []
    with open(LABEL_FILE, 'rb') as labels_file:
        labelreader = csv.reader(labels_file, dialect='excel')
        counter = 0
        for row in labelreader:
            if counter == 0:
                counter = 1
                continue
            line = row[0]
            split_line = line.split(';')
            label = -1
            if split_line[1] == "stop":
                label = 1
            label_tup = (split_line[0], label)
            label_tuples.append(label_tup)

    return label_tuples


def main():
    trainExamples = get_image_labels()
    testExamples = []
    #SGD(trainExamples, testExamples)
    print trainExamples
    print "test"

if __name__ == "__main__":
    main()
