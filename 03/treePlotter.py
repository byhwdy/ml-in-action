import matplotlib.pyplot as plt
from pylab import *

# 中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',xytext=centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(U'叶结点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

# 获得叶结点数目
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = list(iter(myTree.keys()))[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]). __name__ == 'dict':
			numLeafs += getNumLeafs(secondDict[key])
		else: 
			numLeafs += 1
	return numLeafs

# 获得树的层数
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = list(iter(myTree.keys()))[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]). __name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else:
			thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth

# 树信息
def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]

# 在父子节点间填充文本信息
def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
	createPlot.ax1.text(xMid, yMid, txtString)

