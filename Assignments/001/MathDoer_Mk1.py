filename = raw_input('Enter file name')
Input = open(filename, 'r');
Output = open('Output.txt', 'w')
for line in Input:
    eq = line
    sol = eval(eq)
    Output.write("%s\n" % sol)

Output.close()
Input.close()
