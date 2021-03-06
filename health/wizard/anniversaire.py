# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 EVERLIBRE All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import wizard
import pooler

dates_form = '''<?xml version="1.0"?>
<form string="Select period">
    <field name="datedebut" colspan="4"/>
    <field name="datefin" colspan="4"/>
</form>'''

dates_fields = {
    'datedebut': {'string': 'Début', 'type': 'date', 'required': True},
    'datefin': {'string': 'Fin', 'type': 'date', 'required':True}
}

class wizard_report(wizard.interface):
    def _get_defaults(self, cr, uid, data, context):
        pool = pooler.get_pool(cr.dbname)
        period_obj = pool.get('account.period')
        periode = period_obj.find(cr, uid)[0]
        debut= period_obj.read(cr,uid,periode)['date_start']
        fin= period_obj.read(cr,uid,periode)['date_stop']
        data['form']['datedebut'] =debut
        data['form']['datefin'] =fin
        return data['form']

    states = {
        'init': {
            'actions': [_get_defaults],
            'result': {'type':'form', 'arch':dates_form, 'fields':dates_fields, 'state':[('end','Cancel'),('report','Print')]}
        },
        'report': {
            'actions': [],
            'result': {'type':'print', 'report':'health.anniversaire.report', 'state':'end'}
        }
    }
wizard_report('health.anniversaire.report')

