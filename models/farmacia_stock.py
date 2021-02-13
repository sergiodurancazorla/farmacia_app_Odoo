from odoo import fields, models, api


class Stock(models.Model):
    _name = 'farmacia.stock'
    _description = 'Stock'

    inventario = fields.Integer()

    # Referencia a producto
    producto_codigo_nacional = fields.Many2one(
        'farmacia.producto',
        string='Producto',
        ondelete='restrict')

    # Bloquear stock no se pueden hacer ventas de este producto
    bloquear = fields.Boolean('Bloqueado', readonly=True)

    # Campo relacionados
    proveedor = fields.Text()

    # Costes:
    coste_proveedor = fields.Integer()
    coste_venta = fields.Integer()

    def bloquearProducto(self):
        """Bloquea un producto y no se pueden hacer pedidos"""
        action = {}
        if self.bloquear:
            self.bloquear = False
            action = {
                'name': 'Desbloquear producto',
            }
        else:
            self.bloquear = True

        return action
