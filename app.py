import sqlite3
conn=sqlite3.connect("hospital.db")
conn.execute(
    """ CREATE TABLE IF NOT EXISTS medicos (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    telefono VARCHAR(20));
    """)

conn.execute(
    """CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    CI VARCHAR(20) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(20)
);
    """    
)

conn.execute("""

    CREATE TABLE IF NOT EXISTS citas (
    id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    motivo_consulta VARCHAR(255),
    CONSTRAINT fk_cita_paciente FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE,
    CONSTRAINT fk_cita_medico FOREIGN KEY (id_medico) REFERENCES medicos(id_medico) ON DELETE CASCADE
);


""")
#conn.execute(
   #""" INSERT INTO medicos (nombre,apellido,especialidad,telefono)
  #      VALUES ('LUIS','PEREZ','DENTISTA','7894547');

 #  """
#)
#conn.execute("""
 #   INSERT INTO pacientes (nombre,apellido,CI,fecha_nacimiento,telefono)
  #  VALUES ('OSCAR','CHOQUE','233213 LP','2005-12-5','77454514');


#""") 
#conn.execute("""
#INSERT INTO citas (id_paciente,id_medico,fecha_hora,motivo_consulta)
#VALUES (1,1,'13:50','Resfrio');
#""")
#conn.execute("""
#INSERT INTO citas (id_paciente,id_medico,fecha_hora,motivo_consulta)
#VALUES (3,1,'13:50','Resfrio');
#""")
print("TABLA MEDICOS:\n")
cursor=conn.execute("SELECT * FROM MEDICOS;");
for row in cursor:
    print(row)
print("\nTABLA PACIENTES:\n")
cursor=conn.execute("SELECT * FROM PACIENTES;");
for row in cursor:
    print(row)
print("\nTABLA CITAS:\n")   
cursor=conn.execute("SELECT * FROM CITAS;");
for row in cursor:
    print(row)
print("\nTABLA CITAS- join:\n") 
cursor = conn.execute("""
    SELECT 
        c.id_cita,
        p.nombre AS nombre_paciente,
        p.apellido AS apellido_paciente,
        p.CI AS ci_paciente,
        m.nombre AS nombre_medico,
        m.apellido AS apellido_medico,
        m.especialidad,
        c.fecha_hora,
        c.motivo_consulta
    FROM citas AS c
    INNER JOIN pacientes AS p ON c.id_paciente = p.id_paciente
    INNER JOIN medicos AS m ON c.id_medico = m.id_medico;
""")
for row in cursor:
    print(row)




conn.commit()

