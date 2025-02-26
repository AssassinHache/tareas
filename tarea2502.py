from vpython import *
import asyncio
import keyboard
import random 

scene = canvas(title="Combinación de Conceptos en VPython", width=800, height=600)

def crear_esferas(posicion, radio, n):
    if n == 0:
        return
    esfera = cone(pos=posicion, axis=vector(0, 1.5, 0), radius=radio, color=color.blue)
    crear_esferas(posicion + vector(1.5 * radio, 0, 0), radio * 0.8, n - 1)

crear_esferas(vector(-5, 0, 0), 1, 5)

def aleatorio():
    return vector( random.random(),random.random(),random.random())
   
def crear_cilindro(posicion, radio, n):
    if n == 0:
        return
    esfera = cylinder(pos=posicion, axis=vector(0, 1, 0), radius=radio, color=color.blue)
    crear_cilindro(posicion + vector(0 , 1.5, 0),  0.9, n - 1)

crear_cilindro(vector(1, 0, 0), 1, 5)


async def mover_objeto(objeto, eje):
    while True:
        objeto.pos += eje * 0.1
        if objeto.pos.x > 2 or objeto.pos.y > 2 or objeto.pos.z > 2:
            objeto.pos = vector(-5, 0, 0)
        await asyncio.sleep(0.1)

cubo = cone(pos=vector(-2, 0, 0), axis=vector(0, 1.5, 0), radius=1, color=color.red)

async def mover_objeto2(objeto, eje):
    while True:
        objeto.pos += eje * 0.1
        if objeto.pos.x > 4 or objeto.pos.y > 2 or objeto.pos.z > 2:
            objeto.pos = vector(1, 0, 0)
        await asyncio.sleep(0.1)

esfera = cylinder(pos=vector(1, 0, 0), axis=vector(0, 1, 0), radius=1, color=color.green)

async def main():
    task1 = asyncio.create_task(mover_objeto(cubo, vector(1, 0, 1)))
    task2 = asyncio.create_task(mover_objeto2(esfera, vector(1,0 , 1)))

    while True:
        await asyncio.sleep(0.1)
        if keyboard.is_pressed("t"):
                cubo.color = aleatorio()
                esfera.color = aleatorio()
        if keyboard.is_pressed("r"):
            cubo.pos = vector(-5, 0, 0)
            esfera.pos = vector(1, 0, 0)

asyncio.run(main())
