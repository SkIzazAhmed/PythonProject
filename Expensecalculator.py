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
# print(a)



p=0



for i in range(len(a[0])):
    if(a[0][i]=="Amount"):
        p=i
spending=0
for i in range(1,len(a)):
    a[i][p]=int(a[i][p])




TotalErned=0


TotalSpent=0


expense=[]



spend=[]



for i in range(1,len(a)):
    if(a[i][p]>0):
        TotalErned=TotalErned+a[i][p]
    else:
        spend.append(abs(TotalSpent))
        TotalSpent=TotalSpent+a[i][p]
    expense.append(abs(a[i][p]))



max1=max(spend)


index1=expense.index(max1)


print(" ")
print("Total Earned : ",TotalErned)
print(" ")


print("Total Spent : ",TotalSpent)
print(" ")

print("Date \t\t Type \t Expense")
print(a[index1+1][0],"\t",a[index1+1][1],"\t",a[index1+1][2])
print(" ")