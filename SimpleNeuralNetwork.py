from numpy import array,random,dot,exp
X=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])#训练数据集
Y=array([[0,1,1,0]]).T                #训练集中的结果
#随机生成权重
random.seed(1)
W=2*random.random((3,1))-1
#正向推测应用Sigmoid（）激活函数，采用向量机实现点乘
for i in range(100000):
    output=1/(1+exp(-dot(X,W)))
#查看误差并实现梯度下降算法
    error=Y-output
#计算斜率
    K=output*(1-output)
#计算增量
    delta=K*error
#更新权重
    W=W+dot(X.T,delta)
#利用训练好的权重来预测新的值。


#输入预测数据集
X0=([[1,1,0]])
#进行预测并输出结果
Y0=1/(1+exp(-dot(X0,W)))
print(Y0)


