n=int(input("enter the number of rows: "))
row1=[1]
mainlist=[]


for row in range(n):
    
    row2=[1]
    mainlist.append(row1)
    for charindex in range(len(row1)):
        if charindex==(len(row1)-1):
            row2.append(1)
            
        else:
            row2.append(row1[charindex]+row1[charindex+1])

    row1=row2




lastrow=mainlist[-1]
startstring=" "
for element in lastrow:
    startstring+=str(element) + " "


length=len(startstring)

string=" "
for row in mainlist:
    for element in row:
        string+=str(element) + " "
    string=string.center(length)
    print(string)
    string=" "