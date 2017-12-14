# -*- coding: utf-8 -*-
##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones
#    (<http://https://www.trey.es>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Product Ratings",
    "summary": "Valoracion de productos en la tienda online",
    "version": '8.0.0.1',
    "author": 'Trey Kilobytes de Soluciones (https://www.trey.es)',
    "website": "https://www.trey.es",
    "category": "Website",
    "description": """
Puede mostrarse el widget activando la opción de personalización "Product
Ratings" tanto desde el listado como desde la ficha de producto.

O bien, no activar dichos widgets e insertarlos mediante la llamada <t
t-call="website_ratings.widget"> en nuestro código para ubicarlos en cualquier
posición dentro de la página.
""",
    'license': "AGPL-3",
    'depends': [
        "base",
        "website",
        "website_sale",
        "website_ratings"
    ],
    'data': [
        'views/website_sale_product_ratings.xml'
    ],
    'demo': [
    ],
    'auto_install': False,
    'installable': True,
    'images': [

    ],
}