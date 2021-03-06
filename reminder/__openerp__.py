#!/usr/bin/env python
#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    d$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Reminder",
    "version" : "1.0",
    "depends" : ["base"],
    "description": """Reminder Services
    * based on domain and conditions it will call server action
    """,
    'author': 'Tiny',
    'website': 'http://www.openerp.com',   
    'init_xml': [],
    'update_xml': [
        "reminder_view.xml",
        "reminder_data.xml"
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
