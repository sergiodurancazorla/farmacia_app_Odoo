from odoo import fields, models, api

class Proveedores(models.Model):
    _name = 'farmacia.proveedores'
    -description = 'Proveedores'

    id_proveedores = fields.Char(required=True)

    pedidosP =  fields.Many2one(
        'farmacia.pedidoscompra',
        string='Pedidos',
        ondelete='restrict',
    )

    descripcion = fields.Text()
    email = fields.Text()
    telefono = fields.Char()