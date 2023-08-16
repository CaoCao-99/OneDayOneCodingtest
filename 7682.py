
line_check = [[0,1,2],[3,4,5],[6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8],[2,4,6]]
def counting(data):
    o = data.count('O')
    x = data.count('X')
    if 0 == x-o:
        return 0
    elif  x-o == 1:
        return 1
    else:
        return 2


def line(data):
    O,X = 0,0
    for a,b,c in line_check:
        if data[a] ==data[b] == data[c]:
            if data[a] == 'X':
                X+=1
            elif data[a] == 'O':
                O+=1
    return O,X

while True:
    now = input()
    if now == 'end':
        break
    c = counting(now)
    O,X = line(now)
    if O >=1 and X >=1 or c==2:
        print('invalid')
        continue
    else:
        if c == 0:
            if '.' in now and O == 1 and  X == 0:
                print('valid')
            else:
                print('invalid')
        elif c == 1:
            if '.' in now:
                if X == 1 and O == 0:
                    print('valid')
                else:
                    print('invalid')
            else:
                if O == 0 and X <= 2:
                    print('valid')
                else:
                    print('invalid')

