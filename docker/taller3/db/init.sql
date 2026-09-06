CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

INSERT INTO products (name, price) VALUES
('Laptop', 3500000.00),
('Mouse Inalámbrico', 80000.00),
('Teclado Mecánico', 250000.00),
('Monitor 27 Pulgadas', 1200000.00),
('Audífonos Bluetooth', 300000.00);