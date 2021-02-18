from . import models
from odoo import api, fields, tools


def add_datos_prueba(cr, registry):
    tools.convert_file(cr, 'farmacia_app_Odoo', 'data/farmacia.producto.csv', None, mode='init', noupdate=True,
                       kind='init', report=None)
