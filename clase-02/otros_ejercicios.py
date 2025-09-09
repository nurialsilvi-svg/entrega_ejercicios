resultado = 7 / 3
print("Resultado:", resultado)
print(type(resultado))

resultado = 7 // 3
print("Resultado:", resultado)
print(type(resultado))

# 1. Ingresar tres notas y calcular promedio
nota1 = int(input("Ingresá la primera nota: "))
nota2 = int(input("Ingresá la segunda nota: "))
nota3 = int(input("Ingresá la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3   # promedio siempre será float

print("\n--- Promedio ---")
print("Notas:", nota1, nota2, nota3)
print("Promedio:", promedio)
print("Tipo de dato del promedio:", type(promedio))

# 2. Ingresar dos números y realizar operaciones
num1 = int(input("\nIngresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))

print("\n--- Operaciones ---")
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División normal (/):", num1 / num2)   # siempre float
print("División entera (//):", num1 // num2) # siempre int
print("Módulo (%):", num1 % num2)

# 3. Mostrar tipo de dato de cada E/S
print("\n--- Tipos de datos ---")
print("num1 es de tipo:", type(num1))
print("num2 es de tipo:", type(num2))
print("Promedio es de tipo:", type(promedio))







