from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    offered_products = fields.Char(string='Produk yang Ditawarkan')

    @api.depends('is_company', 'name', 'parent_id.display_name', 'type',
                 'company_name')
    def _compute_display_name(self):
        names = dict(self.with_context({}).name_get())
        for partner in self:
            if partner.website_id:
                partner.display_name = partner.name
            else:
                partner.display_name = names.get(partner.id)
