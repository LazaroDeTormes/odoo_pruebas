# -*- coding: utf-8 -*-
# from odoo import http


# class OdooPruebasRelaciones(http.Controller):
#     @http.route('/odoo_pruebas_relaciones/odoo_pruebas_relaciones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_pruebas_relaciones/odoo_pruebas_relaciones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_pruebas_relaciones.listing', {
#             'root': '/odoo_pruebas_relaciones/odoo_pruebas_relaciones',
#             'objects': http.request.env['odoo_pruebas_relaciones.odoo_pruebas_relaciones'].search([]),
#         })

#     @http.route('/odoo_pruebas_relaciones/odoo_pruebas_relaciones/objects/<model("odoo_pruebas_relaciones.odoo_pruebas_relaciones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_pruebas_relaciones.object', {
#             'object': obj
#         })
