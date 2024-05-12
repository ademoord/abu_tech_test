# -*- coding: utf-8 -*-
# from odoo import http


# class AbuSale(http.Controller):
#     @http.route('/abu_sale/abu_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abu_sale/abu_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abu_sale.listing', {
#             'root': '/abu_sale/abu_sale',
#             'objects': http.request.env['abu_sale.abu_sale'].search([]),
#         })

#     @http.route('/abu_sale/abu_sale/objects/<model("abu_sale.abu_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abu_sale.object', {
#             'object': obj
#         })
