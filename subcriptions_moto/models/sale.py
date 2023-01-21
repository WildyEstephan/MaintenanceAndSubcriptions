from odoo import api, fields, models

class Sale(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):

        super().action_confirm()

        lines = self.order_line.filtered(lambda r: r.is_for_subscription)

        for line in lines:
            self.create_subscription_package(line)

    def create_subscription_package(self, line):

        sub = self.env['subscription.package'].create({
            'subscription_plan': line.subscription_plan_id.id,
            'partner_id': line.order_id.partnert_id.id,
        })



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_for_subscription = fields.Boolean(
        string='Is For Subscription',
        required=False, realted='product_id. is_for_subscription')
    subscription_plan_id = fields.Many2one(
        comodel_name='subscription.plan',
        string='Subscription Plan',
        required=False)

