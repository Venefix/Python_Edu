def solve(equ):
        pparam = 0
        psol = []
        tttsol = []
        ttsol = []
        tsol = []
        sol = []
        for n in range(len(equ)):
            sym = equ[n]
            if sym == '(':
                pparam = 1
            elif sym == ')':
                pparam = 0
                solution = solve(psol)
                ttsol.append(solution)
            else:
                if pparam == 0:
                    ttsol.append(sym)
                elif pparam == 1:
                    psol.append(sym)
        for n in range(len(ttsol)):
            sym = ttsol[n]
            if ttsol[n - 1] == '*' and ttsol[n - 2] == '*':
                delete = tttsol.pop()
                delete2 = tttsol.pop()
                delete3 = tttsol.pop()
                pow = float(ttsol[n - 3]) ** float(sym)
                tttsol.append(pow)
            elif ttsol[n - 1] == '^':
                delete = tttsol.pop()
                delete2 = tttsol.pop()
                pow = float(ttsol[n - 2]) ** float(sym)
                tttsol.append(pow)
            else:
                tttsol.append(sym)
        for n in range(len(tttsol)):
            ssym = tttsol[n]
            if tttsol[n - 1] == '*':
                delete = tsol.pop()
                prod = float(tsol.pop()) * float(ssym)
                tsol.append(prod)
            elif tttsol[n - 1] == '/':
                delete = tsol.pop()
                div = float(tsol.pop()) / float(ssym)
                tsol.append(div)
            else:
                tsol.append(ssym)
        for n in range(len(tsol)):
            sssym = tsol[n]
            if tsol[n - 1] == '+':
                delete = sol.pop()
                sum = float(sol.pop()) + float(sssym)
                sol.append(sum)
            elif tsol[n - 1] == '-':
                delete = sol.pop()
                diff = float(sol.pop()) - float(sssym)
                sol.append(diff)
            else:
                sol.append(sssym)
        solution = sol.pop()
        return solution

def checkfloat(n):
    try:
        float(n)
        return True
    except:
        return False

def split(input):
    symbols = ['+', '-', '*', '/', '(', ')', '^']
    eqs = []
    comb = 0
    sol = []
    nums = []
    eqs = []
    neqs = []
    for n in range(len(input)):
        temp = input[n]
        if temp == ' ':
            delete = temp
        elif temp == '\n':
            delete = temp
        else:
            sol.append(temp)
    for n in range(len(sol)):
        ttemp = sol[n]
        try:
            if n == (len(sol) - 1):
                num = float(ttemp)
                nums.append(ttemp)
                nnum = ''.join(nums)
                eqs.append(nnum)
            else:
                num = float(ttemp)
                nums.append(ttemp)
                comb = 1
        except:
            if comb == 1:
                nnum = ''.join(nums)
                eqs.append(nnum)
                eqs.append(ttemp)
                nums = []
                comb = 0
            else:
                eqs.append(ttemp)
                comb = 0
    for n in range(len(eqs)):
        tneg = eqs[n]
        if eqs[n - 1] == '-' and eqs[n - 2] in symbols:
            nneg = [eqs[n - 1], tneg]
            delete = neqs.pop()
            neg = ''.join(nneg)
            neqs.append(neg)
        elif eqs[n - 1] == '.':
            vtest = checkfloat(eqs[n - 2])
            if vtest == True:
                tdec = [eqs[n - 2], eqs[n - 1], tneg]
                delete = neqs.pop()
                delete2 = neqs.pop()
                dec = ''.join(tdec)
                neqs.append(dec)
            else:
                tdec = [eqs[n - 1], tneg]
                delete = neqs.pop()
                dec = ''.join(tdec)
                neqs.append(dec)
        else:
            neqs.append(tneg)
    return neqs

filename = raw_input('Enter file name: ')
try:
    Input = open(filename, 'r')
    Output = open('Output.txt', 'w')
    try:
        for line in Input:
            eqs = split(line)
            solution = solve(eqs)
            Output.write("%s\n" % solution)
    except:
        print('There was an error while reading this line: ' + line)
    Output.close()
    Input.close()

except:
    print('This file or file name is not valid.')