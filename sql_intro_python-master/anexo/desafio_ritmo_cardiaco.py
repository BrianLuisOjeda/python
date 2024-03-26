
import sqlite3

def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sensor")   

    data = c.fetchall()

    conn.commit()
    conn.close()
    return data 

if __name__ == "__main__":
    # Leer la DB
    data = fetch()
    print(data)

    # Data analytics
    #show(data)
    #valor_medio, valor_min, valor_max, valor_std = estadistica(data)
    #regiones(data, valor_medio, valor_std)