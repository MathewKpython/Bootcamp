
def Palindrome(word):
    """
        Zwraca wartość typu boolean
        czy podany tekst 'word' jest palindromem
    """
    word = word.lower()
    length = len(word)
    if length < 2:
        return True
    elif word[0] == word[length - 1]:
        return Palindrome(word[1: length - 1])
    else:
        return False
word = "Kajxak"
answer = Palindrome(word)
if answer:
    print(bool(Palindrome(word)))
else:
    print(bool(Palindrome(word)))