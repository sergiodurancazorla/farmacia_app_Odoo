from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Producto(models.Model):
    _name = 'farmacia.producto'
    _description = 'Producto'
    _rec_name = 'name'

    name = fields.Char('Nombre',
                       default=None,
                       index=True,
                       help='Nombre del producto',
                       readonly=False,
                       required=True,
                       translate=False, )

    inventario = fields.One2many(
        'farmacia.stock',  # modelo relacionado
        'producto_codigo_nacional',  # nombre del campo en el modelo relacionado
        string='Inventario Total', readonly=True, )

    inventario_total = fields.Integer(compute='_compute_calcularTotal', readonly=True)

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

    #
    @api.depends('inventario', 'inventario_total')
    def _compute_calcularTotal(self):
        if not self.inventario :
            self.inventario_total = 0
        else:
            for record in self.inventario:
                self.inventario_total = self.inventario_total + record.inventario
