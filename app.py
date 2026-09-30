import sqlite3
conn=sqlite3.connect("hospital.db")
conn.execute(
    """ CREATE TABLE IF NOT EXISTS medicos (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    telefono VARCHAR(20));
    """)

conn.execute(
    """CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
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
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    motivo_consulta VARCHAR(255),
    CONSTRAINT fk_cita_paciente FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE,
    CONSTRAINT fk_cita_medico FOREIGN KEY (id_medico) REFERENCES medicos(id_medico) ON DELETE CASCADE
);


""")
#conn.execute(
#   """ INSERT INTO medicos (nombre,apellido,especialidad,telefono)
#        VALUES ('LUIS','PEREZ','CIRUJANO','12341233');

#    """
#)
#conn.execute("""
#    INSERT INTO pacientes (nombre,apellido,CI,fecha_nacimiento,telefono)
#    VALUES ('roberto','quispe','7842154 LP','2000-12-12','547457224');


#""") 
#conn.execute("""
#INSERT INTO citas (id_paciente,id_medico,fecha_hora,motivo_consulta)
#VALUES (1,1,'13:50','Resfrio');
#""")
#conn.execute("""
#INSERT INTO citas (id_paciente,id_medico,fecha_hora,motivo_consulta)
#VALUES (3,1,'13:50','Resfrio');
#""")


conn.commit()

