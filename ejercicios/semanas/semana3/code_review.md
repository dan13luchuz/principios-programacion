# Code Review en parejas

## Registro de hallazgos

| # | Parte del código | Descripción del hallazgo | Categoría | Propuesta |
|---|---|---|---|---|
| 1 | `print("Precio unitario: ", precio_unitario)` y otros `print()` | Hay diferencias en el uso de espacios dentro de los mensajes de salida. | Mejora de estilo | Mantener un formato uniforme en todos los `print()`. |
| 2 | `# ---Datos de entrada---` / `#---Monto total y monto con descuento---` | Los comentarios no mantienen exactamente el mismo formato. | Mejora de estilo | Utilizar el mismo formato para todos los comentarios. |
| 3 | Nombres de variables | Se utilizan diferentes convenciones para nombrar variables, por ejemplo `nombreCliente` y `nombre_plato`. | Mejora de estilo | Utilizar una sola convención para todas las variables, por ejemplo `snake_case`: `nombre_cliente`, `nombre_plato`, `precio_unitario`. |

## Conclusiones

### ¿Cuál fue el error más importante encontrado?

El problema más importante fue la falta de consistencia en el estilo del código, ya que se utilizaron distintas formas para nombrar variables y presentar la información.

### ¿Cuál fue la principal mejora de estilo propuesta?

La principal mejora propuesta fue mantener una convención uniforme para los nombres de las variables, utilizando `snake_case`.

### ¿Qué sugerencia decidieron no aplicar y por qué?

Se decidió no realizar cambios adicionales que no fueran necesarios para el funcionamiento o la claridad del programa, ya que el objetivo principal era revisar el código original.

### ¿Qué aprendieron al revisar el código de otra persona?

Aprendimos que un programa no solo debe funcionar correctamente, sino que también debe ser claro, ordenado y mantener un estilo consistente para facilitar su lectura y mantenimiento.