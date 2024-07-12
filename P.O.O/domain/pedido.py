class Pedido:
    def __init__(self, id, cliente, productos):
        self.id = id
        self.cliente = cliente
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __repr__(self):
        return f'Pedido(id={self.id}, cliente={self.cliente}, productos={self.productos})'