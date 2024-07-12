from services.pedido_service import PedidoService

class ListarPedidosController:
    def __init__(self, next_controller=None):
        self.pedido_service = PedidoService()
        self._next_controller = next_controller

    def listar_pedidos(self):
        pedidos = self.pedido_service.listar_pedidos()
        for pedido in pedidos:
            print(f"ID: {pedido.id} - Cliente: {pedido.cliente} - Productos: {', '.join(pedido.productos)}")

        if self._next_controller:
            self._next_controller.listar_pedidos()
            