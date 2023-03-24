from odoo import fields, models

class FiskaltrustModel(models.Model):
    _inherit = 'pos.config'

    _isFiskaltrust = fields.Boolean("fiskaltrust")    
    _cashboxId = fields.Char('cashbox_id', required=False)
    _accessToken = fields.Char('access_token', required=False)
    _baseUrl = fields.Char('baseurl', required=False)

