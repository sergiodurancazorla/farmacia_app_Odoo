from odoo import fields, models


class Stock(models.Model):
    _name = 'farmacia.stock'
    _description = 'Stock'

    inventario = fields.Integer()

    # atributos relacionados, rellenar más adelante
    codigo_nacional = fields.Integer()
    proveedor = fields.Text()
    coste_proveedor = fields.Integer()
    coste_venta = fields.Integer()
