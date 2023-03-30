# Написать и вызвать функцию, проверяющую, что слово является
# палиндромом (примеры: “Топот”, “Довод”)
def palindrome(r):
    # if (r := r.lower()) == r[::-1]: вариант с моржовым оператором - переменная k тогда не нужна
    r = r.lower()
    k = r[::-1]
    if k == r:
        print("The word is a palindrome!")
        return True
    else:
        print("The word is NOT a palindrome")
        return False
    # return (r := r.lower()) == r[::-1] - вариант функции в одну строчку
    # В этом случае принт надо вынести за функцию


a = input("Enter a word: ")
palindrome(a)
