import uasyncio as asyncio

# Parameter
k = -1.0   # Konstante in der DGL
dt = 0.01 # Zeitschrittweite

# Anfangsbedingungen
x = 1.0   # Anfangsposition
v = 0.0   # Anfangsgeschwindigkeit

async def euler_step():
    global x, v
    while True:
        # Euler-Schritt
        a = k * x
        x_new = x + v * dt
        v_new = v + a * dt
        x, v = x_new, v_new

        # Warte für dt Sekunden
        await asyncio.sleep(dt)

async def main():
    # Starte den Euler-Solver
    asyncio.create_task(euler_step())

    # Weitere Aufgaben können hier hinzugefügt werden
    while True:
        print(f"x: {x}, v: {v}")
        await asyncio.sleep(1)

# Starte das Programm
asyncio.run(main())
