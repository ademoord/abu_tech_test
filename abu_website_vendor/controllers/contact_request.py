from odoo import http
from odoo.http import request

class WebsiteCustomerContact(http.Controller):
    @http.route('/contact_request_form', type="http", website=True, auth='public')
    def contact_request_form(self):
        return http.request.render(
            "abu_website_vendor.website_customer_contact_request_form",
            {
                'contact_title': request.env['res.partner.title'].sudo().search([]),
                'country_id': request.env['res.country'].sudo().search([]),
                'state_id': request.env['res.country.state'].sudo().search([]),
            })

    @http.route('/contact_request_form/submit', type="http", website=True,
                auth='public')
    def contact_request_form_completed(self, **kw):
        kw['parent_id'] = request.env.user.partner_id.id
        kw['website_id'] = request.website.id
        request.env['res.partner'].sudo().create(kw)
        return request.render(
            "abu_website_vendor."
            "website_customer_contact_request_form_completed")

    @http.route('/contact_request_form/write', type="http", website=True,
                auth='public')
    def contact_request_form_edit(self, **kw):
        current_contact = request.env['res.partner'].sudo().browse(
            int(kw['id']))
        current_contact.write(kw)
        return request.render(
            "abu_website_vendor"
            ".website_customer_contact_request_form_completed", {})
