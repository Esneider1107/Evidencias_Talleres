import os
import psycopg
from psycopg.rows import dict_row
from flask import Flask, jsonify, request

app = Flask(__name__)

INSTANCE = os.getenv("INSTANCE", "api-local")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "shop")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_db_connection():
    return psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        row_factory=dict_row
    )

@app.get("/products")
def get_products():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, float8(price) AS price FROM products ORDER BY id ASC;")
            products = cur.fetchall()
    return jsonify({
        "served_by": INSTANCE,
        "products": products
    })

@app.get("/products/<int:product_id>")
def get_product(product_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, float8(price) AS price FROM products WHERE id = %s;", (product_id,))
            product = cur.fetchone()
    if not product:
        return jsonify({"error": "Producto no encontrado", "served_by": INSTANCE}), 404
    return jsonify({"served_by": INSTANCE, "product": product})

@app.post("/products")
def create_product():
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")
    if not name or price is None:
        return jsonify({"error": "Faltan datos 'name' o 'price'"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id, name, float8(price) AS price;",
                (name, price)
            )
            new_product = cur.fetchone()
            conn.commit()
    return jsonify({"served_by": INSTANCE, "product": new_product}), 201

@app.put("/products/<int:product_id>")
def update_product(product_id):
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM products WHERE id = %s;", (product_id,))
            if not cur.fetchone():
                return jsonify({"error": "Producto no encontrado", "served_by": INSTANCE}), 404

            cur.execute(
                "UPDATE products SET name = COALESCE(%s, name), price = COALESCE(%s, price) WHERE id = %s RETURNING id, name, float8(price) AS price;",
                (name, price, product_id)
            )
            updated_product = cur.fetchone()
            conn.commit()
    return jsonify({"served_by": INSTANCE, "product": updated_product})

@app.delete("/products/<int:product_id>")
def delete_product(product_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s RETURNING id;", (product_id,))
            deleted = cur.fetchone()
            conn.commit()
    if not deleted:
        return jsonify({"error": "Producto no encontrado", "served_by": INSTANCE}), 404
    return jsonify({"served_by": INSTANCE, "message": f"Producto {product_id} eliminado exitosamente"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)