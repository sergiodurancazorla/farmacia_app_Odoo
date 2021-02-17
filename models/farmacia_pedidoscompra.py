from odoo import fields, models


class Pedidoscompra(models.Model):
    _name = 'farmacia.pedidoscompra'
    _description = 'pedidoscompra'
    _order = 'estado asc'

    _rec_name = 'id_pedidosC'
    descripcion = fields.Text('descripcion')
    # lista_productos = fields.Text('lista')
    filtro_estado = fields.Char('estado')
    coste_pedido = fields.Integer('coste')

    proveedor_id = fields.One2many(
        'farmacia.proveedores',
        'pedidosP',
        string='Pedidos al proveedor', readonly=True,
    )

    productos_pedido = fields.Many2one(
        'farmacia.producto',
        string='Producto',
        ondelete='restrict',
    )
