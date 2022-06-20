from server import app 
from flaskext.mysql import MySQL
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'trab_final_lp3'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
