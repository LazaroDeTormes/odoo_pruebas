from odoo import models, fields, api


class notas(models.Model):
    _name = 'odoo_pruebas_relaciones.profesores'
    _description = 'Profesores'

    name = fields.Char(string="Profesor")