from odoo import fields, models, api
from odoo.exceptions import *


class pedidosventa(models.Model):
    _name = 'farmacia.pedidosventa'
    _description = "pedidosventa"

    estado = fields.Text([('preparandose', 'Pedido en elaboración'), ('reparto', 'Pedido en reparto'), ('entregado', 'Pedido entregado')])
    descripcion = fields.Text('descripcion')

    clienteCL = fields.Many2one(
        'farmacia.clientes',
        #'pedidosV',
        string='Pedidos del cliente',
        ondelet='restrict',
        required=True,
    )

    productos_pedido = fields.Many2many(
        'farmacia.producto',
        string='producto',
        ondelete='restrict',
        required=True,
    )

    #Veremos si se ha añadido un producto
    @api.constrains('productos_pedido')
    def comprobarPedidosYProductos(self):
        if not self.productos_pedido:
            raise ValidationError('Debe de añadir un producto')

    #Verificamos si hay un proveedor elegido
    @api.constrains('clienteCL')
    def comprobarEleccionProveedor(self):
        if not self.clienteCL:
            raise ValidationError('Debe escoger un proveedor')





