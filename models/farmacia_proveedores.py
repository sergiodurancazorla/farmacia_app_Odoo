from odoo import fields, models


class Proveedores(models.Model):
    _name = 'farmacia.proveedores'
    _description = 'Proveedores'

    name = fields.Char('Nombre')

    pedidosP = fields.One2many(
        'farmacia.pedidoscompra',
        'proveedorC',
        string='Pedidos',
        ondelete='restrict',
    )
    imagen = fields.Image()
    descripcion = fields.Text()
    email = fields.Text()
    telefono = fields.Text()
