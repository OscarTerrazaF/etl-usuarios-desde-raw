# 🛢️ Proyecto ETL desde Base de Datos Cruda | Raw Database ETL Project
Este proyecto implementa un pipeline ETL completo en Python. Parte desde una base de datos SQLite sucia (`usuarios_raw.db`), realiza la limpieza y normalización de los datos con `pandas`, y finalmente carga los datos limpios en una nueva base (`usuarios.db`), lista para análisis o consumo por parte de analistas de datos.

This project implements a complete ETL pipeline in Python. It starts from a raw SQLite database (`usuarios_raw.db`), cleans and normalizes the data using `pandas`, and finally loads the cleaned records into a new SQLite database (`usuarios.db`) ready for analysis or consumption by data teams.

## 🔧 Tecnologías utilizadas | Technologies used
- Python 3  
- pandas  
- sqlite3  
- SQLAlchemy  
- DB Browser for SQLite (visualization)

## 🧪 ¿Qué hace este pipeline? | What does this pipeline do?
✔️ Extrae datos desde una base de datos cruda (`usuarios_raw.db`)  
✔️ Limpia nombres, valida emails, normaliza fechas  
✔️ Convierte campos booleanos como “sí”, “NO”, “false” a 1 o 0  
✔️ Elimina registros con emails inválidos  
✔️ Carga los datos limpios en la base `usuarios.db` en una tabla `usuarios_limpios`

✔️ Extracts records from a raw database (`usuarios_raw.db`)  
✔️ Cleans names, validates emails, normalizes date formats  
✔️ Converts dirty boolean values like “sí”, “NO”, “false” into 1 or 0  
✔️ Drops records with invalid emails  
✔️ Loads cleaned data into `usuarios.db` inside a table named `usuarios_limpios`

## 📂 Archivos del proyecto | Project structure

## ▶️ Cómo ejecutar | How to run
```bash
python etl_usuarios_desde_raw.py
SELECT COUNT(*) FROM usuarios_limpios WHERE activo = 1;
✍️ Autor | Author
Este proyecto fue creado por Oscar Terraza Figueroa como parte de su formación práctica en ingeniería de datos.

This project was created by Oscar Terraza Figueroa as part of his practical training in data engineering.   
