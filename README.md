# Biblioteca Universitaria

Sitio web informativo para una biblioteca universitaria, desarrollado con Flask y plantillas Jinja. Incluye cuatro páginas para presentar la biblioteca, sus materiales, servicios y medios de contacto.

## Tecnologías

- **Python y Flask** para definir la aplicación y sus rutas.
- **Jinja** para combinar las plantillas HTML con los datos enviados desde Flask.
- **Bootstrap 5.3.3** para la navegación y la presentación adaptable.

## Estructura del proyecto


biblioteca/
├── server.py
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── catalogo.html
│ ├── servicios.html
│ └── contacto.html
└── requirements.txt


## Elementos implementados

### Aplicación Flask — `server.py`

El archivo `server.py` es el punto de entrada de la aplicación. Crea la instancia de Flask y define las rutas, que utilizan `render_template()` para cargar la plantilla correspondiente. Cada ruta envía las variables `titulo` y `mensaje`.

| Página | URL | Plantilla |
|---|---|---|
| Inicio | `/` y `/inicio` | `index.html` |
| Catálogo | `/catalogo` | `catalogo.html` |
| Servicios | `/servicios` | `servicios.html` |
| Contacto | `/contacto` | `contacto.html` |

Al ejecutar el archivo directamente Flask inicia el servidor en el puerto `5050`.

### Plantilla base — `templates/layout.html`

Contiene la estructura HTML compartida por todo el sitio: idioma, metadatos, título del documento, referencia a Bootstrap y el bloque Jinja `content`, donde cada página hija inserta su contenido.

La plantilla también define la navegación horizontal de Bootstrap. El nombre **Biblioteca Universitaria** funciona como identificador del sitio; los enlaces de Inicio, Catálogo, Servicios y Contacto se generan con `url_for()`. Al estar en la plantilla base, el menú aparece en todas las páginas.

### Plantillas de las páginas

Las cuatro plantillas extienden `layout.html` mediante `{% extends "layout.html" %}` y especifican su contenido dentro de `{% block content %}`. Cada una organiza el contenido con `container-fluid`.

- **`templates/index.html` — Inicio:** presenta el nombre de la biblioteca, un mensaje de bienvenida, el propósito de la institución y su horario general.
- **`templates/catalogo.html` — Catálogo:** describe los libros, revistas, tesis y recursos digitales disponibles.
- **`templates/servicios.html` — Servicios:** explica el préstamo de libros, la consulta en sala, el acceso a recursos digitales y la orientación bibliográfica.
- **`templates/contacto.html` — Contacto:** muestra una dirección, un correo institucional ficticio y el horario de atención.

## Instalación y ejecución

1. Abre una terminal en la carpeta del proyecto.
2. Instala las dependencias:
   python -m pip install -r requirements.txt 
3. Inicia la aplicación:
 server.py

4. Abre `http://127.0.0.1:5050/(ruta)` en el navegador.

Bootstrap se carga desde un CDN, por lo que se requiere conexión a Internet para aplicar sus estilos y el comportamiento del menú adaptable.
