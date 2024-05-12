from odoo import http
from odoo.http import request


class CustomerContacts(http.Controller):
    @http.route(['/my/contacts'], type='http', auth='public', website=True)
    def view_customer(self):
        customer_contact = request.env['res.partner'].sudo().search(
            [('parent_id', '=', request.env.user.partner_id.id)])
        return request.render(
            'abu_website_vendor.website_customer_contact',
            {'customer_contact_portal': customer_contact,
             'page_name': 'customer_contact'})

    @http.route(['/my/contacts/<int:contact>'], type='http', auth='public',
                website=True)
    def view_customer_details(self, contact):
        customer_contact = request.env['res.partner'].sudo().search(
            [('parent_id', '=', request.env.user.partner_id.id),
             ('id', '=', contact)])
        return request.render(
            'abu_website_vendor.website_customer_contact_detail',
            {'customer_contact_portal': customer_contact,
             'page_name': 'customer_contact_details'})
