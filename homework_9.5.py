def quadratic_equation(a, b, c):
    def calc_result(a, b, c, x1, x2):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
        elif discriminant == 0:
            x1 = -b / (2 * a)
        return x1, x2

    x1 = None
    x2 = None
    x1, x2 = calc_result(a, b, c, x1, x2)
    return x1, x2

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

x1, x2 = quadratic_equation(a, b, c)

if x1 is not None and x2 is not None:
    print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
elif x1 is not None:
    print(f"Корінь рівняння: x = {x1}")
else:
    print("Рівняння не має дійсних коренів.")
