# 3)	Задан список слов, в которых встречается символ ‘_’  подчеркивание).
# Создать новый список, в котором символ подчеркивания в словах ‘_’ заменить символом ‘ ‘ (пробел).
# l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]


l = ["ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__"]
new_l = []
for word in l:
    if '_' in word:
        new_word = word.replace('_', ' ')
        new_l.append(new_word)
    else:
        new_l.append(word)
print(new_l)
