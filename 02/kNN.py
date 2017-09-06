'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

@author: pbharrin
'''
from numpy import *
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)  # 得到文件行数
	
	# 创建将返回的np矩阵
	returnMat = zeros((numberOfLines, 3))
	# 标签向量
	classLabelVector = []

	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, : ] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1

	return returnMat, classLabelVector

# 归一化
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet / tile(ranges, (m, 1))
	return normDataSet, ranges, minVals

# 测试
def datingClassTest():
	hoRatio = 0.10

	# 获得数据
	datingDataMat, datingLabels = file2matrix("Ch02/datingTestSet2.txt")
	normMat, ranges, minVals = autoNorm(datingDataMat)

	# 计算测试集应该有的数据数目
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		# 训练
		classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		print("算法返回：%d, 真实结果：%d, === %d" % (classifierResult, datingLabels[i], 1 if classifierResult == datingLabels[i] else 0))
		if (classifierResult != datingLabels[i]): errorCount += 1.0

	print("错误率：%f" % (errorCount / float(numTestVecs)))	

# 测试某个人
def classifyPerson():
	resultList = ['没魅力', '有一点魅力', '魅力十足']
	percentTats = float(input("打游戏时间比？"))
	ffMiles = float(input("一年的坐飞机距离？"))
	iceCream = float(input("每周消费的冰激凌？"))
	datingDataMat, datingLabels = file2matrix('Ch02/datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
	print("你对这个人的喜好程度：", resultList[classifierResult - 1])

# digits识别 数据处理
def img2vector(filename):
	returnVect = zeros((1, 1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, 32*i + j] = int(lineStr[j])
	return returnVect

# 手写数字分类系统的测试代码
def handwritingClassTest():
	# 获得训练集数据
	hwLabels = []     # 标签向量
	
	trainingFileList = listdir('Ch02/digits/trainingDigits')
	m = len(trainingFileList)	
	trainingMat = zeros((m, 1024))    # 训练数据矩阵

	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)        # 获得标签
		trainingMat[i, :] = img2vector('Ch02/digits/trainingDigits/%s' % fileNameStr)  # 获得训练样本

	# 计算错误率
	testFileList = listdir('Ch02/digits/testDigits')
	mTest = len(testFileList)
	errorCount = 0.0
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('Ch02/digits/testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
		print("分类器结果：%d;真实结果： %d" % (classifierResult, classNumStr))
		if (classifierResult != classNumStr) : 
			errorCount += 1.0
			print("================================================================")
	print("错误数： %d" % errorCount)
	print("错误率： %f" % (errorCount / float(mTest)))
    
