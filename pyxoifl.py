# Open (read mode) the 'output' polar file from Xfoil and the 'dump' file where the Cl vs. α data is going to be written.
xfoil_file = open('output', 'r')
dump_file = open('py_output.txt', 'w')

# Skip the header of the Xfoil read file
xfoil_file.seek(431)
# Read the first line and strip the end as well as the spaces
xfoil_content = xfoil_file.readline().strip(' \n')

# Create a new list 'result' and append the red line to it
result=[]
result.append(xfoil_content.split('  '))

# Iterate through the file reading each line and appending it to the 'result' list
while xfoil_content:
    xfoil_content = xfoil_file.readline().strip(' \n')
    result.append(xfoil_content.split('  '))

# Close the Xfoil file
xfoil_file.close()

# Delete the last item from the result list which happens to be an empty string
del result[-1]

# Write only the two first positions of each item in the 'result' list to the 'dump' file
for x in result:
    print(x[0], x[1])
    dump_file.write(x[0] + ' ')
    dump_file.write(x[1] + '\n')
