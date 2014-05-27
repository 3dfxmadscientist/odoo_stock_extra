# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
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

import time
from openerp.osv import fields, orm

class stock_picking(orm.Model):
    _inherit = 'stock.picking'

    _columns = {
       'user_id': fields.related('sale_id', 'user_id', type='many2one', relation='res.users', string='Salesperson', readonly=True, store=True),
    }
# Seems to be so buggy, if I put user_id
# if I put it only in stock.picking, I cannot display it on the views
# so I have to duplicate it in both models...
class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'

    _columns = {
       'user_id': fields.related('sale_id', 'user_id', type='many2one', relation='res.users', string='Salesperson', readonly=True, store=True),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: