from odoo import _, fields, models
class Product(models.Model):
    _inherit = "product.product"

    sales_quotas_id = fields.Many2one('sales.quotas', string=_('Product'))
