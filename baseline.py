DATA_PATH = ""
NUM_ITERATIONS = 10

def featureExtractor(imagePath):
    featureVec = {}
    image =  something imagePath
    for pixel in image:
        if red:
            featureVec[pixel] = 1
    return featureVec

def dotProduct(v1, v2):
    common_nonzero_indices = [index for index in v1 if index in v2]
    return sum([v1[index]*v2[index] for index in common_nonzero_indices])

def increment(v1, scale, v2):
    for elem in v2:
        v1[elem] += (scale * v2[elem])

def evaluate(examples, classifier):
    error = 0

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

    numIters = NUM_ITERATIONS
    for i in range(numIters):
        step_size = 0.00225
        for trainExample in trainExamples:
            gradient = grad(weights, trainExample)
            increment(weights, -step_size, gradient)

        # trainError = evaluatePredictor(trainExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
        # testError = evaluatePredictor(testExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
        # print trainError, testError
    return weights

def get_image_labels():
	label_tuples = []
	with open(os.path.join(DATA_PATH, LABEL_FILE), 'r') as label_map_file:
		for line in label_map_file:
			split_line = line.split()
			label_tup = (split_line[0], int(split_line[1]))
            label_tuples.append(label_tup)

	return label_tuples

def main():
    trainExamples = get_image_labels()
    testExamples = []
    SGD(trainExamples, testExamples) 

if __name__ = "__main__":
    main()