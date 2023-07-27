# 3)	Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной доски,
# определите, может ли король попасть с первой клетки на вторую одним ходом.
# Пример
# Cell 1 coordinates:
# 4, 4
# Cell 2 coordinated:
# 5, 5
# YES
# Конь
# Определите, может ли конь попасть с первой клетки на вторую одним ходом.
# Ладья
# Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Ферзь
# Определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
# Слон
# определите, может ли слон попасть с первой клетки на вторую одним ходом.


def can_king_move(cell1, cell2):
    if abs(cell1[0] - cell2[0]) <= 1 and abs(cell1[1] - cell2[1]) <= 1:
        return True
    else:
        return False


def can_knight_move(cell1, cell2):
    if abs(cell1[0] - cell2[0]) == 2 and abs(cell1[1] - cell2[1]) == 1:
        return True
    elif abs(cell1[0] - cell2[0]) == 1 and abs(cell1[1] - cell2[1]) == 2:
        return True
    else:
        return False


def can_rook_move(cell1, cell2):
    if cell1[0] == cell2[0] or cell1[1] == cell2[1]:
        return True
    else:
        return False


def can_queen_move(cell1, cell2):
    if can_rook_move(cell1, cell2) or abs(cell1[0] - cell2[0]) == abs(cell1[1] - cell2[1]):
        return True
    else:
        return False


def can_bishop_move(cell1, cell2):
    if abs(cell1[0] - cell2[0]) == abs(cell1[1] - cell2[1]):
        return True
    else:
        return False


cell1 = (4, 4)
cell2 = (5, 5)

if can_king_move(cell1, cell2):
    print("Король может попасть с первой клетки на вторую одним ходом")
else:
    print("Король не может попасть с первой клетки на вторую одним ходом")

if can_knight_move(cell1, cell2):
    print("Конь может попасть с первой клетки на вторую одним ходом")
else:
    print("Конь не может попасть с первой клетки на вторую одним ходом")

if can_rook_move(cell1, cell2):
    print("Ладья может попасть с первой клетки на вторую одним ходом")
else:
    print("Ладья не может попасть с первой клетки на вторую одним ходом")

if can_queen_move(cell1, cell2):
    print("Ферзь может попасть с первой клетки на вторую одним ходом")
else:
    print("Ферзь не может попасть с первой клетки на вторую одним ходом")

if can_bishop_move(cell1, cell2):
    print("Слон может попасть с первой клетки на вторую одним ходом")
else:
    print("Слон не может попасть с первой клетки на вторую одним ходом")
