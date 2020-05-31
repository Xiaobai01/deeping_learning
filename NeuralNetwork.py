from numpy import array,random,dot,exp

def fp(l0):
    l1 = 1 / (1 + exp(-dot(l0, W0)))
    l2 = 1 / (1 + exp(-dot(l1, W1)))
    return l1,l2

def bp(Y,l1,l2):
    # 查看误差并实现梯度下降算法
    l2_error = Y - l2
    # 计算斜率
    l2_K = l2 * (1 - l2)
    # 计算增量
    l1_delta = l2_K * l2_error

    #同理求l1
    l1_k=l1*(1-l1)
    l0_error=l1_delta.dot(W1.T)
    l0_delta=l0_error*l1_k


    return l0_delta,l1_delta


l0=array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])#训练数据集
Y=array([[0,1,1,0]]).T                #训练集中的结果


#随机生成权重
random.seed(1)
W0=2*random.random((3,40))-1
W1=2*random.random((40,1))-1

#正向推测应用Sigmoid（）激活函数，采用向量机实现点乘
for i in range(10000000):
    l1,l2=fp(l0)
    l0_delta,l1_delta=bp(Y,l1,l2)
#更新权重
    W1=W1+dot(l1.T,l1_delta)
    W0=W0+dot(l0.T,l0_delta)
#利用训练好的权重来预测新的值。


#输入预测数据集
X0=([[1,0,1]])
#进行预测并输出结果
Y0,Y1=fp(X0)
print(Y1)


