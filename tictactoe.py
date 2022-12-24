print('Вводите координаты через пробел\nсначала указывается вертикальная координата, затем горизонтальная')

field=[['.']*3 for _ in range(3)]
def display(field_):
    line = '  1  2  3'
    print(line)
    for row, i in zip(field_, line.split(  )):
        print(i, '  '.join(str(j) for j in row))

def game_input(turn_, field_):
    while True:
        print('Ходит', turn_, ': ')
        sign = input().split()
        if len(sign) != 2:
            print('Введите две координаты через пробел')
            continue
        if not ((sign[0].isdigit() and sign[1].isdigit()) and \
                (1<=int(sign[0])<=3 and 1<=int(sign[1])<=3)):
            print('Введите числовые координаты от 1 до 3 через пробел')
            continue
        x, y = map(int, sign)
        # if not
        #     print('Введите числовые координаты от 1 до 3 через пробел')
        #     continue
        if field_[x-1][y-1] != '.':
            print('Клетка занята')
            continue
        break
    return x-1, y-1

def win(field_, turn_):
    win_cond = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)),)
    for coord in win_cond:
        xo = []
        for symbol in coord:
            xo.append(field_[symbol[0]][symbol[1]])
        if xo == [turn_, turn_, turn_]:
            return True
    return False

def game(field_):
    count = 0;
    while True:
        display(field_)
        if count % 2 == 0:
            turn = 'X'
        else: turn = 'O'
        if count<9:
            x, y = game_input(turn, field_)
            field[x][y] = turn

        elif count==9:
            print ('Ничья!')
            break
        if win(field_,turn):
            print("Выйграл ", turn)
            display(field_)
            break
        count+=1
game(field)