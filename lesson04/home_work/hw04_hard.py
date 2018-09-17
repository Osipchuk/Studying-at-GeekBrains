import re

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
print('Задание-1:')
print('matrix_rotate = {}\n'.format(list(map(list, zip(*matrix)))))

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


def composition(num):
    comp = 1
    for i in num:
        comp *= int(i)
    return comp


print('Задание-2:')
number = re.sub(r'\n', '', number)
max_comp = 0
for i in range(len(number) - 4):
    comp = 1
    numbers = re.match(r'\d{5}', number).group()
    comp = composition(numbers)
    if comp > max_comp:
        max_num = numbers
        max_comp = comp
        max_i = i
    max_comp = max(max_comp, comp)
    number = number[1:]
print('Максимальное произведение получится из последовательности 5 чисел "{}"\n'
      'Оно будет равно {}\nКоординаты чисел [{}:{}]\n'.format(max_num, max_comp, max_i, max_i + 5))

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
print('\nЗадание-3:')
figures1 = [[1, 7], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
figures2 = [[1, 7], [2, 6], [3, 2], [4, 8], [5, 4], [6, 1], [7, 3], [8, 5]]
figures3 = [[3, 2], [5, 6], [1, 7], [4, 8], [2, 4], [6, 1], [7, 3], [8, 5]]
figures4 = [[1, 8], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]


def queens(figures):
    hor = [0 for _ in range(0, 9)]  # индикатор ферзей на одной горизонтали
    ver = [0 for _ in range(0, 9)]  # индикатор ферзей на одной вертикали
    d_right = [0 for _ in range(0, 15)]  # индикатор ферзей на "правых" диагоналях
    # для фигур на одной "правой" диагонали совпадают разности координат (от -7 до 7)
    d_left = [0 for _ in range(0, 15)]  # индикатор ферзей на "левых" диагоналях
    # для фигур на одной "правой" диагонали совпадают суммы координат (от 2 до 16)
    for queen in figures:  # при попадании фигуры на линию индикатор увеличивается на 1
        hor[queen[0]] += 1
        ver[queen[1]] += 1
        d_right[(queen[1] - queen[0] + 7)] += 1
        d_left[(queen[1] + queen[0] - 2)] += 1

    if max(hor) > 1 or max(ver) > 1 or max(d_right) > 1 or max(d_left) > 1:
        return 'Ферзи бью друг друга'
    return 'Ферзи нигде не пересекаются'


print('Координаты ферзей: {}\n{}'.format(figures1, queens(figures1)))
print('Координаты ферзей: {}\n'.format(figures2, queens(figures2)))
print('Координаты ферзей: {}\n'.format(figures3, queens(figures3)))
print('Координаты ферзей: {}\n'.format(figures4, queens(figures4)))
