distancia = 9000   # kilómetros
hora_salida = 9
hora_llegada = 10

# Tiempo en horas
tiempo_horas = hora_llegada - hora_salida

# Velocidad en km/h
velocidad_kmh = distancia / tiempo_horas

# Conversión a minutos y segundos
velocidad_km_min = velocidad_kmh / 60
velocidad_km_seg = velocidad_kmh / 3600

print("Velocidad del tren:")
print("->", velocidad_kmh, "km/h")
print("->", velocidad_km_min, "km/min")
print("->", velocidad_km_seg, "km/s")
