from odoo import api, fields, modedels


class customorder(models.Model):
    _name = 'youre.customorder'
    _description = 'Data custom parfum'

    aroma = fields.Char(string='aroma parfum')
    ukuran = fields.Interger(string='ukuran parfum')
    tahan = fields.Char(string='ketahanan parfum')
    tipe = fields.Selection(string='tipe parfum', selection=[('cewe','Cewe'), ('cowo','Cowo'), ('unisex','Unisex')])
    jumlah = fields.Interger(string='jumlah parfum')