# 5. create a simple test file   PostgreSQL connection in the simplest way possible
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="infra_monitoring_db",
        user="postgres",
        password="*******",
        host="localhost",
        port="5432"
    )

    print("✅ PostgreSQL connected successfully")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("PostgreSQL version:", version)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error while connecting to PostgreSQL")
    print(e)




