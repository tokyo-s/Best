path = "D:\\programming\\Python\\labirint\\labirint.txt"

k=0
z=0
count=0
xd=[]
x=[] 
with open(path,'r') as f:
    line = f.readline()
    while line:
        x.append(line)
        #print(line)
        line = f.readline()

for iy,i in enumerate(x):
    for ix,c in enumerate(i):
        if c == '$':
            col=ix
            row = iy

            print(row,col)
            row+=1
            c=0
            flag = ''
            k=0
            stiva = []
            while(c!='@'):
                c = x[row][col]
                if(c=='>'):
                    col1 = col
                    col1-=1
                    c=x[row][col1]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        col1-=1
                        c=x[row][col1]
                    k=k//10
                    col+=k
                    k=0
                    print(x[row][col])

                elif(c==']'):
                    stiva.append(x[row][col-1])
                    col-=2
                    print(x[row][col])

                elif(c=='^'):
                    row1 = row
                    row1+=1
                    c=x[row1][col]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        row1+=1
                        c=x[row1][col]
                    k=k//10
                    row-=k
                    k=0
                    print(x[row][col])

                elif(c==')'):
                    ch = stiva.pop()
                    flag = flag+ch
                    col1 = col
                    col1-=1
                    c=x[row][col1]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        col1-=1
                        c=x[row][col1]
                    k=k//10
                    col+=k
                    k=0
                    print(x[row][col])

                elif(c=='%'):
                    flag = flag[::-1]
                    row+=1
                    print(x[row][col])
                
                elif(c=='['):
                    stiva.append(x[row][col+1])
                    col+=2
                    print(x[row][col])

                elif(c=='('):
                    ch = stiva.pop()
                    flag = ch+flag
                    col1 = col
                    col1+=1
                    c=x[row][col1]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        col1+=1
                        c=x[row][col1]
                    k=k//10
                    col-=k
                    k=0
                    print(x[row][col])

                elif(c=='*'):
                    stiva.append(x[row-1][col])
                    row-=2
                    print(x[row][col])

                elif(c=='<'):
                    col1 = col
                    col1+=1
                    c=x[row][col1]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        col1+=1
                        c=x[row][col1]
                    k=k//10
                    col-=k
                    k=0
                    print(x[row][col])
                
                elif(c=='v'):
                    row1 = row
                    row1-=1
                    c=x[row1][col]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        row1-=1
                        c=x[row1][col]
                    k=k//10
                    row+=k
                    k=0
                    print(x[row][col])
                
                elif(c=='.'):
                    stiva.append(x[row+1][col])
                    row+=2
                    print(x[row][col])

                elif(c=='-'):
                    flag=flag[1:]
                    row1 = row
                    row1+=1
                    c=x[row1][col]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        row1+=1
                        c=x[row1][col]
                    k=k//10
                    row-=k
                    k=0
                    print(x[row][col])

                elif(c=='+'):
                    flag=flag[:-1]
                    row1 = row
                    row1-=1
                    c=x[row1][col]
                    while(c>='0' and c<='9'):
                        k+=int(c)
                        k*=10
                        row1-=1
                        c=x[row1][col]
                    k=k//10
                    row+=k
                    k=0
                    print(x[row][col])
                elif(c=='#'):
                    xd.append("error")

            xd.append(flag)
print(xd)

