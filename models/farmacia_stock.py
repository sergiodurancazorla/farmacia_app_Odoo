from odoo import fields, models, api
from odoo.exceptions import *


class Stock(models.Model):
    _name = 'farmacia.stock'
    _description = 'Stock'
    inventario = fields.Integer(required=True)
    _rec_name = 'producto_codigo_nacional'

    # Referencia a producto
    producto_codigo_nacional = fields.Many2one(
        'farmacia.producto',
        string='Producto',
        ondelete='restrict',
    )

    # Bloquear stock no se pueden hacer ventas de este producto
    bloquear = fields.Boolean('Bloqueado', readonly=True)

    # Campo relacionados
    proveedor = fields.Text()

    # Costes:
    coste_proveedor = fields.Integer()
    coste_venta = fields.Integer()

    inventario_total = fields.Integer()


    def bloquearProducto(self):
        """Bloquea un producto y no se pueden hacer pedidos"""
        if self.bloquear:
            self.bloquear = False

        else:
            self.bloquear = True

    # metodo que verifica que el inventario sea mayor a 0
    @api.constrains('inventario')
    def comprobarInventario(self):
        if self.inventario < 0:
            raise ValidationError('El stock del producto debe ser mayor o igual 0 ')

    # metodo que verifica si se ha puesto un producto
    @api.constrains('producto_codigo_nacional')
    def comprobarProducto(self):
        if not self.producto_codigo_nacional:
            raise ValidationError('Debe de añadir un producto')


