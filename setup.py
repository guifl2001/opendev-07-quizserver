import sqlite3
import csv

def create_database(db_name, sql_file):
    with open(sql_file, 'r') as f:
        sql_script = f.read()
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.executescript(sql_script)
    
    conn.commit()
    conn.close()
    print(f"Banco de dados '{db_name}' criado com sucesso!")

def main():
    db_name = 'quiz.db'
    sql_file = 'quiz.sql'

    create_database(db_name, sql_file)

if __name__ == '__main__':
    main()
