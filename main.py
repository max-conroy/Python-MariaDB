
# python connection with MariaDB
import mariadb
import sys


if __name__ == '__main__':

    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="classicmodels"

        )
        conn.autocommit = True

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    else:
        print("connection opened!")
    # Get Cursor
    cur = conn.cursor()

    cur.execute(
        "select * from customers where country = ? order by contactLastName", ("USA",)
    )

    for i in cur:
        print(i)

    conn.close()



