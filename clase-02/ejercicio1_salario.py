# ==================================================
# Ejercicio 1 – Calculadora de salario (USD)
# ==================================================

# -------------------------
# Versión 1: Consigna tal cual (dos datos predefinidos)
# -------------------------

horas_trabajadas = 48        # horas semanales
tarifa_por_hora = 40.0       # tarifa en USD

salario_total = horas_trabajadas * tarifa_por_hora

print("\n--- Calculadora de salario (USD) ---")
print("Horas trabajadas:", horas_trabajadas, "| Tipo:", type(horas_trabajadas))
print("Tarifa por hora:", tarifa_por_hora, "| Tipo:", type(tarifa_por_hora))
print("Salario total:", salario_total, "| Tipo:", type(salario_total))


# -------------------------
# Versión 2: Consigna expandida (totales derivados)
# -------------------------

horas_semanales = 48
tarifa_por_hora = 40.0

salario_semanal = horas_semanales * tarifa_por_hora
salario_diario  = (horas_semanales / 6) * tarifa_por_hora   # suponiendo 6 días laborales
salario_mensual = salario_semanal * 4                      # aproximación de 4 semanas
salario_anual   = salario_semanal * 52

print("\n--- Calculadora de salario (USD) expandida ---")
print("Horas semanales:", horas_semanales, "| Tipo:", type(horas_semanales))
print("Tarifa por hora:", tarifa_por_hora, "| Tipo:", type(tarifa_por_hora))
print("Salario diario:", salario_diario, "| Tipo:", type(salario_diario))
print("Salario semanal:", salario_semanal, "| Tipo:", type(salario_semanal))
print("Salario mensual:", salario_mensual, "| Tipo:", type(salario_mensual))
print("Salario anual:", salario_anual, "| Tipo:", type(salario_anual))


# -------------------------
# Versión 3: Variante interactiva (el usuario ingresa los datos)
# -------------------------

horas_trabajadas = int(input("\nIngresá la cantidad de horas trabajadas: "))
tarifa_por_hora  = float(input("Ingresá la tarifa por hora (USD): "))

salario_total = horas_trabajadas * tarifa_por_hora

print("\n--- Calculadora de salario interactiva ---")
print("Horas trabajadas:", horas_trabajadas, "| Tipo:", type(horas_trabajadas))
print("Tarifa por hora:", tarifa_por_hora, "| Tipo:", type(tarifa_por_hora))
print("Salario total:", salario_total, "| Tipo:", type(salario_total))
