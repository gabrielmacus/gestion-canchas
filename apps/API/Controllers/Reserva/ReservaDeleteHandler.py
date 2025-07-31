from src.Administracion.Reservas.Application.UseCases.EliminarReservaUseCase import EliminarReservaUseCase
from src.Administracion.Reservas.Domain.Services.ReservaFinder import ReservaFinder
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Reservas.Infraestructure.Services.SAReservaRepository import SAReservaRepository

class ReservaDeleteHandler():
    def __init__(self):
        self._repository = SAReservaRepository(SAConnection().get_engine())
        self._reserva_finder = ReservaFinder(self._repository)
        self._eliminar_reserva_usecase = EliminarReservaUseCase(self._repository, self._reserva_finder)
    
    def delete(self, id: str):
        self._eliminar_reserva_usecase.execute(id) 