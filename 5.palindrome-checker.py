def isPalindrome(s):
    return s == s[::-1]
word = input("Input a word : ")
ans = isPalindrome(word)
if ans:
    print("Yes")
else:
    print("No")