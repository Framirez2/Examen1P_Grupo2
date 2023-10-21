import socket
import mysql.connector
import json

from Client_Encoder import Client_Encoder
from Cliente import Cliente


def server_program():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="grupo2",
        database="Exam"
    )

    host = '127.0.0.1' #obetner el nombre del host
    port = 5002 #asignarle un numero de puerto

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    while True:
        try:
            s.listen(2)  # el numero de sockets con los que se va a trabajar
            conn, address = s.accept()  # esperar la conexion del cliente
            print("Connectionn from: " + str(address))
            #while True:
                    # data = conn.recv(1024).decode() #recibe un valor del cliente

            id, tipo = [int(i) for i in conn.recv(2948).decode('utf-8').split('\n')]

            if not (id or tipo):
                break
            if (tipo == 1):
                cursor = mydb.cursor(dictionary=True)
                listaClientes = []
                try:
                    listaClientes = []
                    cursor.execute("SELECT ID, Cuota, Monto, Fecha_Pago, Fecha_Pago_Realizacion, Estado, Referencia FROM TblEXa WHERE ID=" + str(id))
                    for row in cursor:
                        cliente = Cliente()
                        cliente.setID(str(row['ID']))
                        cliente.setCuota(str(row['Cuota']))
                        cliente.setMonto(str(row['Monto']))
                        cliente.setFechaP(str(row['Fecha_Pago']))
                        cliente.setFechaPR(str(row['Fecha_Pago_Realizacion']))
                        cliente.setEstado(row['Estado'])
                        listaClientes.append(cliente)
                        print(row['Fecha_Pago'])
                    data = json.dumps(listaClientes, cls=Client_Encoder, indent=7)
                    conn.send(data.encode('utf-8'))
                    print(len(listaClientes))
                except Exception as e:
                    print('Hubo un error2', e)
                #data = 'send'
                #conn.send(data.encode())
            if (tipo == 2):
                print('realizar pago')

                    #data = input(' -> ')  # el mensaje que se envia de regreso
                    #conn.send(data.encode())  # enviar el mensaje

            conn.close()
        except Exception as e:
            print('Hubo un error 1', e)


if __name__ == '__main__':
    server_program()
