#Percorre os numeros de 1 a 100
for i in range(1,101):
    #Verifica se o numero é divisivel por 3 e 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #Verifica se o numero é divisivel por 3
    elif i % 3 == 0:
        print("Fizz")
    #Verifica se o numero é divisivel por 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)