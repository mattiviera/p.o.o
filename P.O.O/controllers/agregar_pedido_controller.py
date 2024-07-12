from services.pedido_service import PedidoService

class AgregarPedidoController:
    def __init__(self):
        self.pedido_service = PedidoService()

    def agregar_pedido(self, pedido):
        self.pedido_service.agregar_pedido(pedido)