f=open("/Users/izaz/Documents/PythonFiles/Monthlyreport.txt",'r')
a=[]
for i in f:
    b=[]
    for words in i.split(","):
        c=[]
        b.append(list(words))
    a.append(b)
# print(a)
for i in range(len(a)):

    for j in range(len(a[0])):
        if("\n" in a[i][j]):
            a[i][j].remove("\n")
    # print(a[i])
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]="".join(a[i][j])
print(a)
p=0
for i in range(len(a[0])):
    if(a[0][i]=="Amount"):
        p=i
spending=0
for i in range(1,len(a)):
    a[i][p]=int(a[i][p])
TotalErned=0
TotalSpent=0
for i in range(1,len(a)):
    if(a[i][p]>0):
        TotalErned=TotalErned+a[i][p]
    else:
        
        TotalSpent=TotalSpent+a[i][p]
print(TotalErned)
print(TotalSpent)
