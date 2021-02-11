from odoo import fields, models, api

from . import farmacia_stock


class Producto(models.Model):
    _name = 'farmacia.producto'
    _description = 'Producto'

    name = fields.Char('Nombre',
                       default=None,
                       index=True,
                       help='Nombre del producto',
                       readonly=False,
                       required=True,
                       translate=False, )

    codigo_nacional = fields.Integer()
    descripcion = fields.Text()
    imagen = fields.Image()


