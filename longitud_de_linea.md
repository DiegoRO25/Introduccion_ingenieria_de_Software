# Guía de Longitud de Línea en Python 🐍

# ¿Qué es la longitud de línea?

La longitud de línea es la cantidad de caracteres que tiene una línea de código.

Python recomienda seguir el estándar de la guía oficial **PEP 8**.

---

# Regla General

✅ Máximo recomendado: **79 caracteres por línea**

Esto ayuda a:

- Mejorar la lectura
- Evitar código desordenado
- Facilitar el trabajo en equipo
- Adaptarse a diferentes pantallas y editores

---

# Ejemplo Incorrecto ❌

```python
mensaje = "Este es un mensaje extremadamente largo que hace difícil leer el código correctamente"
```

---

# Ejemplo Correcto ✅

```python
mensaje = (
    "Este es un mensaje más organizado "
    "y fácil de leer"
)
```

---

# Cómo dividir líneas largas

# 1. Usando paréntesis

```python
resultado = (
    numero1 + numero2 + numero3 +
    numero4 + numero5
)
```

---

# 2. En listas

```python
frutas = [
    "manzana",
    "pera",
    "uva",
    "sandía",
    "plátano"
]
```

---

# 3. En diccionarios

```python
usuario = {
    "nombre": "Diego",
    "edad": 20,
    "correo": "correo@gmail.com"
}
```

---

# 4. En funciones con muchos parámetros

```python
def registrar_usuario(
    nombre,
    apellido,
    correo,
    telefono
):
    print(nombre)
```

---

# 5. En condiciones largas

```python
if (
    edad >= 18
    and tiene_ine
    and pago_realizado
    and usuario_activo
):
    print("Acceso permitido")
```

---

# Evita usar barras invertidas innecesarias

## ❌ Poco recomendado

```python
resultado = numero1 + numero2 + \
numero3 + numero4
```

## ✅ Mejor opción

```python
resultado = (
    numero1 + numero2 +
    numero3 + numero4
)
```

---

# Herramientas útiles

- black
- autopep8
- yapf

---

# Ejemplo usando Black

```bash
black archivo.py
```

---

# Recomendaciones Finales

✅ Mantén líneas cortas  
✅ Divide expresiones largas  
✅ Usa paréntesis  
✅ Escribe código legible  
