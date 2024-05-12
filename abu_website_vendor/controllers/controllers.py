# -*- coding: utf-8 -*-
# from odoo import http


# class AbuWebsiteVendor(http.Controller):
#     @http.route('/abu_website_vendor/abu_website_vendor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abu_website_vendor/abu_website_vendor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abu_website_vendor.listing', {
#             'root': '/abu_website_vendor/abu_website_vendor',
#             'objects': http.request.env['abu_website_vendor.abu_website_vendor'].search([]),
#         })

#     @http.route('/abu_website_vendor/abu_website_vendor/objects/<model("abu_website_vendor.abu_website_vendor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abu_website_vendor.object', {
#             'object': obj
#         })
