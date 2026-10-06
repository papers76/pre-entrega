# Gestión de productos - Pre-entrega Python

Sistema básico por consola para cargar, listar, buscar y eliminar productos.
Pre-entrega del curso Python Inicial - Talento Tech.

## Ejecutar

```
python app.py
```

## Menú

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir

## Datos

Lista de sublistas: `[nombre, categoria, precio]`. El precio se guarda como entero (sin centavos).

## Decisiones

- La búsqueda usa `in` sobre el nombre en minúsculas, así encuentra coincidencias parciales ("mouse" encuentra "Mouse Logitech" y "Pad para mouse").
- El precio se valida con `isdigit()` antes de convertir con `int()`, para no romper el programa si se ingresa texto.
- Nombre y categoría se guardan con `.title()` para que el listado quede uniforme.
- En la búsqueda se mantiene el número de posición original, así coincide con el que se usa para eliminar.

## Validaciones

- Nombre y categoría no vacíos.
- Precio entero mayor a 0.
- Opción de menú entre 1 y 5.
- Número a eliminar dentro del rango de la lista.
- Aviso si la lista está vacía al mostrar, buscar o eliminar.
