INSERT INTO academia.students (name, email) VALUES
('Ana', 'ana@example.com'),
('Luis', 'luis@example.com'),
('Marta', 'marta@example.com');

INSERT INTO academia.teachers (name, email) VALUES
('Dr. Roberto Gómez', 'roberto.gomez@universidad.edu'),
('Dra. Elena Blanco', 'elena.blanco@universidad.edu');

INSERT INTO academia.courses (name, credits, teacher_id) VALUES
('Cloud Computing', 3, 1),
('Internet of Things', 4, 2),
('Bases de Datos Avanzadas', 3, 1);

INSERT INTO academia.enrollments (student_id, course_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3);
