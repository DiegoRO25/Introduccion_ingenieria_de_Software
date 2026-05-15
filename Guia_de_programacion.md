# Guía de Buenas Prácticas en Python 🐍

## ¿Por qué son importantes?

Las buenas prácticas ayudan a:

- Tener código más limpio
- Facilitar el mantenimiento
- Evitar errores
- Trabajar mejor en equipo
- Hacer el código más profesional

---

# 1. Nombres de Variables

Las variables deben tener nombres claros y descriptivos.

## ✅ Correcto

```python
nombre_usuario = "Diego"
edad_usuario = 20
total_compra = 150.50
```

## ❌ Incorrecto

```python
n = "Diego"
x = 20
a = 150.50
```

---

# Reglas recomendadas

- Usar minúsculas
- Separar palabras con `_`
- Evitar nombres ambiguos
- No usar caracteres especiales

## Estilo recomendado: `snake_case`

```python
cantidad_productos = 10
precio_total = 250
```

---

# 2. Nombres de Clases

Las clases usan `PascalCase`.

## ✅ Correcto

```python
class Usuario:
    pass

class SistemaVentas:
    pass
```

## ❌ Incorrecto

```python
class usuario:
    pass

class sistema_ventas:
    pass
```

---

# 3. Nombres de Métodos y Funciones

Los métodos y funciones usan `snake_case`.

## ✅ Correcto

```python
def calcular_promedio():
    pass

def iniciar_sesion():
    pass
```

---

# 4. Nombres de Constantes

Las constantes se escriben en MAYÚSCULAS.

```python
PI = 3.1416
MAXIMO_INTENTOS = 3
IVA = 0.16
```

---

# 5. Nombres de Archivos

Los archivos Python deben:

- Estar en minúsculas
- Separarse con `_`

## ✅ Correcto

```text
sistema_ventas.py
calculadora.py
registro_usuarios.py
```

## ❌ Incorrecto

```text
SistemaVentas.py
Mi Archivo.py
```

---

# 6. Longitud de Línea

Se recomienda que las líneas no superen los 79 caracteres.

## ❌ Incorrecto

```python
mensaje = "Este es un mensaje extremadamente largo que dificulta la lectura del código"
```

## ✅ Correcto

```python
mensaje = (
    "Este es un mensaje más organizado "
    "y fácil de leer"
)
```

---

# 7. Separación de Segmentos de Código

Usa líneas en blanco para separar bloques lógicos.

## ✅ Correcto

```python
nombre = input("Nombre: ")
edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")


print("Programa finalizado")
```

---

# 8. Comentarios

Los comentarios ayudan a entender el código.

## Comentario simple

```python
# Calcular promedio del alumno
promedio = suma / cantidad
```

## Comentario en varias líneas

```python
\"\"\"
Este programa calcula
el promedio de un alumno
y muestra si aprobó.
\"\"\"
```

---

# Recomendaciones para comentarios

✅ Explicar partes complejas  
✅ Mantenerlos cortos  
✅ Actualizarlos si cambia el código  

## ❌ Evita comentarios innecesarios

```python
# Sumar dos números
resultado = num1 + num2
```

---

# 9. Formato de Operadores Matemáticos

Debe haber espacios entre operadores.

## ✅ Correcto

```python
resultado = num1 + num2
promedio = suma / cantidad
```

## ❌ Incorrecto

```python
resultado=num1+num2
promedio=suma/cantidad
```

---

# Operadores matemáticos

| Operador | Uso |
|---|---|
| `+` | Suma |
| `-` | Resta |
| `*` | Multiplicación |
| `/` | División |
| `%` | Módulo |
| `**` | Potencia |

---

# 10. Operadores Lógicos

## Operadores principales

| Operador | Significado |
|---|---|
| `and` | Y |
| `or` | O |
| `not` | Negación |

---

## Ejemplo de `and`

```python
edad = 20
tiene_ine = True

if edad >= 18 and tiene_ine:
    print("Puede entrar")
```

---

## Ejemplo de `or`

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana")
```

---

## Ejemplo de `not`

```python
usuario_bloqueado = False

if not usuario_bloqueado:
    print("Acceso permitido")
```

---

# 11. Indentación

Python usa indentación obligatoria.

Se recomienda usar **4 espacios**.

## ✅ Correcto

```python
if edad >= 18:
    print("Mayor")
```

## ❌ Incorrecto

```python
if edad >= 18:
print("Mayor")
```

---

# 12. Ejemplo Completo Aplicando Buenas Prácticas

```python
# Constante
MAXIMO_INTENTOS = 3


class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


def verificar_mayoria_edad(edad):
    return edad >= 18


nombre_usuario = input("Nombre: ")
edad_usuario = int(input("Edad: "))

usuario = Usuario(nombre_usuario, edad_usuario)

usuario.mostrar_informacion()

if verificar_mayoria_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

---

# 13. Recomendaciones Finales

✅ Usa nombres descriptivos  
✅ Mantén el código ordenado  
✅ Separa bloques de código  
✅ Comenta solo lo necesario  
✅ Respeta la indentación  
✅ Usa espacios correctamente  
✅ Evita líneas demasiado largas  
