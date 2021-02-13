from odoo import fields, models, api
from odoo.exceptions import ValidationError

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

    codigo_nacional = fields.Integer('Codigo nacional',
                                     default=None,
                                     index=True,
                                     help='Codigo nacional',
                                     readonly=False,
                                     required=True,
                                     translate=False,
                                     )

    descripcion = fields.Text()
    imagen = fields.Image()

    # metodo que verifica que el codigo nacional sea correcto
    @api.constrains('codigo_nacional')
    def checkCodigoNacional(self):
        if not self.codigo_nacional or len(self.codigo_nacional) != 6:
            raise ValidationError('El codigo nacional debe tener 6 numeros')


