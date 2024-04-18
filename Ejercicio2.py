class Mision:
    def __init__(self, tipo, reino_destino, dios_solicitante):
        self.tipo = tipo
        self.reino_destino = reino_destino
        self.dios_solicitante = dios_solicitante
        self.recursos = {'Valkirias': 0, 'Unidades': 0}

    def es_prioritaria(self):
        return self.dios_solicitante in ['Odín', 'Loki']

    def asignar_recursos(self):
        if self.es_prioritaria():
            self.recursos['Valkirias'] = 10
            self.recursos['Unidades'] = 50
        else:
            recursos_por_tipo = [
                ('Defensa', {'Valkirias': 5, 'Unidades': 20}),
                ('Exploración', {'Valkirias': 3, 'Unidades': 10}),
                ('Conquista', {'Valkirias': 7, 'Unidades': 30})
            ]
            for tipo, recursos in recursos_por_tipo:
                if tipo == self.tipo:
                    self.recursos.update(recursos)
                    break

class GestorDeMisiones:
    def __init__(self):
        self.misiones = []

    def agregar_mision(self, tipo, reino, dios):
        mision = Mision(tipo, reino, dios)
        mision.asignar_recursos()
        self.misiones.append(mision)

    def mostrar_recursos(self):
        for mision in self.misiones:
            print(f"Misión a {mision.reino_destino} ({mision.tipo}):")
            for recurso, cantidad in mision.recursos.items():
                print(f"  {recurso.capitalize()} asignadas: {cantidad}")

def mostrar_recursos_asignados(misiones):
    for mision in misiones:
        print(f"Misión a {mision.reino_destino} ({mision.tipo}):")
        for recurso, cantidad in mision.recursos.items():
            print(f"  {recurso.capitalize()} asignadas: {cantidad}")

def agregar_misiones():
    gestor = GestorDeMisiones()

    while True:
        tipo = input("Ingrese el tipo de misión (Defensa, Exploración, Conquista): ")
        reino = input("Ingrese el reino destino: ")
        dios = input("Ingrese el dios que solicita la misión: ")
        gestor.agregar_mision(tipo, reino, dios)
        mostrar_recursos_asignados(gestor.misiones)

        continuar = input("¿Desea agregar otra misión? (s/n): ")
        if continuar.lower() != 's':
            break

agregar_misiones()