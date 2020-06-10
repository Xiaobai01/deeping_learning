import numpy as np
import math
import random
#————————————————————————————————————————————————————变量————————————————————————————————————————————————————————————————

crossRate = 0.8        #交叉概率
mutationRate = 0.1      #突变概率

#-------------------------------------------------导入数据---------------------------------------------------------------

np.set_printoptions(suppress=True)
City = np.loadtxt('数据集.txt',dtype=np.int)

#————————————————————————————————————————————————功能函数————————————————————————————————————————————————————————————————

def dict_to_list(str):                                  #字符串转换list
    str = str[:-1]
    a=str.split(',')
    b=[int(i) for i in a]
    return b

def final_pop(temp_pop,City):
    temp=[[[0 for k in range(3)]for j in range(len(temp_pop[0]))] for i in range(len(temp_pop))]
    p=0
    #print('---------------------------------------------------')
    for i in range(len(temp_pop)):
        q = 0
        for j in range(len(temp_pop[i])-1):
            for k in range(len(City)):
                if temp_pop[i][j]==City[k][0]:
                    temp[p][q][0]=temp_pop[i][j]
                    temp[p][q][1]=City[k][1]
                    temp[p][q][2]=City[k][2]
                    q=q+1
                    #print('i:', i,' ','j: ', j,'k: ', k,'temp_pop: ', len(temp_pop),'temp_pop[1]   ', len(temp_pop[1]))
                    #print('p:', p,  'q    ', q,  'temp:  ', len(temp),'temp[0]:', len(temp[0]))

        p=p+1
        #print(p)
        #print(len(temp))
    return temp


def Creat_pop(size):                                    #创建种群
    pop = []
    for i in range(size):
        temp=np.random.permutation(City)                #打乱数组
        pop.append(temp)                                #加入种群
    return pop



#-------------------------------------------------计算适应值------------------------------------------------------------------

def Distance(City):  #计算每次的距离,也可记为染色体
    #print(City)
    total=len(City)
    distance=0
    for i in range(total-1):
        distance =distance+ math.sqrt((City[i][1] - City[i+1][1]) ** 2 + (City[i][2] - City[i+1][2]) ** 2)
    return distance

def Match(pop):                                        #传入单个染色体
   # print(pop)
    match=1/Distance(pop)
    a = ' '
    for i in range(len(pop)):
        a=a+str(pop[i][0])+','
    return a,match
'''
def init(pop):                                          #传入一个种群
    temp=dict()
    for i in range(len(pop)):
        k, value = Match(pop[i])
        temp[k] = value
    return temp
'''
def init_dict(pop):
    temp=dict()
    sum=0
    for i in range(len(pop)):                          #存入字典
      #  print(pop[i])
        k, value = Match(pop[i])
        temp[k] = value
    ks=list(temp.keys())
    for i in range(len(ks)):                           #计算字典的值之和
        sum=sum+temp[ks[i]]
    for i in range(len(ks)):                           #完成字典值的最终结果
        temp[ks[i]]=temp[ks[i]]/sum
    return temp

#-------------------------------------------------交叉------------------------------------------------------------------
def Cross(parent1, parent2):
    index1 = np.random.randint(0, len(City)-1)
    index2 = np.random.randint(index1, len(City)-1)
    tempGene = parent2[index1:index2]                 #  交叉的基因片段
    newGene = []
    newGene.extend(tempGene)  # 插入基因片段
    for i in range(len(parent1)) :
            if parent1[i] not in newGene:
                newGene.append(parent1[i])
    return newGene
#-------------------------------------------------突变------------------------------------------------------------------
def Mutation(gene):
    #print(type(gene))
    gene=gene[::-1]
    index1 = np.random.randint(0, len(gene) - 1)
    index2 = np.random.randint(0, len(gene) - 1)
    gene[index1], gene[index2] = gene[index2], gene[index1]
    return gene

#--------------------------------------------------选择-----------------------------------------------------------------
def sum_list(l):
    r = 0
    for i in l:
        r += i
    return r

def random_select(pro):                                 #种群选择

    a=list(pro.values())
    r = random.random()
    b = list()
    for i in range(len(a)):
        b.append(sum_list(a[:i+1]))
    for i in range(len(b)):
        if i==0 and r<b[0]:
            k = list(pro.keys())[i]
            return k
        elif r>b[i] and r<b[i+1]:
            k = list(pro.keys())[i]
            return k

#——————————————————————————————————————————————————逻辑函数——————————————————————————————————————————————————————————————
def action():
    pop=Creat_pop(100)                               #产生一个100个染色体的种群，二维数组结构
    i=0
    #print(type(pop))
    while i<2:                                       #循环进化：
       # print(type(pop))
        popa = init_dict(pop)                        # 计算这一个种群中每一个染色体的适应值，成为了字典结构
        j=0                                          # 根据适应值从种群中再挑选100个染色体成为一个种群
        temp_pop = list()
        while j<100:
            temp_pop.append(random_select(popa))
            j=j+1

        r = random.random()
        if r < crossRate:                                 # 交叉产生后代
            temp_pop_cross = list()
            for s in range(len(temp_pop)):
                if s== len(temp_pop)-1:
                    parent1 = dict_to_list(temp_pop[s])
                    parent2 = dict_to_list(temp_pop[0])
                    temp_pop_cross.append(Cross(parent1, parent2))
                else:
                    parent1 = dict_to_list(temp_pop[s])
                    parent2 = dict_to_list(temp_pop[s + 1])
                    temp_pop_cross.append(Cross(parent1, parent2))
            temp_pop = temp_pop_cross

        r = random.random()                              #变异产生后代
        if r<mutationRate:
            temp_pop_mutation=list()
            for l in range(len(temp_pop)):
                temp_pop_mutation.append(temp_pop[l])
            temp_pop=temp_pop_mutation

        pop=final_pop(temp_pop,City)
        i=i+1


    popa = init_dict(pop)                                #计算进化后的pop适应值
    Results_the_path = max(popa,key=popa.get)            #挑选当前种群的最短路径
    print(Results_the_path)
    return Results_the_path




# ——————————————————————————————————————————————————主函数—————————————————————————————————————————————————————————————
if __name__ == '__main__':
    action()