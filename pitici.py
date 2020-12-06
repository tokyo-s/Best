x = int(input())
a=[]
b=[]
print("introduce nr de kg cu care slabeste la fiecare casa")
for i in range(x):
    a.append(int(input()))
print("introduce nr de kg cu care care vrea sa slabeasca fiecare pitic")
for i in range(x):
    b.append(int(input()))

answ = [0] * x

for i in range(x):
    k=i
    while(b[i]>0 and k!=x ):
        b[i]-=a[k]
        answ[k]+=1
        k+=1

print(max(answ),answ.count(max(answ)))




