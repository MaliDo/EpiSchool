import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind.db')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_all_suppliers():
    return query("""SELECT * FROM Supplier""")

def get_products(supplier_id):
    return query("""SELECT * FROM Product
                WHERE SupplierId = ?""", supplier_id)

def get_supplier(supplier_id):
    return query("""SELECT CompanyName FROM Supplier
                WHERE Id = ?""", supplier_id)

def get_categories():
    return query("""SELECT Category.Id, Category.CategoryName, Category.Description, count(product.Id) FROM Category
                INNER JOIN Product
                on Category.Id = Product.CategoryId 
                GROUP by category.Id""")

def get_products_by_category(category_id):
    return query("""SELECT Category.CategoryName, Product.ProductName, Supplier.Id, Supplier.CompanyName FROM Category
                INNER JOIN Product
                on Category.Id = Product.CategoryId 
				INNER JOIN Supplier
                on Product.SupplierId = Supplier.Id 
                WHERE Category.Id = ?""", category_id)

def get_the_category(category_id):
    return query("""SELECT CategoryName FROM Category
                WHERE Id = ?""", category_id)