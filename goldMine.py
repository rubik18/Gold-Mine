
import time
import matplotlib.pyplot as plt

def formatData(a):
    for i in a.keys():
        k=[]
        for j in range(7):
            m = int(a[i][j])/100
            k.append(m)
        a[i]=k
    return a
# loi nhuan thu duoc khi co k cong nhan
def profit(li, k):
    cost = 0
    for i in range(7):
        if k < i:
            cost += li[i] * 60 * k
        else:
            cost += li[i] * (50 * i - 20 * (k - i))
    return cost
# loi nhuan trong tat ca cac truong hop
def profitAll(dic):
    result = {}
    for k in range(1,len(dic)+1):
        result[k]=[]
    for i in dic.keys():
        li = []
        for j in range(0,7):
            m = profit(dic[i],j)
            li.append(m)
        result[i] = li
    return result

#loi nhuan thu duoc khi them 1 cong nhan
def profitIncre (dic):
    for i in dic.keys():
        li = []
        li.append(dic[i][0])
        li.append(dic[i][1])
        for j in range(2,7):
            m = dic[i][j]-dic[i][j-1]
            li.append(m)
        dic[i] = li
    return dic


#ham tham thuc hien them cn vao lan luot cac mo
def greed(data,k):
    gi = formatData(data)
    re1 = profitAll(gi)
    # print(re1)
    dic = profitIncre(re1)
    # print(dic)
    sum = 0
    result = {}
    for m in range(1, len(dic) + 1):
        result[m] = 0
    # print("result",result)
    for i in dic.keys():
        dic[i].pop(0)
    # print("result", result)
    for h in range(1,k+1):
        # print(h,dic)
        maxx = max(dic[i][0] for i in dic.keys())
        sum += maxx
        # print(sum)
        for i in dic.keys():
            if dic[i][0] == maxx:
                result[i] += 1
                # print(result)
                dic[i].pop(0)
                # print(i,dic[i])
                if len(dic[i])==0:
                    del dic[i]
                break

    return sum, result


#test01----------------------------------------------
g1 ={1:['000', '030', '030', '040', '000', '000', '000'], 2: ['020', '020', '020', '010', '010', '010', '010']}
k1 = 4
#test02-------------------------------------------------------------
g2 = {}
for i in range(1,6):
    g2[i] = ['100', '000', '000', '000', '000', '000', '000']
# print(g2)
k2 = 8
#test03-----------------------------------------------------------
g3 = {}
for i in range(1,11):
    g3[i] = ['050', '000', '000', '000', '000', '050', '000']
# print(g3)
k3 = 30
#test04---------------------------------------------------------
g4 = {}
for i in range(1,51):
    g4[i] = ['026', '012', '005', '013', '038', '002', '004']
k4 = 56
#test05--------------------------------------------------------
g55 = ["100, 000, 000, 000, 000, 000, 000",
  "090, 010, 000, 000, 000, 000, 000",
  "080, 020, 000, 000, 000, 000, 000",
  "075, 025, 000, 000, 000, 000, 000",
  "050, 050, 000, 000, 000, 000, 000",
  "025, 075, 000, 000, 000, 000, 000",
  "020, 080, 000, 000, 000, 000, 000",
  "010, 090, 000, 000, 000, 000, 000",
  "000, 100, 000, 000, 000, 000, 000",
  "000, 090, 010, 000, 000, 000, 000",
  "000, 080, 020, 000, 000, 000, 000",
  "000, 075, 025, 000, 000, 000, 000",
  "000, 050, 050, 000, 000, 000, 000",
  "000, 025, 075, 000, 000, 000, 000",
  "000, 020, 080, 000, 000, 000, 000",
  "000, 010, 090, 000, 000, 000, 000",
  "000, 000, 100, 000, 000, 000, 000",
  "000, 000, 090, 010, 000, 000, 000",
  "000, 000, 080, 020, 000, 000, 000",
  "000, 000, 075, 025, 000, 000, 000",
  "000, 000, 050, 050, 000, 000, 000",
  "000, 000, 025, 075, 000, 000, 000",
  "000, 000, 020, 080, 000, 000, 000",
  "000, 000, 010, 090, 000, 000, 000",
  "000, 000, 000, 100, 000, 000, 000",
  "000, 000, 000, 100, 000, 000, 000",
  "000, 000, 000, 090, 010, 000, 000",
  "000, 000, 000, 080, 020, 000, 000",
  "000, 000, 000, 075, 025, 000, 000",
  "000, 000, 000, 050, 050, 000, 000",
  "000, 000, 000, 025, 075, 000, 000",
  "000, 000, 000, 020, 080, 000, 000",
  "000, 000, 000, 010, 090, 000, 000",
  "000, 000, 000, 000, 100, 000, 000",
  "000, 000, 000, 000, 090, 010, 000",
  "000, 000, 000, 000, 080, 020, 000",
  "000, 000, 000, 000, 075, 025, 000",
  "000, 000, 000, 000, 050, 050, 000",
  "000, 000, 000, 000, 025, 075, 000",
  "000, 000, 000, 000, 020, 080, 000",
  "000, 000, 000, 000, 010, 090, 000",
  "000, 000, 000, 000, 000, 100, 000",
  "000, 000, 000, 000, 000, 090, 010",
  "000, 000, 000, 000, 000, 080, 020",
  "000, 000, 000, 000, 000, 075, 025",
  "000, 000, 000, 000, 000, 050, 050",
  "000, 000, 000, 000, 000, 025, 075",
  "000, 000, 000, 000, 000, 020, 080",
  "000, 000, 000, 000, 000, 010, 090",
  "000, 000, 000, 000, 000, 000, 100" ]
g5 = {}
for i in range(0,len(g55)):
    a = g55[i].split()
    ls = []
    for j in a:
        m = j.rstrip(',')
        ls.append(m)
    g5[i+1]=ls
k5 = 150

n =[2,5,10,50]
timeee = []

start_time = time.time()
pf, re = greed(g1,k1)
print("Test01")
print('----------------------------------')
print("Tong loi nhuan: ",pf)
print("Phan cong: ",re)
end_time = time.time()
tim=(end_time - start_time) * 1000
timeee.append(tim)

start_time2 = time.time()
pf2, re2 = greed(g2,k2)
print("Test02")
print('----------------------------------')
print("Tong loi nhuan: ",pf)
print("Phan cong: ",re)
end_time2 = time.time()
tim2=(end_time2 - start_time2) * 1000

timeee.append(tim2)

start_time3 = time.time()
pf3, re3 = greed(g3,k3)
print("Test03")
print('----------------------------------')
print("Tong loi nhuan: ",pf)
print("Phan cong: ",re)
end_time3 = time.time()
tim3=(end_time3 - start_time3) * 1000
timeee.append(tim3)

start_time4 = time.time()
pf4, re4 = greed(g4,k4)
print("Test04")
print('----------------------------------')
print("Tong loi nhuan: ",pf)
print("Phan cong: ",re)
end_time4 = time.time()
tim4=(end_time4 - start_time4) * 1000
timeee.append(tim4)

start_time = time.time()
pf, re = greed(g5,k5)
print("Test05")
print('----------------------------------')
print("Tong loi nhuan: ",pf)
print("Phan cong: ",re)
end_time = time.time()
timee=(end_time - start_time) * 1000
print(timee)

print(timeee)

p2, = plt.plot(n, timeee, 'r.-')
plt.title('Sự thay đổi thời gian thực hiện theo kích cỡ dữ liệu đầu vào')
plt.xlabel('N')
plt.ylabel('Time (seconds) ')
# plt.savefig('goldMine.png')
plt.show()
