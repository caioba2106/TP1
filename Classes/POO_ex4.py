class Animal:
    
    categoria = "Mamífero"

animal1 = Animal()
animal2 = Animal()

print("Categoria inicial de animal1: ", animal1.categoria)
print("Categoria inicial de animal2: ", animal2.categoria)

Animal.categoria = "Ave"

print("Categoria de animal1 após a modificação: ", animal1.categoria)
print("Categoria de animal2 após a modificação: ", animal2.categoria)
