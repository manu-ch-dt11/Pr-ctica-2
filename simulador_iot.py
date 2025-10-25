"""
=================================================

Fecha:      24 de octubre de 2025

=================================================
==           INTEGRANTES DEL EQUIPO            ==
=================================================

- CORDOBA HERNANDEZ JOSE MANUEL
- HERNANDEZ MALDONADO CRISTIAN GAEL
- SOLANO GONZALES JOSUE
- ROMERO GARCIA DANIEL ALBERTO 
- PENSADO PAREDES FREDY EMMANUEL

=================================================
"""

import random

# --- 1. CLASE BASE ---
class DispositivoIoT:
    def __init__(self, id_dispositivo: str):
        self.__id_dispositivo = id_dispositivo
        self.__estado = False  # False = apagado, True = encendido

    @property
    def id_dispositivo(self) -> str:
        return self.__id_dispositivo

    @property
    def estado(self) -> str:
        return "Encendido" if self.__estado else "Apagado"

    def encender(self):
        self.__estado = True

    def apagar(self):
        self.__estado = False

    def mostrar_datos(self):
        print(f"--- ID: {self.id_dispositivo} ({self.__class__.__name__}) ---")
        print(f"  Estado: {self.estado}")

# --- 2. SUBCLASES (HERENCIA) ---

class SensorTemperatura(DispositivoIoT):
    def __init__(self, id_dispositivo: str, temp_inicial: float = 20.0):
        super().__init__(id_dispositivo)
        self.__temperatura = temp_inicial
        self.encender()

 @property
    def temperatura(self) -> float:
        return self.__temperatura

    def leer_temperatura(self) -> float:
        """Simula una lectura de sensor."""
        self.__temperatura += random.uniform(-1.5, 1.5)
        self._temperatura = max(10.0, min(40.0, self._temperatura))
        # CORRECCIÓN: Añadido print para ver la lectura
        print(f"  [Sensor {self.id_dispositivo}] lee: {self.temperatura:.2f}°C")
        return self.__temperatura

    def mostrar_datos(self):
        """Sobrescribe método base (Polimorfismo)."""
        super().mostrar_datos()
        print(f"  Lectura: {self.temperatura:.2f}°C")
