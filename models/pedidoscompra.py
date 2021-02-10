from odoo import fields, models

class pedidoscompra(models.Model):
    _name = 'pedidoscompra'
    _description = 'pedidoscompra'
    _order = 'estado asc'

    id = fields.Textext(default=None,
                     index=True,
                     readonly=False,
                     required=True,
                     translate=False)
    descripcion = fields.Text('descripcion')
    lista_productos = fields.Text('lista')
    filtro_estado = fields.Text('estado')

    proveedor_id = fields.Many2one('proveedor', string='Publisher')