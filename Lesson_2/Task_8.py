""" Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра, которую
 необходимо посчитать, задаются вводом с клавиатуры."""

def calc():
    num_str = input('Введите последовательность чисел через пробел')
    dig = input('Введите цыфру которую нужно найти ')
    result = num_str.count(dig)
    print(result)
def main():
    calc()

if __name__ == '__main__':
    main()