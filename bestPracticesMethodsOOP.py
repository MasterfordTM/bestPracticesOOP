class Alumno:
    # Constructor con atributos vacíos
    def __init__(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_completo(self):
        return f"{self.get_nombre() or 'No definido'} {self.get_apellido_paterno() or 'No definido'} {self.get_apellido_materno() or 'No definido'}"

    # Método para mostrar la información del alumno
    def mostrar_info(self):
        return (f"Nombre: {self.get_nombre() or 'No definido'} "
                f"{self.get_apellido_paterno() or 'No definido'} "
                f"{self.get_apellido_materno() or 'No definido'}, "
                f"No. Control: {self.get_no_control() or 'No definido'}, "
                f"Semestre: {self.get_semestre() or 'No definido'}")


# Crear un diccionario para almacenar hasta 50 alumnos
alumnos_dict = {}

# Bucle para ingresar hasta 50 alumnos
for i in range(3):
    print(f"\n--- Ingreso de Alumno {i} ---")

    alumno = Alumno()

    nombre = input("Ingrese el nombre: ")
    apellido_paterno = input("Ingrese el apellido paterno: ")
    apellido_materno = input("Ingrese el apellido materno: ")
    no_control = input("Ingrese el número de control: ")
    semestre = input("Ingrese el semestre: ")

    # Almacenar la instancia en el diccionario
    alumnos_dict[i] = alumno
    print(f"nombre: {alumnos_dict[0].get_nombre()}")

    # Establecer valores en la instancia de Alumno
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

#mostrar los nombres registrados
for i in range(3):
    print(f"Nombre:{alumnos_dict[i].get_nombre()}")



# Mostrar información de todos los alumnos almacenados
print("\n--- Información de Alumnos ---")
for clave, alumno in alumnos_dict.items():
    print(f"\nAlumno {clave}:")
    print(alumno.mostrar_info())