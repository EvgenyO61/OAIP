# Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
# неравенства A > 0 или B < —2».
while True:
    try:
        a = int(input('введите число a:'))
        b = int(input('Введите число b:'))
        break
    except ValueError:
        print(" ")
        print("Числа не целые")


if a > 0:
    print('Высказывание a > 0 истинно')
else:
    print('Высказывание ложно')
if b < -2:
    print('Высказывание b истинно')
else:
    print('Высказывание b < -2 ложно')
