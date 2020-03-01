import numpy as np
def Sigmoid_function(x):       #二分类使用
    s = 1 / (1 + np.exp(-x))
    return s

def Softmax_function(x):       #多分类使用
    x_exp=np.exp(x)
    x_sum=np.sum(x_exp,axis=1,keepingdms=True)
    return x_exp/x_sum

def Sigmoid_gradien(x):        #Sigmoid梯度下降
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return ds

def Reshaping_arrays(x):       #矩阵转换形态x.reshape重塑形态，x.shape获取当前形态
    v = x.reshape((x.shape[0] * x.shape[1] * x.shape[2]))
    return v

def Normalizing_rows(x):       #归一化或者说把向量单位化
    x0 = np.linalg.norm(x, axis=1, keepdims=True)   # 求矩阵的范数-np.linalg.norm(矩阵名，axis=1为1范数/axis=2为2范数/axis=np.inf为无穷范数，keepingdims为是否保持矩阵的二维特性)
    x = x / x0
    return x

def Loss(yhat,y):              #yhat为预测值，y为准确值
    loss=np.dot((y-yhat),(y-yhat))                  # np.dot矩阵相乘
    return loss


