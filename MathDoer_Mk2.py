filename = raw_input('Enter file name:')
try:
    Input = open(filename, 'r')
    Output = open('Output.txt', 'w')
    for line in Input:
        try:
            eq = line
            equ = eq.split()
            tsol = []
            sol = []
            for n in range(len(equ)):
                sym = equ[n]
                if equ[n - 1] == '*':
                    delete = tsol.pop()
                    prod = int(tsol.pop()) * int(sym)
                    tsol.append(prod)
                elif equ[n - 1] == '/':
                    delete = tsol.pop()
                    div = int(tsol.pop()) / int(sym)
                    tsol.append(div)
                else:
                    tsol.append(sym)
            for n in range(len(tsol)):
                ssym = tsol[n]
                if tsol[n-1] == '+':
                    delete = sol.pop()
                    sum = int(sol.pop()) + int(ssym)
                    sol.append(sum)
                elif tsol[n-1] == '-':
                    delete = sol.pop()
                    diff = int(sol.pop()) - int(ssym)
                    sol.append(diff)
                else:
                    sol.append(ssym)
            outp = sol.pop()
            Output.write("%s\n" % outp)
        except:
            print('There was an error while reading this line: ' + line)
    Output.close()
    Input.close()

except:
    print('This file or file name is not valid.')