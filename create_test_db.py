import psycopg2
from app.config import Config

def create_test_db():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="exam_db",
            user="exam",
            password="exam_password"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute("DROP DATABASE IF EXISTS exam_db_test")
        
        cursor.execute("CREATE DATABASE exam_db_test WITH OWNER exam ENCODING 'UTF8'")
        print("Тестовая БД exam_db_test успешно создана")
        
    except Exception as e:
        print(f"Ошибка при создании тестовой БД: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_test_db()