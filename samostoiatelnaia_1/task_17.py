# Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
# «G».Вам нужно вернуть другую дополнительную сторону. Нить
# ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
#
# “АТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"


mydna = "ATCGT"
res = ""
for dn in mydna:
    if dn == "A":
        res += "T"
    elif dn == "T":
        res += "A"
    elif dn == "C":
        res += "G"
    elif dn == "G":
        res += "C"
print(res)