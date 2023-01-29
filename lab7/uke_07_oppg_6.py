first_line = input()
rows,cols = first_line.split(" ")
rows = int(rows)
cols = int(cols)

tt = []
for row in range(rows):
    line = input()
    split_line = line.split(" ")
    split_line_number = []
    for str_item in split_line:
        num_item = int(str_item)
        split_line_number.append(num_item)
    tt.append(split_line_number)

tf = []
for row in range(rows):
    tf.append([]*cols)

# regn ut første kolonne først
for row in range(rows):
    if row != 0:
        tf [row][0] = tf[row-1][0] + tt[row][0]
    else:
        tf[row][0] = tt[row][0]

# regner ut første rad
for col in range(1,cols):
    tf[0][col] = tf[0][col-1] + tt[0][col]

for row in range(1, rows):
    for col in range(1, cols):
        tf[row][col] = max(tf[row-1][col], tf[row][col-1]+ tt[row][col])

for row in range(rows):
    x = tf[row][-1]
    print(x,end=" ")
    