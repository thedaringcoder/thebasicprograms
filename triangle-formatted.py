row_num = int(input("Row"))


def prepare_triangle_matrix(num_of_rows: int):
    triangle = []
    last_row = []

    for i in range(1, num_of_rows):
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

    return triangle

def format_triangle(matrix, max_row_member):
    format_length = (max_row_member * 2) - 1

    triangle_string = ""
    
    row_num = 1

    for each_row in matrix:
        triangle_string += " " * (max_row_member - row_num)
        for each_member in each_row:
            triangle_string += (str(each_member) + " ")
        
        triangle_string += "\n"

        row_num += 1
    
    
    print(triangle_string)


format_triangle(prepare_triangle_matrix(row_num), row_num)