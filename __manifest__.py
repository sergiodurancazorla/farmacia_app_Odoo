{
    'name': 'Farmacia y Parafarmacia APP',
    'description': 'Control de almacen, gestion de pedidos y productos farmaceuticos y de parafarmacia',
    'author': 'Sergio Duran, Sara Andres, Sergio Martinez',
    'depends': ['base'],
    'application': True,
    'post_init_hook': 'add_datos_prueba',
    'post_init_hook': 'add_datos_proveedores',
    'data': [
        'security/ir.model.access.csv',
        'views/farmacia_menu.xml',
        'views/producto_view.xml',
        'views/stock_view.xml',
        'views/proveedores_view.xml',
        'views/pedidoscompra_view.xml',
    ],
    'demo': [
        'data/farmacia.producto.csv',
        'data/farmacia.proveedores.csv',
    ]

}
