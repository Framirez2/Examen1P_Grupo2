import socket
from datetime import date

import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date

host = socket.gethostname()  # as both code is running on same pc
port = 5000  # socket server port number

# Crear un socket cliente
client_socket = socket.socket()

client1_socket = socket.socket()

def fetch_data_from_database(client_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sa1e1"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tblexa WHERE  Id_Cliente = %s", (client_id,))
    result = cursor.fetchall()
    db.close()
    return result

def display_data():
    def search():
        client_id = entry.get()
        result = fetch_data_from_database(client_id)
        for i in tree.get_children():
            tree.delete(i)
        for row in result:
            tree.insert("", "end", values=row)

    def clear():
        entry.delete(0, tk.END)
        for i in tree.get_children():
            tree.delete(i)

    def reversar():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("ERROR", f"Ningún elemento seleccionado")
            return
        
        fecha1 = tree.item(selected_item)['values'][4]
        cliente1_id = tree.item(selected_item)['values'][0]
        cuota_1 = tree.item(selected_item)['values'][1]
        referencia1 = tree.item(selected_item)['values'][6]
        estado = tree.item(selected_item)['values'][5]

        if fecha1 == 'None':
            messagebox.showwarning("Error", "La fecha es nula (None) o está vacía.")
            return

        if estado == 'C':
            valor = "00"
            reference_message = "exitoso"
        elif estado == 'P':
            valor = "01"
            reference_message = "con error"

        confirmation = messagebox.askyesno("Confirmar reversión", f"¿Desea reversar la cuota {cuota_1}  del cliente {cliente1_id}?")
        if confirmation:

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sa1e1"
            )
            cursor = db.cursor()
            try:
                trama = f"Codigo de Cliente:{cliente1_id} Referencia:{referencia1}"
                client_socket = socket.socket()
                client_socket.connect((host, port))
                client_socket.send(trama.encode())
                client_socket.close()


                reference_code = "XBLN-" + (valor)  # Generate the reference code
                # Agregar código de referencia y cambiar el estado a 00 exitoso
                fecha1 = datetime.strptime(fecha1, '%Y-%m-%d').date()
                messagebox.showinfo("Informacion", f"Referencia de Base de Datos {reference_code} {reference_message}")
                cursor.execute("UPDATE tblexa SET Fecha_Pago_Realizacion = Null, Referencia = %s, Estado='P' WHERE Cuota = %s and Id_cliente = %s and fecha_Pago_Realizacion = %s",
                            (reference_code, cuota_1, cliente1_id, date.today()))
                db.commit()
                success_message=""
                if fecha1 < date.today():
                    messagebox.showwarning("Error", f"La fecha ya ha pasado, no se puede reversar el pago {reference_code} {reference_message}")
                else:
                    # Enviar mensaje al servidor
                    success_message = f"Referencia de Base de Datos {reference_code}  {reference_message}"

                client1_socket = socket.socket()
                client1_socket.connect((host, port))
                client1_socket.send(success_message.encode())
                client1_socket.close()


            except mysql.connector.Error as err:
                valor = "01"
                messagebox.showerror("Error", f"Referencia de Base de Datos {reference_code} {reference_message}")

            except ConnectionRefusedError:
               messagebox.showerror("Error", f"No se pudo establecer una conexión con el servidor.Porfavor ejecute el servidor")
            finally:
                db.close()
            search()



    root = tk.Tk()
    root.geometry("1500x400")

    label = tk.Label(root, text="Ingrese el Id del Cliente a buscar: ")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Buscar", command=search)
    button.pack()

    clear_button = tk.Button(root, text="Limpiar", command=clear)
    clear_button.pack()

    reversar_button = tk.Button(root, text="Reversar", command=reversar)
    reversar_button.pack()

    tree = ttk.Treeview(root, columns=("Id Cliente", "Cuota", "Monto", "Fecha_Pago", "Pago_Fecha_Realizacion", "Estado", "Referencia"), show="headings")
    tree.heading("#1", text="Id Cliente")
    tree.heading("#2", text="Cuota")
    tree.heading("#3", text="Monto")
    tree.heading("#4", text="Fecha_Pago")
    tree.heading("#5", text="Pago_Fecha_Realizacion")
    tree.heading("#6", text="Estado")
    tree.heading("#7", text="Referencia")

    tree.column("#1", anchor=tk.CENTER)
    tree.column("#2", anchor=tk.CENTER)
    tree.column("#3", anchor=tk.CENTER)
    tree.column("#4", anchor=tk.CENTER)
    tree.column("#5", anchor=tk.CENTER)
    tree.column("#6", anchor=tk.CENTER)
    tree.column("#7", anchor=tk.CENTER)
    tree.pack()

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

    root.mainloop()

    client_socket.close()
    client1_socket.close()



if __name__ == '__main__':
    display_data()
