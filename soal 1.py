#kode 1
def sequenceGenerator(start, stop):
    x = []
    for i in range(start, stop+1):
        x.append(i)
    return x
print(sequenceGenerator(1, 10))

#jawaban 
def sequenceGenerator(start, stop):return list(range(start, stop+1))
print(sequenceGenerator(1, 10))


#kode 2
def fizzBuzz(a, b):
    x = []
    for num in range (a, b) :
        if num % 3 == 0 and num % 5 == 0 :
            x.append('FizzBuzz')
        elif num % 3 == 0 :
            x.append('Fizz')
        elif num % 5 == 0 :
            x.append('Buzz')
        else :
            x.append(num)
    return x

#jawaban 
def fizzBuzz(a, b):
    return [val for val in (map(lambda num: 'FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num, range(a, b))) if val is not None]


# #kode 3
def twoNumber(l) :
    res = []
    for i in 1 :
        if l.index(i) == len (1)-1 :
            break
        z = i + l[i+1]
        res.append(z)
    return res

#jawaban
def twoNumber(l):
    return [x + y for x, y in zip(l, l[1:])]


    