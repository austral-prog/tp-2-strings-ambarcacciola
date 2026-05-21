def change():
    print("Ingresar gasto:")
    gasto_str = input()

    if "." in gasto_str and gasto_str.endswith("0"):
        gasto_str = gasto_str.rstrip("0")

    print(gasto_str)
    gasto = float(gasto_str)


    print("Dinero recibido")
    dinero_str = input()
    print(dinero_str)
    dinero_recibido = int(dinero_str)


    vuelto_total = dinero_recibido - gasto
    pesos = int(vuelto_total)
    centavos = round((vuelto_total - pesos) * 100)


    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

    if __name__ == "__main__":
        change()
