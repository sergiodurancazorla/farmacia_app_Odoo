from odoo import fields, models, api
from odoo.exceptions import *


class Pedidoscompra(models.Model):
    _name = 'farmacia.pedidoscompra'
    _description = 'pedidoscompra'

    descripcion = fields.Text('descripcion')
    # lista_productos = fields.Text('lista')
    filtro_estado = fields.Selection([('pendiente', 'Pendiente de pago'), ('pagado', 'Pagado')], 'estado')
    coste_pedido = fields.Integer('coste')

    proveedorC = fields.Many2one(
        'farmacia.proveedores',
       # 'pedidosP',
        string='Pedidos al proveedor', ondelete='restrict', required=True,
    )

    productos_pedido = fields.Many2many(
        'farmacia.producto',
        string='producto',
        ondelete='restrict',
        required=True,
    )
    #deberia verificar si se ha puesto un producto
    @api.constrains('productos_pedido')
    def comprobarProductosPedido(self):
        if not self.productos_pedido:
            raise ValidationError('Debe de añadir un producto')

    #deberia verificar si se ha elegido un proveedor
    @api.constrains('proveedorC')
    def comprobarProveedor(self):
        if not self.proveedorC:
            raise ValidationError('Debe escoger un proveedor')