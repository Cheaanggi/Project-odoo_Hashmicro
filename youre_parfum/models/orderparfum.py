from odoo import api, fields, modedels


class orderparfum(models.Model):
    _name = 'youre.orderparfum'
    _description = 'Data order parfum'

    nama = fields.Char(string='nama parfum')
    ukuran = fields.Interger(string='ukuran parfum')
    tahan = fields.Char(string='ketahanan parfum')
    tipe = fields.Selection(string='tipe parfum', selection=[('cewe','Cewe'), ('cowo','Cowo'), ('unisex','Unisex')])
    stock = fields.Interger(string='stock parfum')
    harga = fields.Interger(string='harga parfum')