class PedidoDAO:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.pedidos