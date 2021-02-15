from odoo import fields, models

class pedidoscompra(models.Model):
    _name = 'farmacia.pedidoscompra'
    _description = 'pedidoscompra'
    _order = 'estado asc'

    id_pedidosC = fields.Char(default=None,
                     index=True,
                     readonly=False,
                     required=True,
                     translate=False)
    descripcion = fields.Text('descripcion')
    lista_productos = fields.Text('lista')
    filtro_estado = fields.Char('estado')

    proveedor_id = fields.One2many(
        'farmacia.proveedores',
        'pedidosP',
        string='Pedidos al proveedor', readonly=True,
    )

    productos_pedido = fields.Many2one(
        'farmacia.producto',
        string = 'Producto',
        ondelete= 'restrict',
    )