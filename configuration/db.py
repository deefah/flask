from configuration import params as para
import psycopg2
from configuration import credential as crd


def call_procedure(function, column):
    ps_connection = psycopg2.connect(user=crd.database_user, password=crd.database_password,
                                     host=para.db_host_ip, port=para.db_port, database=para.db_name)
    cursor = ps_connection.cursor()
    cursor.callproc(function, column)
    result = cursor.fetchall()
    #cursor.close()
    ps_connection.commit()
    #ps_connection.close()
    return result