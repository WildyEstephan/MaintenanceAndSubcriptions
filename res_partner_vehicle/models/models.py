# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner_vehicle(models.Model):
    _inherit = 'res.partner'

    vehicle_id = fields.One2many('fleet.vehicle', compute="_fleet_vehicle_compute")
    
    @api.depends('vehicle_id')
    def _fleet_vehicle_compute(self):
        fleet_id = self.env['fleet.vehicle'].search([('driver_id', '=', self.id)])
        for rec in self:
            if fleet_id:
                rec.vehicle_id = fleet_id
            else:
                self.vehicle_id = rec.vehicle_id
