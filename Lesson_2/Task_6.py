"""В программе генерируется случайное целое число от 0 до 100. Пользователь
 должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки
  должно сообщаться больше или меньше введенное пользователем число,
  чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""
import random
def game():
    num = random.randint(1, 100)
    i = 0
    while i <= 10:
        tries = 10 - i
        answer = int(input(f'Я загадал число от 1 до 100. Пропробуйте его угадать за 10 попыток. Осталось {tries} попыток '))
        if answer == num:
            print(f'Вы угадали за {i} попыток. Ура')
            break
        elif answer < num:
            print(f'Ваш ответ меньше числа ')
        elif answer > num:
            print(f'Ваш ответ ,больше числа ')
        i = i + 1
        if i == 10:
            print(f'Вы проиграли. Это было число {num} ')
            break

def main():
    game()

if __name__ == '__main__':
    main()