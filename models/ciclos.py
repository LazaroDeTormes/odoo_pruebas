from odoo import models, fields, api


class ciclos(models.Model):
    _name = 'odoo_pruebas_relaciones.ciclos'
    _description = 'Ciclos'

    name = fields.Char(string="Ciclo")