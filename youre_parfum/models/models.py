# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class youre_parfum(models.Model):
#     _name = 'youre_parfum.youre_parfum'
#     _description = 'youre_parfum.youre_parfum'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
