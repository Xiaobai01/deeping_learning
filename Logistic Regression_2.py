
#encoding:UTF-8
import csv
import numpy as np
from math import *
from numpy.linalg import *
from matplotlib import pyplot as plt
 
#牛顿迭代法实现对数几率回归
 
old_ml=0 #初始似然函数值
n=0 
beta=np.mat([[0],[0],[1]])
 

wm_data_30a = csv.reader(open("watermelonDataset.csv的路径",'r'))
 
xi_d = np.mat(np.zeros((17,3)))
yi_d = np.mat(np.zeros((17,1)))


sn=0
for stu in wm_data_30a:


	if(stu[0].isdigit()==True):
		xi_d[sn,:] = np.mat([float(stu[1]),float(stu[2]),1])
		yi_d[sn,0] = float(stu[3])
		sn = sn+1



xi = np.mat(np.zeros((3,1)))
while(iter<10):
	sn=0
	print('iter=',iter)
	new_ml=0
	for idx in range(17):
				
		xi = xi_d[idx,:].T
		yi=yi_d[idx,0]
		new_ml = new_ml + log(1+e**det(beta.T*xi)) - yi*det(beta.T*xi)
	print('new ml=',new_ml)
	if abs(new_ml-old_ml)<0.001:
		print(new_ml-old_ml)
		print(beta)
		break

	old_ml = new_ml
	dml_beta_1 = np.mat([[0],[0],[0]])
	dml_beta_2 = np.mat(np.zeros((3,3)))

	for idx in range(17):
		xi = xi_d[idx,:].T 
		yi=yi_d[idx,0]
		p1_xi = 1-1/(1+e**(det(beta.T*xi)))
		dml_beta_1 = dml_beta_1 - xi*(yi-p1_xi)
		dml_beta_2 = dml_beta_2 + xi*(xi.T)*p1_xi*(1-p1_xi)
	beta = beta - (dml_beta_2.I)*dml_beta_1
	print('beta=',beta)
	iter=iter+1

 
for idx in range(17):
	if yi_d[idx,0]==1:
		plt.plot(xi_d[idx,0],xi_d[idx,1],'+r')
	else:
		plt.plot(xi_d[idx,0],xi_d[idx,1],'ob')

ply=-(0.1*beta[0,0]+beta[2,0])/beta[1,0];
pry=-(0.9*beta[0,0]+beta[2,0])/beta[1,0];
 
px=[0.1,0.9]
py=[ply,pry]
 
plt.plot(px,py)
 
 
plt.xlabel('density')
plt.ylabel('suger ratio')
plt.title('logistic function regression')
plt.show()