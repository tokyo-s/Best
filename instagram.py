path = "D:\\programming\\Python\\ig.txt"

collection=[]
with open(path, 'r') as f:
    line = f.readline()
    while line:
        st=''
        st1=''
        flag = False
        for c in line:
            if not flag:
                st+=c
            else: st1+=c
            if c==':': flag = True
        collection.append((st,st1[:-1]))
        line = f.readline()

print(collection)

def value(r):
 
    if (r == 'I'):
        return 1
 
    if (r == 'V'):
        return 5
 
    if (r == 'X'):
        return 10
         
    if (r == 'L'):
        return 50
 
    if (r == 'C'):
        return 100
 
    if (r == 'D'):
        return 500
 
    if (r == 'M'):
        return 1000
 
    return -1
 
def romanToDecimal(st):
 
    res = 0
 
    i = 0
    while i < len(st):
 
        s1 = value(st[i])
 
        if (i + 1 < len(st)):
 
            s2 = value(st[i + 1])
 
            if (s1 >= s2):
 
                res = res + s1
             
            else :
 
                res = res + s2 - s1
                i += 1
         
        else :
            res = res + s1
             
        i += 1
     
    return res
 
def sortArr(arr, n,keys):
 
    vp = {}
    answer = [0]*len(keys)
    for i in range(n):
        p = romanToDecimal(arr[i]) 
        answer[p] = keys[i]
        vp[p] = arr[i]
 
    for i in sorted(vp):
        print(vp[i], i+1)

    return answer
 
romans = []
keys=[]
for x,y in collection:
    romans.append(x)
    keys.append(y)

n = len(romans)

answer = sortArr(romans, n,keys)
answer = ''.join(answer).replace(" ",'')
print(answer)