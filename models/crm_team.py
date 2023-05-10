from odoo import _, fields, models
class CrmTeam(models.Model):
    _inherit = "crm.team"

    crm_team_id = fields.Many2one('sales.quotas', string=_('Sales Team'))
