# Diseñando programas que toman decisiones

## Contexto seleccionado: Tienda de videojuegos

Una tienda vende videojuegos en tres ediciones: estándar, deluxe y coleccionista. El programa determina el precio según la edición y aplica descuentos dependiendo de la cantidad comprada y de si el cliente es estudiante.

---

## Parte 1: Análisis del problema

### ¿Qué datos debe ingresar el usuario?

El usuario debe ingresar:

- La edición del videojuego.
- La cantidad de videojuegos.
- Si es estudiante.

### ¿Qué cálculos debe realizar el programa?

El programa debe:

1. Determinar el precio unitario según la edición.
2. Calcular el subtotal.
3. Calcular el descuento por cantidad.
4. Calcular el subtotal después del descuento.
5. Calcular el descuento adicional para estudiantes cuando corresponda.
6. Calcular el total a pagar.

### ¿Qué valores permanecen fijos durante la ejecución?

Los valores definidos como constantes son:

- Precio estándar: ₡25 000.
- Precio deluxe: ₡35 000.
- Precio coleccionista: ₡50 000.
- Descuento por 3 o 4 videojuegos: 10 %.
- Descuento por 5 videojuegos o más: 15 %.
- Descuento adicional para estudiantes: 5 %.
- Cantidad mínima para obtener descuento: 3.
- Cantidad para obtener el descuento mayor: 5.

### ¿Qué decisiones debe tomar el programa?

Debe determinar:

- Qué edición seleccionó el cliente.
- Si la cantidad es de 5 videojuegos o más.
- Si la cantidad es de al menos 3 videojuegos.
- Si el cliente es estudiante.

### ¿Qué información debe mostrar al finalizar?

Debe mostrar:

- Edición seleccionada.
- Precio unitario.
- Subtotal.
- Descuento por cantidad.
- Descuento por estudiante.
- Total a pagar.

---

## Parte 2: Diagrama de flujo

El siguiente diagrama representa la solución utilizada en el programa.

![Diagrama de tienda de videojuegos](diagrama_tienda_videojuegos.png)

---

## Parte 3: Implementación en Python

La solución fue implementada en el archivo:

`tienda_videojuegos.py`

El programa utiliza variables, constantes, operaciones aritméticas y estructuras condicionales para determinar los descuentos y el total de la compra.

---

## Parte 4: Convenciones y estilo

El programa utiliza nombres de variables relacionados con la información almacenada y constantes escritas con letras mayúsculas.

También utiliza indentación para representar correctamente las estructuras condicionales y comentarios para identificar diferentes partes del programa.

---

## Parte 5: Análisis del flujo condicional

### ¿Cuáles son las condiciones que utiliza el programa?

Entre las principales condiciones se encuentran:

`edicion == "estandar"`

`edicion == "deluxe"`

`edicion == "coleccionista"`

`cantidad >= 5`

`cantidad >= 3`

`es_estudiante == "si"`

### ¿Qué sucede cuando una condición es verdadera?

Se ejecutan las instrucciones que se encuentran dentro de esa rama.

Por ejemplo, si `cantidad >= 5` es verdadera, se aplica un descuento del 15 %.

### ¿Qué sucede cuando una condición es falsa?

El programa continúa con otra condición o ejecuta la rama correspondiente al `else`.

Por ejemplo, si `cantidad >= 5` es falsa, se comprueba si `cantidad >= 3`.

### ¿Existen condiciones que pueden combinarse?

Sí. La cantidad comprada y la condición de estudiante influyen conjuntamente en el cálculo del precio final.

El descuento de estudiante se aplica después del descuento por cantidad cuando corresponde.

### ¿Todas las instrucciones se ejecutan en todas las situaciones?

No. Las instrucciones ejecutadas dependen de los datos ingresados y del resultado de cada condición.

Por ejemplo, un cliente que compra menos de tres videojuegos no ejecuta los cálculos correspondientes al descuento por cantidad ni al descuento adicional de estudiante.

### ¿Qué camino sigue el programa para cada escenario?

