from odoo import models, fields, api


class curso(models.Model):
    _name = 'odoo_pruebas_relaciones.curso'
    _description = 'Curso académico'

    name = fields.Char(string="Curso Académico")

    def anho_get(self):
        resultado = []
        for rexistro in self:
            if rexistro.anho:
                resultado.append((rexistro.id, str(rexistro.anho)))
            else:
                resultado.append((rexistro.id, str(rexistro.name)))
        return resultado
