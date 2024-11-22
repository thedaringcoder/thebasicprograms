triangle = []

last_row = []

row_num = int(input("Row"))

for i in range(1, row_num):
    row = []
    row.append(1)

    if i > 2:
        member_index = 0
        
        for each_member in last_row:
            if not (member_index + 1) == len(last_row):
                row.append(last_row[member_index] + last_row[member_index + 1])
            
            member_index += 1
    
    if not i == 1:
        row.append(1)

    triangle.append(row)

    last_row = row

print(triangle)