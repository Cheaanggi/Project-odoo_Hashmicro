# -*- coding: utf-8 -*-
# from odoo import http


# class YoureParfum(http.Controller):
#     @http.route('/youre_parfum/youre_parfum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/youre_parfum/youre_parfum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('youre_parfum.listing', {
#             'root': '/youre_parfum/youre_parfum',
#             'objects': http.request.env['youre_parfum.youre_parfum'].search([]),
#         })

#     @http.route('/youre_parfum/youre_parfum/objects/<model("youre_parfum.youre_parfum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('youre_parfum.object', {
#             'object': obj
#         })
