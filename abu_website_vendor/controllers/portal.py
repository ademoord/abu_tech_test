from odoo.addons.portal.controllers import portal
from odoo.http import request


class CustomerPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'contact_count' in counters:
            values['contact_count'] = request.env['res.partner'] \
                .sudo().search_count(
                [('parent_id', '=', request.env.user.partner_id.id)])
        return values
