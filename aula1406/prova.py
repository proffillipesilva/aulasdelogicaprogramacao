class Prova:
    def __init__(self, id: int, materia: str, conceito: float):
        self._id = id
        self._materia = materia
        self._conceito = conceito

    def get_conceito(self):
        return self._conceito

