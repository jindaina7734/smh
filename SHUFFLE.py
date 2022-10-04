mm = str(input())
m = mm.split()
n = int(m[0])
k = int(m[1])
x = int(m[2])
lst = []

for i in range(1,n+1):
    lst.append(i)
    
for ii in range(x):
    stt = str(input())
    st = stt.split()
    i = int(st[0])
    mmm = int(st[1])
    j = int(st[2])
    
    lst01 = []
    for iii in range(i-1, i+mmm-1):
        xx = lst.pop(i-1)
        lst01.append(xx)
    trc = j-1
    for jjj in range(len(lst01)):
        lst.insert(trc,lst01[jjj])
        trc+=1

text = ''
for iii in range(k):
    print(lst[iii], end = " " )

        
