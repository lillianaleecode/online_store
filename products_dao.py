import mysql.connector

def get_all_products():
    cnx= mysql.connector.connect(user='root', password='ORACLE545901', host='127.0.0.1', database='online_store')



    cursor = cnx.cursor() #documentation from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

    query = "SELECT products.product_id, products.name, products.price_per_unit, unit_measure.unit_measure_name FROM online_store.products JOIN online_store.unit_measure ON products.unit_measure_id = unit_measure.unit_measure_id ;"

    cursor.execute(query)

    

    for (product_id, name, unit_measure_id, price_per_unit) in cursor:
        print(product_id, name, unit_measure_id, price_per_unit)

    cnx.close()

if __name__=='__main__':
    print(get_all_products())