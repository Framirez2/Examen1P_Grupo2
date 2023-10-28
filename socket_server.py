import socket
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Configuración del socket server
host = socket.gethostname()  # Dirección del servidor
port = 5000  # Puerto del servidor

# Configuración de la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sa1e1"
)

# Crear un socket server
server_socket = socket.socket()
server_socket.bind((host, port))  # Vincular el socket a la dirección y puerto

# Escuchar conexiones entrantes
server_socket.listen()
print(f"Servidor escuchando en {host}:{port}")



while True:
    # Aceptar conexiones entrantes
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida desde {client_address}")
        client1_socket, client_address = server_socket.accept()

        # Recibir datos del socket cliente
        data = client_socket.recv(1024).decode()
        print(f"Datos recibidos del cliente: {data}")

        data1= client1_socket.recv(1024).decode()
        print(f' {data1}')


        # Cerrar la conexión con el cliente
        client_socket.close()
        client1_socket.close()
    except Exception as e:
        print(f"Error en la conexión con el cliente: {e}")

# Cerrar el socket server
server_socket.close()

