import sqlite3
# python drivers for sqlite DB
try: #create connection
 con = sqlite3.connect("master.db")
 #create a cursor
 cur = con.cursor()
  #prepare & Execute the query
 cur.execute('''create table if not exists emps( name string, age integer)''')
 data=(("ravi",10), ("hari",20), ("manu",30), ("john",40))
 for rec in data:
 #perpare the query
  query="insert into emps values('%s',%s)" %(rec[0],rec[1])
 #execute the query
  cur.execute(query)
 # commit the changes con.commit()
  query="select * from emps"
  cur.execute(query)
 for elem in cur.fetchall():
    print(elem)
except sqlite3.Exception as e1:
  print("Error = ",e1)
finally:
 cur.close()
 con.close()