#Paso 1: Elige situaciones del mundo real que puedan ser modeladas mediante POO
#......... Gestión de Mascotas en una Clínica Veterinaria............
#  Versión 1 se creo clases simples como dueño y mascota con solo atributos 

# clinica_veterinaria_v1.py

# Clase Dueño
class Dueño:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    def mostrar_info(self):
        print(f"Dueño: {self.nombre}, Teléfono: {self.telefono}")

# Clase Mascota
class Mascota:
    def __init__(self, nombre, especie, edad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.dueño = dueño

    def mostrar_info(self):
        print(f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}")
        self.dueño.mostrar_info()

# Ejemplo de como se usa
dueño1 = Dueño("Alex Portero", "0963002378")
mascota1 = Mascota("Mia", "Gato", 4, dueño1)

print("Mascota:", mascota1.nombre)
print("Dueño:", mascota1.dueño.nombre)

mascota1.mostrar_info()

