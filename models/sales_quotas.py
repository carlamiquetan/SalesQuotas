from odoo import _, api, fields, models
class SalesQuotas(models.Model):
    _name = "sales.quotas"
    _description = "Sales Quotas"

    sales_team_ids = fields.One2many(comodel_name="crm.team", inverse_name="crm_team_id", string="Sales Team",
                                     required=True)
    product_ids = fields.One2many(comodel_name="product.product", inverse_name="sales_quotas_id", string="Product", required=True)
    start_date = fields.Date("Start Date", required=True)
    end_date = fields.Date("End Date", required=True)
    sales_quota = fields.Integer("Sales Quota", required=True)
    quantity_sold = fields.Integer("Quantity Sold")
    quantity_available = fields.Integer("Quantity Available", compute = "_compute_quantity_available")

    @api.depends("sales_quota", "quantity_sold")
    def _compute_quantity_available(self):
        for rec in self:
            rec.quantity_available = (
                    rec.sales_quota - rec.quantity_sold
            )
