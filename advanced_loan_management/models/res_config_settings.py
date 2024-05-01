# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Megha (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Add new fields to display service products"""
    _inherit = 'res.config.settings'

    interest_product_id = fields.Many2one('product.product',
                                          string="Interest Product",
                                          config_parameter="advanced_loan_management.interest_product_id",
                                          help="Product For Interest "
                                               "To Create Invoice Lines")
    repayment_product_id = fields.Many2one('product.product',
                                           string="Repayment Product",
                                           config_parameter="advanced_loan_management.repayment_product_id",
                                           help="Product For Repayment "
                                                "To Create Invoice Lines")
    interest_account_id = fields.Many2one('account.account', string="Interest Account",
                                          config_parameter='advanced_loan_management.interest_account_id',
                                          default=lambda self: self.env['account.account'].search([('code', 'ilike', '200011')]),
                                          help="Account to be used for interest (200111 liability_current)")
    repayment_account_id = fields.Many2one('account.account', string="Repayment Account",
                                           config_parameter='advanced_loan_management.repayment_account_id',
                                           default=lambda self: self.env['account.account'].search([('code', 'ilike', '200012')]),
                                           help="Account to be used for repayment (200112 asset_cash)")
