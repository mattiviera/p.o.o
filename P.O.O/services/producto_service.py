from dao.producto_dao import ProductoDAO

class ProductoService:
    def __init__(self):
        self.producto_dao = ProductoDAO()

    def agregar_producto(self, producto):
        self.producto_dao.agregar_producto(producto)

    def listar_productos(self):
        return self.producto_dao.listar_productos()