Si la edición es válida, se asigna su precio correspondiente y se calcula el subtotal.

Después se determina el descuento:

- 5 videojuegos o más: 15 %.
- 3 o 4 videojuegos: 10 %.
- Menos de 3: sin descuento.

Cuando corresponde un descuento por cantidad, se comprueba además si el cliente es estudiante para aplicar un 5 % adicional.

Finalmente se calcula y muestra el total a pagar.

---

## Reflexión

Una estructura condicional modifica el flujo de ejecución porque permite que el programa tome diferentes caminos dependiendo de los datos ingresados.

En este programa no siempre se ejecutan las mismas instrucciones. Por ejemplo, la cantidad de videojuegos determina qué porcentaje de descuento se aplica y la condición de estudiante puede producir un descuento adicional.

---

## Parte 6: Casos de prueba

| N.º | Tipo de prueba | Datos de entrada | Condición que se prueba | Salida esperada | Resultado obtenido |
|---|---|---|---|---|---|
| 1 | Normal | Estándar, 2 videojuegos, no estudiante | Menos de 3 videojuegos | Subtotal ₡50 000, sin descuentos, total ₡50 000 | Exitosa |
| 2 | Límite | Estándar, 3 videojuegos, no estudiante | `cantidad >= 3` | Subtotal ₡75 000, descuento ₡7 500, total ₡67 500 | Exitosa |
| 3 | Rama verdadera | Deluxe, 5 videojuegos, no estudiante | `cantidad >= 5` | Subtotal ₡175 000, descuento ₡26 250, total ₡148 750 | Exitosa |
| 4 | Rama falsa | Deluxe, 4 videojuegos, no estudiante | `cantidad >= 5` falsa y `cantidad >= 3` verdadera | Subtotal ₡140 000, descuento ₡14 000, total ₡126 000 | Exitosa |
| 5 | Caso especial | Estándar, 3 videojuegos, estudiante | Descuento por cantidad y estudiante | Subtotal ₡75 000, descuento cantidad ₡7 500, descuento estudiante ₡3 375, total ₡64 125 | Exitosa |

---

## Parte 7: Verificación y reflexión

### 1. ¿Todos los resultados obtenidos coinciden con los resultados esperados?

### 1. ¿Todos los resultados obtenidos coinciden con los resultados esperados?

Sí. Los cinco casos de prueba ejecutados produjeron los mismos resultados que se habían calculado previamente, por lo que todas las pruebas fueron exitosas.

### 2. ¿Qué caso de prueba fue más importante para comprobar la lógica del programa?

El caso de 5 videojuegos es importante porque comprueba la nueva regla del descuento del 15 %.

### 3. ¿Qué sucede cuando los datos se encuentran exactamente en un límite?

Cuando la cantidad es exactamente 3, se aplica el descuento del 10 %.

Cuando la cantidad es exactamente 5, se aplica el descuento del 15 %.

### 4. ¿Se ejecutan todas las instrucciones del programa en todos los casos?

No. Las instrucciones ejecutadas dependen de las condiciones que se cumplan.

### 5. ¿Qué ramas del flujo condicional fueron comprobadas?

Se comprobaron:

- Compra sin descuento.
- Descuento del 10 %.
- Descuento del 15 %.
- Descuento adicional para estudiante.
- Selección de diferentes ediciones.
- Edición no válida.

### 6. ¿Existe alguna situación que no haya sido contemplada en los casos de prueba?

Podrían comprobarse valores como una cantidad igual a cero, números negativos o una respuesta diferente de "sí" o "no" para la condición de estudiante.

### 7. ¿Qué modificación realizaría para mejorar el programa?

Se podrían agregar validaciones para impedir cantidades negativas o iguales a cero y controlar mejor los datos ingresados por el usuario.

---

## Reto

Se agregó una nueva regla:

Si el cliente compra 5 videojuegos o más, recibe un descuento del 15 % en lugar del 10 %.

El código y el diagrama de flujo fueron adaptados para incluir esta nueva condición.