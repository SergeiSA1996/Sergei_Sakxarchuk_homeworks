# 6. Напишите функцию для сортировки слов в алфавитном порядке

def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words


word_list = ["banana", "apple", "cherry", "date"]
sorted_words = sort_words(word_list)
print(f"Отсортированные слова: {sorted_words}")