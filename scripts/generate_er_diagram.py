import os
from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER', 'exam')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'exam_password')
DB_NAME = os.getenv('DB_NAME', 'exam_db')
DB_HOST = os.getenv('DB_HOST', 'localhost')

DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

def generate_er_diagram():
    try:
        engine = create_engine(DB_URI)
        metadata = MetaData()
        
        metadata.reflect(bind=engine)
        
        graph = create_schema_graph(
            engine=engine,
            metadata=metadata,
            show_datatypes=False,
            show_indexes=False,
            rankdir='TB',
            concentrate=False
        )
        
        graph.write_png('docs/er_diagram.png')
        graph.write_svg('docs/er_diagram.svg')
        print("ER диаграмма успешно создана: er_diagram.png и er_diagram.svg")
        
    except Exception as e:
        print(f"Ошибка при создании ER диаграммы: {e}")

if __name__ == "__main__":
    generate_er_diagram()