# Límites de los descuentos
LIMITE_5 = 30000
LIMITE_10 = 60000
LIMITE_15 = 100000

# Porcentajes de descuento
PORCENTAJE_5 = 0.05
PORCENTAJE_10 = 0.10
PORCENTAJE_15 = 0.15

# Entrada de datos
monto_compra = float(input("Ingrese el monto de la compra: ₡"))

# Determinar el porcentaje de descuento
if monto_compra >= LIMITE_15:
    porcentaje_descuento = PORCENTAJE_15

elif monto_compra >= LIMITE_10:
    porcentaje_descuento = PORCENTAJE_10

elif monto_compra >= LIMITE_5:
    porcentaje_descuento = PORCENTAJE_5

else:
    porcentaje_descuento = 0

# Calcular descuento y total
monto_descuento = monto_compra * porcentaje_descuento
total_pagar = monto_compra - monto_descuento

# Mostrar resultados
print("\n--- Resumen de la compra ---")
print(f"Monto de la compra: ₡{monto_compra:,.2f}")
print(f"Descuento aplicado: {porcentaje_descuento * 100:.0f}%")
print(f"Monto del descuento: ₡{monto_descuento:,.2f}")
print(f"Total a pagar: ₡{total_pagar:,.2f}")