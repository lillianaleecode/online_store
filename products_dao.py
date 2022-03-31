#python3 products_dao.py

import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor() #documentation from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    

    query = "SELECT products.product_id, products.name, unit_measure.unit_measure_name, products.price_per_unit FROM online_store.products JOIN online_store.unit_measure ON products.unit_measure_id = unit_measure.unit_measure_id ;" #order matters

    cursor.execute(query)

    response = []

    for (product_id, name, unit_measure_id, price_per_unit) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name': name,
                'price_per_unit' : price_per_unit,
                'unit_measure_id' : unit_measure_id,
                
                #'unit_measure_name' : unit_measure_name,

            }
        )
        
        #print(product_id, name, unit_measure_id, price_per_unit)

    
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO online_store.products "
             "(product_id, name, unit_measure_id, price_per_unit)"
             "VALUES (%s, %s, %s, %s)")

    data = (product['product_id'], product['product_name'], product['unit_measure_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))

    print(insert_new_product(connection, {
        'product_id': 7,
        'product_name': 'crepes',
        'unit_measure_id': '1',
        'price_per_unit': 10
    }))