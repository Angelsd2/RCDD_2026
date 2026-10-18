import os
import socket
import time

import grpc

import saludo_pb2
import saludo_pb2_grpc
import  socket

# Nombre del contenedor servidor dentro de la red de Docker
SERVIDOR = os.environ.get("SERVIDOR", "servidor:50051")
CLIENTE_ID = os.environ.get("CLIENTE_ID",socket.gethostname())
#agregar otro cliente y que los identifique cual es cada uno
def ciclo2():
    canal = grpc.insecure_channel(SERVIDOR)
    stub = saludo_pb2_grpc.SaludoStub(canal)
    nombre = socket.gethostname()

    cnt = 0
    while True:
        # wait_for_ready espera a que el servidor esté disponible
        r = stub.Decir(saludo_pb2.Peticion(nombre=f"{nombre} #{cnt}"), wait_for_ready=True)
        print(f"{cnt}: {r.mensaje}")
        cnt += 1
        time.sleep(1)

def ciclo():
    canal = grpc.insecure_channel(SERVIDOR)
    stub = saludo_pb2_grpc.SaludoStub(canal)
    nombre = socket.gethostname()

    cnt = 0
    while True:
        # wait_for_ready espera a que el servidor esté disponible
        r = stub.Decir(saludo_pb2.Peticion(nombre=f"{nombre} #{cnt}"), wait_for_ready=True)
        print(f"{cnt}: {r.mensaje}")
        cnt += 1
        time.sleep(1)

def ciclo2():
    canal = grpc.insecure_channel(SERVIDOR)
    stub = saludo_pb2_grpc.SaludoStub(canal)
    nombre = socket.gethostname()

    cnt = 0
    while True:
        # wait_for_ready espera a que el servidor esté disponible
        r = stub.Decir(saludo_pb2.Peticion(nombre=f"{nombre} #{cnt}"), wait_for_ready=True)
        print(f"{cnt}: {r.mensaje}")
        cnt += 1
        time.sleep(1)

if __name__ == "__main__":
    ciclo()
