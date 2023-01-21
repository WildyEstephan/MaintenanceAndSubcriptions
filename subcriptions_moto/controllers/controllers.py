# -*- coding: utf-8 -*-
# from odoo import http


# class SubcriptionsMoto(http.Controller):
#     @http.route('/subcriptions_moto/subcriptions_moto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subcriptions_moto/subcriptions_moto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('subcriptions_moto.listing', {
#             'root': '/subcriptions_moto/subcriptions_moto',
#             'objects': http.request.env['subcriptions_moto.subcriptions_moto'].search([]),
#         })

#     @http.route('/subcriptions_moto/subcriptions_moto/objects/<model("subcriptions_moto.subcriptions_moto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subcriptions_moto.object', {
#             'object': obj
#         })
