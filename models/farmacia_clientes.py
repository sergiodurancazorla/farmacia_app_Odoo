from odoo import fields, models
from odoo.exceptions import *


class clientes(models.Model):
    _name = 'farmacia.clientes'
    _description = 'clientes'

    name = fields.Char('Nombre')

    pedidosV = fields.One2many(
        'farmacia.pedidosventa',
        'clienteCL',
        string='Pedidos',
        ondelete='restrict',
    )
    informacion = fields.Text()
    telefono = fields.Char()
    email = fields.Text()
    saldo = fields.Char()

