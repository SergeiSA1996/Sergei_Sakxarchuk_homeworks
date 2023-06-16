#Ваша задача состоит в том , чтобы преобразовать строки в то, как они были написаны Джейденом Смитом.
# Строки являются настоящими цитатами Джейдена Смита, но они не написанны с заглавной буквы так ,
# как он изначально их напечатал.


def to_jaden_case(string):
    words = string.split()
    jaden_case_words = [word.capitalize() for word in words]
    jaden_case_string = " ".join(jaden_case_words)
    return jaden_case_string


quote = "how can mirrors be real if our eyes aren't real"
jaden_case_quote = to_jaden_case(quote)
print(jaden_case_quote)