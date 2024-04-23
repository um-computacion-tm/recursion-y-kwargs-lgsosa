
def sumatoria(value):
    if value == 1:
        return 1
    return value + sumatoria(value - 1)
resultado = sumatoria(6)
print(resultado)