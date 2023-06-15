from cosas import *

def main():
    l1 = libro.libro_planeta(" El perfume", Autor("Patrick", "Ps"), 1980)
    print(l1)
    #codigo para cambiar el pseudonimo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("--------- Herencia ----------")
    al2 = Alumno("Jose", 19, "328431", "ICO", 9 )
    al2.nombre = "Pepe"
    print(vars(al2))
main()