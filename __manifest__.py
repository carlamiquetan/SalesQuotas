# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{

    "name": "Sales Quotas",
    "summary": """
        This module manages sales quotas by product and by sales team.
    """,
    "author": "Carla Miquetan",
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["product", "crm", "sale"],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_quotas.xml',
        'views/sales_quota_action.xml',
        'reports/sales_quotas_report.xml',
        'reports/sales_quotas_report_template.xml',
    ],

}
