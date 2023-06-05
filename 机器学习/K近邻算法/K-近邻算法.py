# -*- codeing = utf-8 -*-
import numpy as np
import operator

#(1)准备数据集
def createDataSet():
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    labels = ["爱情片","爱情片","动作片","动作片"]
    return group,labels



#(2)k-近邻算法
"""
函数说明:kNN算法,分类器

Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果

Modify:
    2017-07-13
"""
def classify0(inX, dataSet, labels, k):
    #numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    #在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    """
    np.tile(inX, (dataSetSize, 1)) 的作用是将测试数据点 i
    nX 在横向上重复 dataSetSize 次，纵向上重复1次，
    得到一个新的矩阵。这个新的矩阵与数据集 dataSet 的形状相同，
    用于计算测试数据点与数据集中每个数据点之间的差。
    """
    #二维特征相减后平方
    sqDiffMat = diffMat**2
    #sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    #开方，计算出距离
    distances = sqDistances**0.5
    #返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()

    #定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        #取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        #计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #python3中用items()替换python2中的iteritems()
    #key=operator.itemgetter(1)根据字典的值进行排序
    #key=operator.itemgetter(0)根据字典的键进行排序
    #reverse降序排序字典
    #classCount.items() 将字典 classCount 转换为由键值对元组组成的列表
    #key=operator.itemgetter(1) 表示按照每个元组的第二个元素（即值）进行排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #返回次数最多的类别,即所要分类的类别

    return sortedClassCount[0][0]


if __name__ == "__main__":
    group,labels = createDataSet()
    print(group)
    print(labels)
    test = [101,20]
    test_class = classify0(test,group,labels,3)
    print(test_class)