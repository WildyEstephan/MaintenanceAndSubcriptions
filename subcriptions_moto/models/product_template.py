from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_for_subscription = fields.Boolean(
        string='Is For Subscription',
        required=False)
    service_subscription = fields.Many2one(
        comodel_name='product.template',
        string='Service Subscription',
        required=False)
