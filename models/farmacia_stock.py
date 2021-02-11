from odoo import fields, models


class Stock(models.Model):
    _name = 'farmacia.stock'
    _description = 'Stock'

    inventario = fields.Integer()

    # Referencia a producto
    producto_codigo_nacional = fields.Many2one(
        'farmacia.producto',
        string='Producto',
        ondelete='restrict')

    # Campo relacionados
    proveedor = fields.Text()

    # Costes:
    coste_proveedor = fields.Integer()
    coste_venta = fields.Integer()

