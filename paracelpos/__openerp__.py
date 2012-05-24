##############################################################################
#
# Copyright (c) 2012 RiTH-Tech (http://rith-tech.com). All Right Reserved
#
# Author : Huy Doan (huy.doan@rith-tech.com)
#
##############################################################################

{
    "name": "Paracel POS",
    "version": "0.4",
    "category": "Point Of Sale",
    "images": ["images/paracelpos.png"],
    "author": "RiTH-Tech",
    "description": """This module provides extra functions to make POS working as a backend for Paracel POS""",
    "website" : "http://www.rith-tech.com",    
    'depends': ['point_of_sale'],
    'init_xml': [],
    'update_xml': [
	'paracelpos_view.xml',
	'security/ir.model.access.csv',
    ],
    'demo_xml': [
    ],
    'installable': True,
    'application': False,
}
