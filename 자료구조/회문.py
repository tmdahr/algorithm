def palindrome(s) :
    queue=[]
    stack=[]
    for i in s :
        if i.isalpha() :
            queue.append(i.lower())
            stack.append(i.lower())
    for i in queue :
        if i!=stack.pop():
            return False
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))