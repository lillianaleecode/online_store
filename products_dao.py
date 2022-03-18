import mysql.connector

def get_all_products():
    cnx= mysql.connector.connect(user='root', password='ORACLE545901', host='127.0.0.1', database='online_store')



    cursor = cnx.cursor() #documentation from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

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

    cnx.close()
    return response

if __name__=='__main__':
    print(get_all_products())