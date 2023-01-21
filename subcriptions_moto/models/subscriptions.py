from odoo import api, fields, models, _
from datetime import datetime
from dateutil.relativedelta import relativedelta

class SubscriptionPackage(models.Model):
    _name = 'subscription.package'
    _description = 'Subscription Package'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        required=False)
    to_renewal = fields.Boolean(
        string='To Renewal',
        required=False, default=True, tracking=True)
    subscription_plan_id = fields.Many2one(
        comodel_name='subscription.plan',
        string='Subscription Plan',
        required=True, tracking=True)
    start_date = fields.Date(
        string='Start Date',
        required=False)
    next_invoice_date = fields.Date(
        string='Next Invoice Date',
        required=False, tracking=True)
    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale',
        required=False)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=False, tracking=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),
                   ('progress', 'Progress'),
                   ('close', 'Close'),
                   ],
        required=False, tracking=True, deafult='new')
    invoice_ids = fields.One2many(
        comodel_name='account.move',
        inverse_name='subscription_id',
        string='Invoice',
        required=False)
    invoice_count = fields.Integer(
        string='Invoice Count',
        required=False)

    @api.model
    def create(self, values):
        # Add code here

        if values.get('name', _('New')) == _('New'):
            values['name'] = self.env['ir.sequence']. \
                                 next_by_code('subscription.package') or _('New')

        return super().create(values)

    def start_package(self):

        self.start_date = datetime.today()

    @api.depends('start_date')
    def _compute_next_invoice_date(self):

        for rec in self:
            if rec.state == 'progress':
                rec.next_invoice_date = self.start_date + relativedelta(days=self.subscription_plan_id.renewal_time)

