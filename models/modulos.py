from odoo import models, fields, api


class modulos(models.Model):
    _name = 'odoo_pruebas_relaciones.modulos'
    _description = 'Módulos'

    name = fields.Char(string="modulo")