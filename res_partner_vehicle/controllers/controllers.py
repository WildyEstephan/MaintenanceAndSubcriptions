# -*- coding: utf-8 -*-
# from odoo import http


# class ResPartnerVehicle(http.Controller):
#     @http.route('/res_partner_vehicle/res_partner_vehicle', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_partner_vehicle/res_partner_vehicle/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_partner_vehicle.listing', {
#             'root': '/res_partner_vehicle/res_partner_vehicle',
#             'objects': http.request.env['res_partner_vehicle.res_partner_vehicle'].search([]),
#         })

#     @http.route('/res_partner_vehicle/res_partner_vehicle/objects/<model("res_partner_vehicle.res_partner_vehicle"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_partner_vehicle.object', {
#             'object': obj
#         })
