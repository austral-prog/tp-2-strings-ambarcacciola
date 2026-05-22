def ficha():
    nombre_raw = input()
    email_raw = input()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    nombre_limpio = nombre_raw.strip().title()
    email_limpio = email_raw.strip().lower()

    posicion_espacio = nombre_limpio.find(" ")
    nombre_solo = nombre_limpio[:posicion_espacio]
    apellido_solo = nombre_limpio[posicion_espacio + 1:]

    iniciales = nombre_solo[0] + apellido_solo[0]

    usuario = apellido_solo.lower() + "." + nombre_solo.lower()

    email_valido = "@" in email_limpio
    posicion_arroba = email_limpio.find("@")
    dominio = email_limpio[posicion_arroba + 1:]

    nombre_archivo = nombre_limpio.replace(" ", "_")
    cant_a = nombre_limpio.lower().count("a")
    codigo_secreto = nombre_limpio[::-1].upper()

    suma_notas = nota1 + nota2 + nota3
    promedio_notas = suma_notas / 3
    promedio_entero = suma_notas // 3

    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_limpio}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cant_a}")
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma_notas}")
    print(f"Promedio: {promedio_notas}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)


if __name__ == "__main__":
    ficha()
