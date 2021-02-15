from odoo import fields, models


class Proveedores(models.Model):
    _name = 'farmacia.proveedores'
    _description = 'Proveedores'

    name = fields.Char('Nombre')
    id_proveedores = fields.Char(required=True)

    pedidosP = fields.Many2one(
        'farmacia.pedidoscompra',
        string='Pedidos',
        ondelete='restrict',
    )
    imagen = fields.Image()
    descripcion = fields.Text()
    email = fields.Text()
    telefono = fields.Text()
