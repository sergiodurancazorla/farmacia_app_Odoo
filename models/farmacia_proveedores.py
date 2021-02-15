from odoo import fields, models, api

class Proveedores(models.Model):
    _name = 'farmacia.proveedores'
    -description = 'Proveedores'

    id_proveedores = fields.Char(required=True)

    pedidos =  fields.One2many(
        'farmacia.pedidoscompra',
        'id_pedidosC',
        string = 'Pedidos del proveedor', readonly="True",)

    descripcion = fields.Text()
    email = fields.Text()
    telefono = fields.Char()