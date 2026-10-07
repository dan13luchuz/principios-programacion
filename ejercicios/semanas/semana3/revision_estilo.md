# Revisión de estilo de un programa secuencial

## Lista de cotejo

| # | Criterio | Respuesta | Observación |
|---|---|---|---|
| 1 | ¿Las variables tienen nombres descriptivos? | Sí | Los nombres como `nombreCliente`, `nombre_plato`, `precio`, `cantidad`, `subtotal`, `impuesto` y `total` permiten identificar qué información almacenan. |
| 2 | ¿Se utiliza una misma convención para nombrar las variables? | No | Se utilizan diferentes formas de nombrar variables, por ejemplo `nombreCliente` y `nombre_plato`. |
| 3 | ¿Se utilizan espacios alrededor de los operadores? | No | Los operadores no tienen espacios alrededor. Por ejemplo, se utiliza `subtotal=...` en lugar de `subtotal = ...`. |
| 4 | ¿Los mensajes de entrada son claros y consistentes? | Sí | Los mensajes indican claramente al usuario qué información debe ingresar. |
| 5 | ¿Las operaciones matemáticas están correctamente escritas? | No | En `preciocantidad` falta el operador de multiplicación `*` y en `subtotal13/100` falta el operador que indica la multiplicación por 13. |
| 6 | ¿Los resultados se almacenan en variables antes de mostrarlos? | Sí | Los resultados se almacenan en `subtotal`, `impuesto` y `total` antes de utilizar `print()`. |
| 7 | ¿La salida de información es clara y fácil de leer? | Sí | Los resultados están identificados mediante etiquetas como cliente, plato, subtotal, impuesto y total a pagar. |
| 8 | ¿El código mantiene un estilo consistente? | No | Hay diferencias en la forma de nombrar variables y en el uso de espacios alrededor de los operadores. |
| 9 | ¿El programa es fácil de leer y comprender? | No | Aunque se entiende la intención del programa, los errores en las operaciones y la falta de espacios dificultan la lectura y comprensión del código. |
| 10 | ¿El programa cumple con lo solicitado en el problema? | No | El programa intenta calcular el subtotal, impuesto y total, pero las operaciones matemáticas están escritas incorrectamente y no producirían los resultados esperados. |

## Reflexión

Considero que el error más importante encontrado es la forma incorrecta en que están escritas algunas operaciones matemáticas, ya que no solo dificulta la comprensión del código, sino que también puede provocar que el programa no funcione correctamente.

Por ejemplo, en `subtotal=preciocantidad` falta el operador de multiplicación `*`.

Además, la falta de espacios alrededor de los operadores hace que el código sea menos ordenado y fácil de leer.