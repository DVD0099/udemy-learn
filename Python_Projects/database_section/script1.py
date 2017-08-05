import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #write sql code for database
    conn.commit() #commit changes to database
    conn.close() #close connection to database

def insert(item, quantity, price):
        conn=sqlite3.connect("lite.db") #1st step create connection, if no db exists this creates the db
        cur=conn.cursor() #creates cursor object
        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
        conn.commit() #commit changes to database
        conn.close() #close connection to database

#insert("Coffee Cup", 10, 5)

def view():
    conn=sqlite3.connect("lite.db") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("DELETE FROM store WHERE item=?", (item,)) #comma after item is necessary
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=sqlite3.connect("lite.db") #1st step create connection, if no db exists this creates the db
    cur=conn.cursor() #creates cursor object
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item)) #comma after item is necessary if only one parameter
    conn.commit()
    conn.close()

update(11,6,"water glass")
#delete("Wine glass")

print(view())
