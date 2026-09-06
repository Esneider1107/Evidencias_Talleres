// Seleccionar o crear la base de datos 'tienda'
db = db.getSiblingDB('tienda');

// Colección: products
db.products.insertMany([
  { name: 'Laptop', price: 3500000, stock: 5 },
  { name: 'Mouse', price: 80000, stock: 20 },
  { name: 'Keyboard', price: 150000, stock: 12 },
  { name: 'Monitor 27', price: 1200000, stock: 8 },
  { name: 'Headphones', price: 250000, stock: 15 }
]);

// Colección: customers
db.customers.insertMany([
  { name: 'Ana', email: 'ana@example.com', city: 'Cali' },
  { name: 'Luis', email: 'luis@example.com', city: 'Bogotá' },
  { name: 'Marta', email: 'marta@example.com', city: 'Medellín' }
]);

// Colección: orders (Reto con documentos e ítems anidados)
db.orders.insertMany([
  {
    customerEmail: 'ana@example.com',
    date: ISODate('2026-08-24T00:00:00Z'),
    status: 'completed',
    items: [
      { product: 'Laptop', price: 3500000, quantity: 1 },
      { product: 'Mouse', price: 80000, quantity: 2 }
    ],
    total: 3660000
  },
  {
    customerEmail: 'luis@example.com',
    date: ISODate('2026-08-25T10:30:00Z'),
    status: 'pending',
    items: [
      { product: 'Keyboard', price: 150000, quantity: 1 }
    ],
    total: 150000
  }
]);