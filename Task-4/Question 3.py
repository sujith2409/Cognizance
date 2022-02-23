print("TO PRINT A TABLE AND DISPLAYING A PARTICULAR ROW")
n=int(input('Enter The Number of Students : '))
l=[['Roll No','Name','Marks']]
for i in range(n):
    a=input("Enter the Roll Number of the Student:")
    b=input("Enter the Name of the Student:")
    c=int(input("Enter the Marks:"))
    l.append([a,b,c])
for i in range(len(l)):
    for j in range(len(l[i])):
        k=l[i][j]
        print(k,end='\t')
    print('\n')
x=int(input("Enter the Roll Number to Print that Row:"))
for i in l[x]:
    print(i,end='\t')
