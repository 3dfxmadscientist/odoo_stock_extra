# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time
from openerp.report import report_sxw


class picking(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(picking, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_total_qty': self.get_total_qty,
            'get_product_desc': self.get_product_desc,
        })

    def get_total_qty(self, picking):
        #qty = sum([x.product_qty for x in picking.move_lines])
        qty = 0
        for x in picking.move_lines:
            if x.state not in ['cancel']:
                qty += x.product_qty
        # decimal = "%.%ff" %3
        # for decimal precision, manual fix for the moment
        return "%.3f" %qty

    def get_product_desc(self, move_line):
        desc = move_line.product_id.name
        if move_line.product_id.default_code:
            desc = '[' + move_line.product_id.default_code + ']' + ' ' + desc
        return desc

for suffix in ['', '.in', '.out']:
    report_sxw.report_sxw('report.stock.picking.list.sarment' + suffix,
                          'stock.picking' + suffix,
                          'addons/sarment_stock_report/report/picking.rml',
                          parser=picking)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
