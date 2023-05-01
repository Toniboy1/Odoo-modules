from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    supplier_product_code = fields.Char(
        string='Supplier Product Code',
        compute='_compute_supplier_product_code'
    )

    @api.depends('product_id', 'order_id.partner_id')
    def _compute_supplier_product_code(self):
        for line in self:
            supplier = line.order_id.partner_id
            supplierinfo = line.product_id.seller_ids.filtered(lambda s: s.partner_id == supplier)
            line.supplier_product_code = supplierinfo[:1].product_code or ''

