# 🧩 Proyecto: LibrOS Raúl

Este proyecto es una aplicación web desarrollada con **Django**, que permite gestionar un catálogo de libros y películas, recordar contenido y manejar usuarios registrados.

---

## 📂 Estructura del Proyecto

```
proyecto.raull.p/
│
├── mi_proyecto/              # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── catalogo/                 # App para gestión de libros y películas
│   ├── static/
│   ├── templates/catalogo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── recomendador/             # App para el sistema de recomendaciones
│   ├── templates/recomendador/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── usuarios/                 # App para registro y login de usuarios
│   ├── templates/usuarios/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── venv/                     # Entorno virtual (no se sube a Git)
├── db.sqlite3                # Base de datos local
├── manage.py
├── requirements.txt          # Dependencias del proyecto
└── README.md
```

---

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto localmente:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/raultueso2006/proyecto_django.git
```

---

#### Abrir la terminal desde la carpeta donde esta el "manage.py".

### 2️⃣ Crear y activar el entorno virtual

#### 🪟 En Windows (PowerShell o VS Code terminal):
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 En Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Aplicar migraciones

```bash
python manage.py migrate
```

---

### 5️⃣ Crear un superusuario (opcional, para acceder al panel admin)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Luego abrí tu navegador en:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Apps del Proyecto

| Aplicación     | Descripción |
|----------------|-------------|
| `catalogo`     | Maneja los libros, películas y su gestión. |
| `recomendador` | Sistema de recomendaciones y visualización de ítems. |
| `usuarios`     | Registro, login y autenticación de usuarios. |

---

## 🧠 Tecnologías Utilizadas

- **Python 3**
- **Django**
- **SQLite3**
- **HTML / CSS**
- **Bootstrap**

---

## 📜 Notas

- No olvides activar el entorno virtual antes de ejecutar el proyecto.  
- Si se agregan nuevas dependencias, actualiza el archivo `requirements.txt` con:
  ```bash
  pip freeze > requirements.txt
  ```
