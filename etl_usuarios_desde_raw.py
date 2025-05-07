import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from datetime import datetime

def limpiar_email(email):
    if isinstance(email, str) and "@" in email and "." in email:
        return email
    return None

def parse_fecha(fecha):
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(fecha, fmt).strftime("%Y-%m-%d")
        except:
            continue
    return None

def transformar_activo(valor):
    if isinstance(valor, str):
        valor = valor.strip().lower()
        return int(valor in ['sí', 'si', 'true', '1'])
    return int(bool(valor))

def transform_data(df):
    df['nombre_completo'] = df['nombre_completo'].str.strip().str.lower()
    df['email'] = df['email'].apply(limpiar_email)
    df = df.dropna(subset=['email']).copy()
    df['fecha_registro'] = df['fecha_registro'].astype(str).apply(parse_fecha)
    df['activo'] = df['activo'].apply(transformar_activo)
    return df

def main():
    conn_raw = sqlite3.connect('usuarios_raw.db')
    df_raw = pd.read_sql_query('SELECT * FROM usuarios_raw', conn_raw)
    conn_raw.close()

    df_clean = transform_data(df_raw)

    engine = create_engine('sqlite:///usuarios.db')
    df_clean.to_sql('usuarios_limpios', engine, if_exists='replace', index=False)

    conn = sqlite3.connect('usuarios.db')
    result = conn.execute('SELECT COUNT(*) FROM usuarios_limpios WHERE activo = 1').fetchone()
    print(f"Usuarios activos: {result[0]}")
    conn.close()

if __name__ == '__main__':
    main()