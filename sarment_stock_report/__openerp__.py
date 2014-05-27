# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: LIN Yu <lin.yu@elico-corp.com>
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
    'name': ' Warehouse Reports',
    'version': '0.1',
    'category': 'Sales',
    'sequence': 19,
    'summary': 'Stock Reports for Sarment',
    'description': """
Customize Stock Reports:
==================================================

* Display quantities in stock report.
* Display signature, total quanties, date in stock report.
* Display clearly full path of 'location from' and full path of 'location to' on all picking move line form
* Add to delivery order list view the  "salesperson" from the related SO document, and add on search view of delivery order. 
    """,
    'author': 'Elico',
    'website': 'http://www.elico-corp.com',
    'images': [],
    'depends': ['sale_stock','stock'],
    'data': [
        'stock_report.xml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
