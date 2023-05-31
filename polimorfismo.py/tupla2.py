#animales = ("perro", "gato",  "raton", "serpiente", "caballo")
#print(animales[1:4])

#animales = ("perro", "gato",  "raton")
#print(animales[0])

#animales = ("perro", "gato",  "raton", "serpiente", "caballo")
p#rint(len(animales)) #cuenta la cantidad de elementos

#las python tuples son inalterables, por lo que no pueden ser datadas de nuevos elemento
#sin embargo para actuallizar una tupla ya existente, puedes crear una tupla y  añadir valores nuevos
#ademas de la tupla original.
#esto se hace con el operador+ : he aqui un ejemplo


#algunos_animales = ("perro", "gato",  "raton", "serpiente", "caballo")
#todos_los_animales = algunos animales +("hamster", "jirafa")
#print(todos_los_animales)

#la funcion count, cuenta las veces que aparece un elemento dentro de una tupla de python

animales = ("perro", "gato",  "raton", "serpiente", "caballo")
print(animales.count("perro")) 
