import psycopg2

def db_execute(commands):
    conn = None
    try:
        conn = psycopg2.connect("dbname=brewery_reviews")
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

drop_table_commands = (
    """
    DROP TABLE IF EXISTS cities
    """,
    """
    DROP TABLE IF EXISTS breweries
    """,
    """
    DROP TABLE IF EXISTS reviews
    """
)

create_table_commands = (
    """
    CREATE TABLE IF NOT EXISTS cities (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL,
        ba_city_id INTEGER NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS breweries (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        city VARCHAR(255) NOT NULL,
        state_province VARCHAR(255),
        postal_code VARCHAR(255),
        rating REAL,
        total_ratings INTEGER,
        url VARCHAR(255) NOT NULL,
        ba_brewery_id INTEGER NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS reviews (
        id SERIAL PRIMARY KEY,
        review TEXT NOT NULL,
        rating INTEGER NOT NULL,
        ba_brewery_id INTEGER NOT NULL
    )
    """
)

db_execute(drop_table_commands)
db_execute(create_table_commands)

