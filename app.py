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
    """ INSERT INTO medicos (nombre,apellido,especialidad,telefono)
        VALUES ('LUIS','PEREZ','CIRUJANO','12341233');

    """
)
conn.commit()

