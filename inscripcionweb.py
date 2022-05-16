#PROGRAMA PARA INSCRIBIR ALUMNOS VÍA WEB

import pywebio
import pymongo
import pprint

from pywebio.platform.flask import webio_view
from flask import Flask


#import argparse
#from pywebio import start_server

from pywebio.input import * 
from pywebio.output import *
from pymongo import MongoClient


app = Flask(__name__)


cliente = MongoClient('localhost', port=27017)

db = cliente.Inscripcion_web

coleccion = db.datos_alumno



def carga_datos():
    
    img = open('img/sistema-inscripcion-web.jpg', 'rb').read()  
    put_image(img, width='1000px')

    

    datos = input_group("Datos generales del alumno",[
       
       input('Apellido paterno', name='paterno'),
       input('Apellido materno', name='materno'),
       input('Nombre', name='nombre'),
       input('Año de nacimiento', name='edad', type=NUMBER)
    ])

    put_text(datos['paterno'], datos['materno'], datos['nombre'], datos['edad'],)

    registro = {

        'Ap.paterno': datos['paterno'],
        'Ap.materno': datos['materno'],
        'Nombre': datos['nombre'],
        'Edad': datos['edad']
    }

    coleccion.insert_one(registro)
        

def domicilio():

    

    datos = input_group("Datos del domicilio",[
       
       input('Apellido paterno', name='paterno'),
       input('Apellido materno', name='materno'),
       input('Nombre', name='nombre'),
       input('Año de nacimiento', name='edad', type=NUMBER)
    ])

    put_text(datos['paterno'], datos['materno'], datos['nombre'], datos['edad'],)


def cargar_archivos():

    imgs = file_upload("Select some pictures:", accept="image/*", multiple=True)
    for img in imgs:
        put_image(img['content'])



def imprimir_ficha():
    print("En esta funcion se deberá imprimir la ficha del alumno")

def consulta_datos():
    
   
    consulta = (coleccion.find_one({"Nombre": "ZAHIR"}))
    
    #pprint.pprint(consulta)
    put_text(consulta)

    
"""
    put_markdown('El nombre del alumno es: `%s` `%s` `%s`' % (ap_paterno, ap_materno, nombre))
"""

# `task_func` is PyWebIO task function
app.add_url_rule('/tool', 'webio_view', webio_view(carga_datos),
            methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(carga_datos, port=args.port)



#app.run(host='localhost', port=80)   

#if __name__ == '__main__':
    
    #carga_datos()
    #domicilio()
    #cargar_archivos()
    #consulta_datos()
   
