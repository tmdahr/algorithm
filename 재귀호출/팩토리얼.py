def fact(n) :
    if n==0 :
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))