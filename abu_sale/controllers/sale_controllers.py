from odoo import http
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
import json

class ProductsController(http.Controller):
    @http.route('/api/products', type='http', auth='none', methods=['GET'], csrf=False)
    def get_products(self, **kw):
        product_model = request.env['product.template'].sudo()
        product_ids = product_model.search([])
        if product_ids:
            products_data = []
            for product in product_ids:
                products_data.append({
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'list_price': product.list_price,
                    'standard_price': product.standard_price,
                    'type': product.type,
                    'categ_id': product.categ_id.id,
                    'uom_id': product.uom_id.id,
                    'uom_po_id': product.uom_po_id.id,
                    'taxes_id': [tax.id for tax in product.taxes_id],
                    'supplier_taxes_id': [tax.id for tax in product.supplier_taxes_id],
                    'barcode': product.barcode,
                    'default_code': product.default_code,
                    'active': product.active,
                    'sale_ok': product.sale_ok,
                    'purchase_ok': product.purchase_ok
                })
            return json.dumps({
                'status': 200,
                'data': products_data
            })

