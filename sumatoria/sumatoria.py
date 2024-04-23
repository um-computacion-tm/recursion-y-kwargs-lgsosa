def sumatoria1(value):
    resultado = 0
    while value > 0:
        resultado = resultado + value 
        value -= 1
    return resultado
result = sumatoria1(4)
print(result)

def sumatoria(value):
    if value == 1:
        return 1
    return value + sumatoria(value - 1)
resultado = sumatoria(6)
print(resultado)