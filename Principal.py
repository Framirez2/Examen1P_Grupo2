import socket
import sys
from tkinter import *
from tkinter import ttk
import json

from Cliente import Cliente

v = Tk()
v.title('Consultas y Pagos')
v.geometry('900x650')


def buscarCliente():
    host = '127.0.0.1'
    port = 5002

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        id = ide.get()
        tipo = 1
        #while True:
            # print('data')
        s.sendall(str.encode("\n".join([str(id), str(tipo)])))
        data = s.recv(2048).decode('utf-8')

        try:
            datos = json.loads(data)

            if isinstance(datos, list):
                listaClientes = []

                for item in datos:
                    cliente = Cliente()
                    cliente.setID(item['ID'])
                    cliente.setCuota(item['Cuota'])
                    cliente.setMonto(item['Monto'])
                    cliente.setFechaP(item['Fecha_Pago'])
                    cliente.setFechaPR(item['Fecha_Pago_Realizacion'])
                    cliente.setEstado(item['Estado'])
                    cliente.setReferencia(item['Referencia'])
                    listaClientes.append(cliente)
                    print(item['Fecha_Pago'])
            id = ide.get()
            tipo = 1
            s.close()
            for i in listaClientes:
                print(i.Fecha_Pago)
        except json.JSONDecodeError as e:
            print('Error parsing', e)

    except Exception as e:
        print('Hubo un error de conexion', e)


lblID = Label(v, text="ID del cliente a buscar").place(x=20, y=20)
global ide
ide = StringVar()
txtID = ttk.Entry(v, textvariable=ide).place(x=200, y=20)
btnSearch = Button(v, text="Buscar", command=buscarCliente).place(x=380, y=15)

v.mainloop()
