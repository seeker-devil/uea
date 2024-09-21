def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primera llamada: solo con monto total
monto_total1 = 1000
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1

print("Primera llamada:")
print(f"Monto Total: ${monto_total1}")
print(f"Descuento: ${descuento1:.2f}")
print(f"Monto Final: ${monto_final1:.2f}")
print()

# Segunda llamada
monto_total2 = 10000
porcentaje2 = 20
descuento2 = calcular_descuento(monto_total2, porcentaje2)
monto_final2 = monto_total2 - descuento2

print("Segunda llamada:")
print(f"Monto Total: ${monto_total2}")
print(f"Descuento: ${descuento2:.2f}")
print(f"Monto Final: ${monto_final2:.2f}")