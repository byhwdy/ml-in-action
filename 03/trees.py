from math import log
import operator

# 计算信息熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)

	# 统计分类数目
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1

	# 计算
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)

	return shannonEnt

# 创建鱼类数据集
def createDataSet():
	dataSet = [[1, 1, 'yes'],
			   [1, 1, 'yes'],
			   [1, 0, 'no'],
			   [0, 1, 'no'],
			   [0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels

# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

# 叶子节点有多个分类时的多数表决
def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

# 创建决策树
def createTree(dataSet, labels):
	# 数据集的类别列表
	classList = [example[-1] for example in dataSet]
	# 类别完全相同则停止继续划分
	if classList.count(classList[0]) == len(classList): 
		return classList[0]
	# 遍历完所有特征时返回出现次数最多的类别
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLable = labels[bestFeat]
	myTree = {bestFeatLable:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

	return myTree

