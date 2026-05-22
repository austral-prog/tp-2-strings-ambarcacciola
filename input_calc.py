def rectangle():
    base = int(input("Base: "))
    altura = int(input("Altura: "))

    area = base * altura
    perimetro = 2 * (base + altura)

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")


if __name__ == "__main__":
    rectangle()
