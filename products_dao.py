import mysql.connector

cnx= mysql.connector.connect(user='root', password='ORACLE545901', host='127.0.0.1', database='online_store')

cnx.close()

#cursor = cnx.cursor() #documentation from https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html