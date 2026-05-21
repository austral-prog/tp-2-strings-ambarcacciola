def names():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_completo = nombre + " " + apellido
    minusculas = nombre_completo.lower()
    titulo = nombre_completo.title()
    mayusculas = nombre_completo.upper()
    tabulado = "\t" + minusculas

    if __name__ == "__main__":
        names()
