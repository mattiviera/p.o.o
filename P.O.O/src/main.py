#%%
from controllers.agregar_pedido_controller import AgregarPedidoController
from controllers.listar_pedidos_controller import ListarPedidosController
from domain.pedido import Pedido

def main():
    print("Iniciando la aplicación...")

    listar_pedidos_controller = ListarPedidosController()
    agregar_pedido_controller = AgregarPedidoController()

    listar_pedidos_controller._next_controller = agregar_pedido_controller

    pedido_nuevo = Pedido(id=1, cliente="Juan", productos=["Producto A", "Producto B"])
    listar_pedidos_controller.listar_pedidos()

    print("Finalizando la aplicación.")

if __name__ == "__main__":
    main()
# %%
