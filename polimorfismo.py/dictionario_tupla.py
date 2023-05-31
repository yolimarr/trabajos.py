#dictionario y tupla
def suma(*args, **kwargs): #se crea un dictionario
    return kwargs, args

print(suma("ficha 612746", 10, 2, a="luis", b=44, e=true, d=False, e=56, f=6))

#tipos de datos que se pueden almacenar en una tupla:
animales =("perro", "gato", "raton")

#valores numericos
numeros = (4,17, 39, 12)

#valores boleanos
booleanos = (false, false, true, false)

#tambien puede hacer una mezcla de diferentes tipos de datos:
persona = ("persona de ejemplo", "max", 1974, true)

