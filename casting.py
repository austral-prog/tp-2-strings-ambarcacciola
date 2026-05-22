def casting():
    precio_str = input()
    precio = int(precio_str)

    descuento_str = input()
    descuento = float(descuento_str)

    cantidad_str = input()
    cantidad = int(cantidad_str)

    precio_con_descuento = precio - descuento
    total = precio_con_descuento * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")

if __name__ == "__main__":
    casting()
