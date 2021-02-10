from odoo import fields, models


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
    inventario = fields.Integer()

    # atributos relacionados, rellenar más adelante
    proveedor = fields.Text()
    coste_proveedor = fields.Integer()
    coste_venta = fields.Integer()
