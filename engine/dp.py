import sqlite3

con = sqlite3.connect('sophia.db')
cursor = con.cursor()

#create app table
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer PRIMARY KEY, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)


#insert apps data
query = "INSERT INTO sys_command VALUES ( null,'spyder','C:\\Program Files\\Spyder\\Python\\pythonw.exe')"
cursor.execute(query)
con.commit()
con.close() 

#create web table
query = "CREATE TABLE IF NOT EXISTS web_command(id integer PRIMARY KEY, name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

#insert web data
query = "INSERT INTO web_command VALUES ( null,'chat g p t ','https://chatgpt.com/')"
cursor.execute(query)
con.commit()
con.close()


