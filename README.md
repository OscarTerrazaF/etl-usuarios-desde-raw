# 🛢️ Proyecto ETL desde Base de Datos Cruda

Este proyecto simula un pipeline ETL donde los datos se extraen desde una base de datos sucia (`usuarios_raw.db`), se limpian con Python y se cargan en una base de datos final (`usuarios.db`) lista para análisis.

## 🔧 Tecnologías
- Python
- Pandas
- SQLite
- SQLAlchemy

## 📂 Archivos
- `usuarios_raw.db`: Base con datos sucios
- `etl_usuarios_desde_raw.py`: Script ETL
- `usuarios.db`: Base limpia generada
- `README.md`: Documentación

## ▶️ Cómo ejecutar
```bash
python etl_usuarios_desde_raw.py
```

## ✨ Resultado
Los datos limpios se cargan en la tabla `usuarios_limpios`, y se imprime cuántos usuarios activos hay.