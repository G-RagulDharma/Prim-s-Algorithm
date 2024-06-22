matrix=[]
c=0
n=int(input("Enter Number of Nodes :"))

for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    matrix.append(row)
for i in range(n):
    print(matrix[i])
while(c!=3):
    print()
    print("---------------MENU----------------")
    print("1. Insert ")
    print("2. Find MINIMUM SPANNING TREE")
    print("3. Exit ")
    print("-----------------------------------")
    print()
    c=int(input("Enter your choice : "))
    if(c==1):
        s=int(input("Enter Source        : "))
        des=int(input("Enter Destination   : "))
        d=int(input("Enter Distance      : "))
        matrix[s][des]=d
        print(" ",end=" ")
        for i in range(n):
            print("",i,end=" " )
        print(" ")
        for i in range(n):
            print(i,matrix[i])

    elif(c==2):
        inf=9999999
        selected=[0] 
        mst=[]
        for i in range(n-1): 
            minweight=inf
            a=0
            b=0
            for i in selected:
                for j in range(n):
                    nodej=0
                    for node in selected:
                        if node==j:
                            nodej=1
                            break
                    if (nodej==0  and matrix[i][j]>0):
                        if matrix[i][j] < minweight:
                            minweight=matrix[i][j]
                            a=i
                            b=j
            mst.append((a,b,minweight))
            selected.append(b)

        print("source - Destination : Weight")
        for edge in mst:
            print(edge[0] ,"     -    ", edge[1] ,"      : ",edge[2])
                  
        
