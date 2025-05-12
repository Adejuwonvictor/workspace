import psycopg2
from config import load_config

def create_tables():
    """Create table in this PostGRE database"""
    commands = (
        '''CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(50) NOT NULL
        )''',

        '''CREATE TABLE parts(
             part_id SERIAL PRIMARY KEY,
             part_name VARCHAR(50) NOT NULL
             )'''
    )
    try:
        config=load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()