import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='Joker123' host='localhost' port='5432'") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #write sql code for database
    conn.commit() #commit changes to database
    conn.close() #close connection to database

def insert(item, quantity, price):
        conn=psycopg2.connect("dbname='db1' user='postgres' password='Joker123' host='localhost' port='5432'") #1st step create connection, if no db exists this creates the db
        cur=conn.cursor() #creates cursor object
        #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')"%(item,quantity,price))
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
        conn.commit() #commit changes to database
        conn.close() #close connection to database

#insert("Coffee Cup", 10, 5)

def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='Joker123' host='localhost' port='5432'") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='Joker123' host='localhost' port='5432'") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) #comma after item is necessary
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='Joker123' host='localhost' port='5432'") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item)) #comma after item is necessary if only one parameter
    conn.commit()
    conn.close()

create_table()
#insert("Orange",10,15)
#delete("Orange")
update(20,15.0,'Apple')
print(view())
#update(11,6,"water glass")
#delete("Wine glass")

#print(view())
