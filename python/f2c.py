def f2c(temp):
    '''
    (number) -> number

    Return celsius value from fahrenheit temp parameter
    '''
    return (temp - 32) / 9 * 5
h = input("insert temp: ")
print (f2c(h))
