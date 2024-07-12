from dao.pedido_dao import PedidoDAO

class PedidoService:
    def __init__(self):
        self.pedido_dao = PedidoDAO()

    def agregar_pedido(self, pedido):
        self.pedido_dao.agregar_pedido(pedido)

    def listar_pedidos(self):
        return self.pedido_dao.listar_pedidos()