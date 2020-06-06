
Map = {}

g_dict_shifts = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5],
                 3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
                 6:[3,7],  7:[4,6,8], 8:[5,7]}

def swap(a, i, j):
    if i > j:
        i, j = j, i
    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
    return b

def step_number(Layout):
    sum = 0
    for i in range(1, 9):
        for j in range(0, i):
            if Layout[j] > Layout[i] and Layout[i] != '0':     # 0是false,'0'才是数字
                sum = sum + 1
    return sum

def action(srcLayout, destLayout):
    src = step_number(srcLayout)
    dest = step_number(destLayout)
#判断是否可以达到目标条件
    if (src%2)!=(dest%2):
        return -1, None

	#初始化字典
    Map[srcLayout] = -1
    OPen = []
    OPen.append(srcLayout)#当前状态存入列表

    while len(OPen) > 0:
        temp = OPen.pop(0)#出栈
        if temp == destLayout:#判断当前状态是否为目标状态
            break

        # 寻找0 的位置。
        ind_slide = temp.index("0")
        lst_shifts = g_dict_shifts[ind_slide]                        #当前可进行交换的位置集合
        for nShift in lst_shifts:
            newLayout = swap(temp, nShift, ind_slide)           #交换位置

            if Map.get(newLayout) == None:#判断交换后的状态是否已经查询过
                Map[newLayout] = temp
                OPen.append(newLayout)#存入集合

    Close = []
    Close.append(temp)
    while Map[temp] != -1:#存入路径
        temp = Map[temp]
        Close.append(temp)
    Close.reverse()
    return 0, Close


if __name__ == "__main__":
	#测试数据输入格式
    srcLayout  = "541203786"
    destLayout = "123804765"

    flag, Close = action(srcLayout, destLayout)
    if flag != 0:
        print("目标布局不可达")
    else:
        for Index in range(len(Close)):
            print("第" + str(Index + 1)+"步：")
            print(Close[Index][:3])
            print(Close[Index][3:6])
            print(Close[Index][6:])

