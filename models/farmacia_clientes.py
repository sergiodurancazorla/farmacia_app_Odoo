from odoo import fields, models
from odoo.exceptions import ValidationError

class clientes(models.Model):
    _name = 'farmacia.clientes'
    _description = 'clientes'

    id_clientes = fields.Char(required=True)

    pedidosV = fields.Many2one(
        'farmacia.pedidosventa',
        string = 'Pedidos',
        ondelete = 'restrict',
    )

    informacion = fields.Text()
    telefono = fields.Char()
    email = fields.Text()
    saldo = fields.Char()