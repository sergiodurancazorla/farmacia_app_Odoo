from odoo import fields, models


class Pedidoscompra(models.Model):
    _name = 'farmacia.pedidoscompra'
    _description = 'pedidoscompra'
    _order = 'estado asc'

    descripcion = fields.Text('descripcion')
    # lista_productos = fields.Text('lista')
    filtro_estado = fields.Selection([('pendiente', 'Pendiente de pago'), ('pagado', 'Pagado')], 'estado')
    coste_pedido = fields.Integer('coste')

    proveedor = fields.One2many(
        'farmacia.proveedores',
        'pedidosP',
        string='Pedidos al proveedor', readonly=True,
    )

    productos_pedido = fields.Many2one(
        'farmacia.producto',
        string='Producto',
        ondelete='restrict',
    )
