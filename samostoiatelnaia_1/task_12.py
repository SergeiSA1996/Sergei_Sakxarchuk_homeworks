# 12.	В классе N школьников. На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь».
# Выведите, что скажут ученики.
# Входные данные: Вводится одно целое число — количество человек в классе.
# Входные данные: Выведите последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.


ych_v_class = int(input('Количество учеников в классе: '))
for i in range(ych_v_class):
    if i < ych_v_class - 1:
        print(('Первый!', 'Второй!')[i % 2])
    else:
        print(('Первый!', 'Второй!')[i % 2] + ' Расчет окончен!')
