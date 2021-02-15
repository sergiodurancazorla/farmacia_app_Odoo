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

    proveedor_id = fields.Many2one('farmacia.proveedores', string='Proveedor', ondelete='restrict')