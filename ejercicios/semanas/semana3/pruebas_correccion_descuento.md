# Pruebas de corrección del descuento

El programa original debía aplicar un descuento del 10 % al precio ingresado.

El código original calculaba el precio final restando directamente el número 10:

```python
p = float(input("Precio: "))
d = 10
pf = p - d
print("Precio final:", pf)
```

El problema es que el valor `10` se está restando directamente al precio como una cantidad fija, en lugar de calcular el 10 % del precio ingresado.

---

## Corrección del programa

Para corregir el problema, primero se calcula cuánto representa el 10 % del precio original y luego se resta ese monto.

```python
PORCENTAJE_DESCUENTO = 10

precio_original = float(input("Ingrese el precio original: "))

monto_descuento = precio_original * PORCENTAJE_DESCUENTO / 100

precio_final = precio_original - monto_descuento

print("Precio final:", precio_final)
```

La versión corregida también se encuentra en el archivo:

`correccion_descuento.py`

---

## Casos de prueba

Se consideran diferentes tipos de entrada para comprobar el comportamiento del programa.

| Tipo de prueba | Entrada | Resultado esperado |
|---|---:|---:|
| Normal | ₡10 000 | ₡9 000 |
| Límite | ₡0 | ₡0 |
| Inválido | Precio negativo | El dato debería validarse |
| Extremo | ₡1 000 000 | ₡900 000 |

### Caso normal

Con un precio de ₡10 000:

```text
10 000 × 10 / 100 = 1 000
```

El descuento es de ₡1 000 y el precio final es:

```text
₡9 000
```

### Caso límite

Con un precio de ₡0, el descuento también es ₡0 y el precio final permanece en ₡0.

### Caso inválido

Si se introduce un precio negativo, el programa puede realizar el cálculo porque todavía no tiene una validación para impedir este tipo de entrada.

Esto muestra una posible mejora futura: comprobar que el precio sea mayor o igual a cero.

### Caso extremo

Con un precio de ₡1 000 000:

```text
1 000 000 × 10 / 100 = 100 000
```

El precio final es:

```text
₡900 000
```

---

## Resultado del análisis

El error principal del programa original era tratar el número `10` como una cantidad fija que debía restarse al precio.

La versión corregida calcula primero el 10 % del precio original y después resta ese monto.

De esta manera, el descuento se adapta correctamente al valor ingresado.

Las pruebas también muestran que podría agregarse posteriormente una validación para impedir precios negativos.