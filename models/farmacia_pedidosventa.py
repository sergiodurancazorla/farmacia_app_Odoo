from odoo import fields, models
from odoo.exceptions import ValidationError

class pedidosventa(models.Model):
    _name = 'farmacia.pedidosventa'
    _description = "pedidosventa"

    clientes_id = fields.One2many(
        'farmacia.clientes',
        'pedidosV',
        string='Pedidos del cliente',
        readonly=True,
    )

    estado = fields.Text()

