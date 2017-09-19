# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_sale_delay = fields.Float('Tiempo entrega (dias)',related='product_id.sale_delay', store=True)

