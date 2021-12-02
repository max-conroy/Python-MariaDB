import mariadb
import sys


def get_all_employees():
    cur.execute(
        "select * from employees"
    )
    for i in cur:
        print(i)


def begin():
    print("--------------------Begin-----------------------------------")
    cur.execute(
        "show tables"
    )
    for i in cur:
        print(i[0], end=" | ")
    print()


def get_fields():
    print("-------------------Show Fields-----------------------------")
    cur.execute(
        "show fields from employees"
    )
    for i in cur:
        print(i[0], end=" ")
    print()

    get_all_employees()


def get_job_title():
    print("----------------------Job Title-------------------------------")
    cur.execute(
        "select firstName, lastName, email from employees where jobTitle = ? order by firstName",
        ("Sales Rep",)
    )

    for i in cur:
        print(i)


def like():
    print("---------------------------Like---------------------------")
    cur.execute(
        "select UPPER(contactLastName), UPPER(contactFirstName) from customers where contactLastName like ?",
        ("S%",)
    )

    for i in cur:
        print(i)


def drop_table():
    print("----------------------Drop table-------------------------------")
    cur.execute(
        "drop table IF EXISTS test"
    )
    cur.execute(
        "create table test("
        "id INT PRIMARY KEY,age INT, first VARCHAR(30), last VARCHAR(30))"
    )

    cur.execute(
        "describe test"
    )
    for i in cur:
        print(i)


def insert_into():
    print("-----------------------insert into------------------------------")
    cur.execute(
        "insert into test (id, age, first, last) values (100, 25, 'jafer', 'alhaboubi')"
    )
    cur.execute(
        "insert into test (id, age, first, last) values (200, 30, 'x', 'z')"
    )

    cur.execute(
        "select * from test"
    )

    for i in cur:
        print(i)


def end():
    print("-----------------------END-----------------------------")
    cur.execute(
        "delete from test where id = ?", (100,)
    )


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
        print("Error connecting to MariaDB Platform:  {}".format(e))
        sys.exit(1)
    else:
        print("successfully connected")
    cur = conn.cursor()

    begin()
    get_fields()
    get_job_title()
    like()
    drop_table()
    insert_into()
    end()

    conn.close()
