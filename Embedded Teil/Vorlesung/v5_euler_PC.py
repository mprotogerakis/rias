import asyncio
from typing import Tuple

# Parameter
k: float = -1.0  # Konstante in der DGL
dt: float = 0.01  # Zeitschrittweite

# Anfangsbedingungen
x: float = 1.0  # Anfangsposition
v: float = 0.0  # Anfangsgeschwindigkeit

async def euler_step() -> None:
    """Führt einen Schritt des Euler-Verfahrens durch, um die Differentialgleichung zu lösen."""
    global x, v
    while True:
        # Berechne die Beschleunigung a = k * x
        a: float = k * x
        
        # Berechne die neue Position und Geschwindigkeit mit dem Euler-Verfahren
        x_new: float = x + v * dt
        v_new: float = v + a * dt
        
        # Aktualisiere die aktuellen Werte
        x, v = x_new, v_new
        
        # Warte für dt Sekunden, bevor der nächste Schritt durchgeführt wird
        await asyncio.sleep(dt)

async def main() -> None:
    """Startet den Euler-Solver und gibt die Ergebnisse regelmäßig aus."""
    # Starte den Euler-Solver als Hintergrundaufgabe
    asyncio.create_task(euler_step())
    
    # Hauptschleife zur regelmäßigen Ausgabe der aktuellen Position und Geschwindigkeit
    while True:
        print(f"x: {x:.6f}, v: {v:.6f}")
        await asyncio.sleep(1)  # Ausgabe jede Sekunde

if __name__ == "__main__":
    # Starte das Hauptprogramm
    asyncio.run(main())
