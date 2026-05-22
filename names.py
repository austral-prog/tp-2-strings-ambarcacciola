def names():
    nombre = input("Ingrese su nombre: ").strip()
    apellido = input("Ingrese su apellido: ").strip()

    nombre_completo = nombre + " " + apellido

    minusculas = nombre_completo.lower()
    titulo = nombre_completo.title()
    mayusculas = nombre_completo.upper()
    tabulado = "\t" + minusculas

    print(minusculas)
    print(titulo)
    print(mayusculas)
    print(tabulado)


if __name__ == "__main__":
    names()
