import mysql.connector
# Conexión
database = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="creditos3_bd"#6
)
# 1 identifico si hay conexion
print(database)

# 2 Cursor
cursor = database.cursor(buffered=True)
#5 ingresar  a la base
cursor.execute("use creditos3_bd")
# 3 Crear base de datos
cursor.execute("CREATE DATABASE creditos3_bd")
# 3 ver si no ha creado la base de datos entonces creela
cursor.execute("CREATE DATABASE IF NOT EXISTS creditos3_bd")
#4 para mirar que bases de datos hay
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# 6 crea la primer tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos(
   id int(10) auto_increment not null,
   marca varchar(40) not null,
   modelo varchar(40) not null,
   precio float(10,2) not null,
   CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

# 7 mirar todas las tablas
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# 8 insertar datos en la tabla
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
('Seat', 'Ibiza', 5000),
('Renault', 'Clio', 15000),
('Citroen', 'Saxo', 2000),
('Mercedes', 'Clase C', 35000)
]
#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()  
# 9 commit para almacenar los datos en la base de datos  

# 10 mirar todos los datos que hay en la tabla 
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
print("---- TODOS MIS COCHES ---")
for coche in result:
    print(coche[1], coche[2], coche[3])

