# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "OCR for documents",
    "version": "8.0.1.0.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Knowledge Management",
    "summary": "Run character recognition on uploaded files",
    "depends": [
        'document',
    ],
    "data": [
        "data/ir_cron.xml",
        "data/ir_config_parameter.xml",
    ],
    "external_dependencies": {
        'bin': [
            'tesseract',
        ],
    },
}
