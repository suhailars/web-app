import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
cur = con.cursor()  
cur.execute("DROP TABLE IF EXISTS blog")
cur.execute("CREATE TABLE blog(id SERIAL PRIMARY KEY, author TEXT,post TEXT)")
con.commit()
con.close()
