from odoo import models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def validate_quota(self):
        for line in self.order_line:
            quota = line.product_id.sales_quotas_id
            # No se chequea que el producto de la sale.order sea el mismo
            # que el de la quota dado que se llega a esta a traves del product
            if self.team_id == quota.sales_team_ids \
                and quota.start_date < self.date_order.date() < quota.end_date:
                if line.product_uom_qty > quota.sales_quota:
                    raise ValidationError(
                        _("Sale can't be confirmed as it exceeds the sales quota for product %s" % line.product_id.name)
                    )
        return True

    def action_confirm(self):
        if self.validate_quota():
            for line in self.order_line:
                quota = line.product_id.sales_quotas_id
                quota.quantity_sold += line.product_uom_qty
            return super(SaleOrder, self).action_confirm()
