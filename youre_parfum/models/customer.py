from odoo import api, fields, modedels


class customorder(models.Model):
    _name = 'youre.customer'
    _description = 'Data customer parfum'

    nama = fields.Char(string='nama customer')
    ukuran = fields.Interger(string='ukuran parfum')
    tipe = fields.Selection(string='tipe parfum', selection=[('cewe','Cewe'), ('cowo','Cowo'), ('unisex','Unisex')])
    jumlah = fields.Interger(string='jumlah parfum')
    harga = fields.Interger(string='harga parfum')