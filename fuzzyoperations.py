print("\tOperations on Fuzzy Set")
print("\t-----------------------")


def insert():
    global n,A,B
    n = int(input("\nEnter number of elements : "))
    A = []
    B = []
    print("Enter elements for A:") 
    for i in range(0, n): 
        ele = float(input()) 
        A.append(ele)
    print("Enter elements for B:") 
    for i in range(0, n): 
        ele = float(input()) 
        B.append(ele)
    print("A = {"+str(A)[1:-1]+"}")
    print("B = {"+str(B)[1:-1]+"}")
    return


def union():
    union = []
    for i in range(0,n):
        union.append(max(A[i],B[i]))
    print("\n  A U B = {"+str(union)[1:-1]+"}")
    return


def intersection():
    inter = []
    for i in range(0,n):
        inter.append(min(A[i],B[i]))
    print("  A intersection B = {"+str(inter)[1:-1]+"}")
    return


def A_complement():
    A_comp = []
    for i in range(0,n):
        A_comp.append(1-A[i])
    print("  A' = {"+str(A_comp)[1:-1]+"}")
    return


def B_complement():
    global B_comp
    B_comp = []
    for i in range(0,n):
        B_comp.append(1-B[i])
    print("  B' = {"+str(B_comp)[1:-1]+"}")
    return


def difference():
    diff = []
    for i in range(0,n):
        diff.append(min(A[i],B_comp[i]))
    print("  A - B = {"+str(diff)[1:-1]+"}")
    return


op=1
while(op!=6):
    print("\n\tMenu:\n1 -> Insert Sets\n2 -> Union\n3 -> Intersection\n4 -> Complement\n5 -> Difference\n6 -> Exit\n")
    print("Enter Your Choice: ")
    ch=int(input())
    if ch==1:
        insert()
    elif ch==2:
        union()
    elif ch==3:
        intersection()
    elif ch==4:
        A_complement()
        B_complement()
    elif ch==5:
        difference()
    elif ch==6:
        break
    else:
        print("Wrong Choice!")
        continue
    
