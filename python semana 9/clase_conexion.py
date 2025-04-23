import mysql.connector

class conexion:
    def _init_(self):
        self.user= "root"
        self.password=""
        self.database="tienda"
        self.host= "localhost"

    def hacer_conexion ():
        conexion = mysql.conector.connect(host="localhost",database = "tienda", user = "root", password = "")
        if conexion.is_connected ():
            print("conexion exitosa....")
        else:
            print ("conexion fallida......")
        return conexion