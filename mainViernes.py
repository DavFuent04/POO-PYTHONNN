from cosasViernes import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)
    print("------- herencia alumno --------")
    al1 = Alumno("Jose", 19, "328431", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = ("Juan")
    print(al2)
    al2.dormir()

    print("------ herencia profesor -------")
    profe1 = Profesor("Jesus", 30 + 16, "367567", "Ingenieria en software")
    print(profe1)
    profe1.dormir()
    print("------- Herencia ayudante Profesor ---------")
    ayudante = Ayudante_Profesor("Adrian", 20, "328456", "ICO", 234567, "Ing En Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O")



main()
