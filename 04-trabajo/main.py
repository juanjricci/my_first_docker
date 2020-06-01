from person import Person
from personService import PersonService

class App():
    def menu_person(self):
        print("\n\n1. Listar persona")
        print("2. Agregar persona")
        print("3. Modificar persona")
        print("4. Eliminar persona")
        return int(input("Elija una opcion: "))

if __name__ == "__main__":
    app = App()
    personService = PersonService()

    while True:
        opcion_person = app.menu_person()
        if opcion_person == 1:
            listPerson = personService.get_personList()
            for key in listPerson:
                print("legajo: %s -> %s" % (key, listPerson[key]))

        if opcion_person == 2:
            p = Person()
            p.name = str(input("Ingrese nombre: "))
            p.surname = str(input("Ingrese apellido: "))
            p.age = int(input("Ingrese edad: "))
            personService.add_person(p)

        if opcion_person == 3:
            p = Person()
            key = int(input("Ingrese el legajo de la persona a modificar: "))
            p.name = str(input("Ingrese el nuevo nombre: "))
            p.surname = str(input("Ingrese el nuevo apellido: "))
            p.age = int(input("Ingrese la nueva edad: "))
            personService.update_person(key, p)

        if opcion_person == 4:
            p = Person()
            key = int(input("Ingrese legajo de la persona: "))
            personService.delete_person(key)    

        if opcion_person < 1 or opcion_person > 4:
                break