CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    email VARCHAR(50),
    fecha_registro DATEsTIME
);

INSERT INTO usuarios (nombre, email, fecha_registro) VALUES
    ('Gustavo', 'boogiexd1998@gmail.com', '2024-09-12'),
    ('Angeles', 'angeles@ejem.com', '2024-09-12'),
    ('Kobu', 'kobu@ejem.com', '2024-09-12');