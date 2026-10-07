# Git, GitHub y beca estudiantil

## Organización del repositorio

Se creó un repositorio relacionado con el curso de Principios de Programación.

El repositorio contiene una carpeta `ejercicios`, donde se organizan las soluciones desarrolladas durante las diferentes semanas del curso.

También contiene un archivo `README.md` con información general del repositorio.

## Ventajas de utilizar un repositorio

Guardar los ejercicios en un repositorio permite mantener los archivos organizados, conservar un historial de los cambios realizados y recuperar versiones anteriores mediante los commits.

Además, GitHub permite almacenar una copia de los trabajos en línea y compartir fácilmente el código mediante un enlace.

---

## Ejercicio: Beca estudiantil

El programa determina si un estudiante puede obtener una beca utilizando su promedio académico, porcentaje de asistencia y participación en un programa de apoyo institucional.

### Datos de entrada

- Promedio académico.
- Porcentaje de asistencia.
- Participación en programa de apoyo.

### Primera condición

El estudiante obtiene la beca si:

`promedio >= 80 and asistencia >= 85`

### Segunda condición

También puede obtenerla si:

`programa_apoyo and asistencia >= 75`

### Combinación de las condiciones

Las dos posibilidades se combinan mediante `or`:

`condicion_academica or condicion_apoyo`

Por lo tanto, basta con que una de las dos condiciones principales sea verdadera para obtener la beca.

---

## Casos de prueba

| Promedio | Asistencia | Programa de apoyo | Resultado esperado |
|---:|---:|---|---|
| 85 | 90 | No | Obtiene la beca |
| 75 | 90 | No | No obtiene la beca |
| 70 | 80 | Sí | Obtiene la beca |
| 70 | 70 | Sí | No obtiene la beca |

## Archivo del programa

La solución se encuentra en:

`beca_estudiantil.py`