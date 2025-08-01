class UniqueIdViolationException(Exception):
    def __init__(self):
        super().__init__("El id que se intenta agregar ya existe")