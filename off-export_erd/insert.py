import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="100%Safe",
    database="open_food_facts"
)




table_name = "Product"
attributes = "product_id, code, lc, quantity, quantity_unit_id, serving_size, serving_size_unit_id, obsolete, obsolete_since_date, link, nova_group, nova_group_tag"
values = "1234567890123, 1234567890123, 'en', 500, 1, 250, 2, 0, NULL, 'http://example.com/product/1234567890123', 4, 'en:4-ultra-processed-food-and-drink-products'"




cursor = conn.cursor()
cursor.execute("insert into " + table_name + "(" + attributes + ") values(" + values + ");")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()