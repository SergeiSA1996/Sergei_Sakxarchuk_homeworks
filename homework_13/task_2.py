# 2)	Создайте программу, которая, принимая массив имён,
# возвращает строку описывающая количество лайков (как в Facebook). Примеры:
# likes() -> "no one likes this"
# likes("Ann") -> "Ann likes this"
# likes("Ann", "Alex") -> "Ann and Alex like this"
# likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this" likes("Ann", "Alex", "Mark", "Max") ->
# "Ann, Alex and 2 others like this"


def likes(*names):
    num_likes = len(names)
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        others = num_likes - 2
        return f"{names[0]}, {names[1]} and {others} others like this"


print(likes())
print(likes("Ann"))
print(likes("Ann", "Alex"))
print(likes("Ann", "Alex", "Mark"))
print(likes("Ann", "Alex", "Mark", "Max"))
