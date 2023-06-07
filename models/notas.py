from odoo import models, fields, api


class notas(models.Model):
    _name = 'odoo_pruebas_relaciones.notas'
    _description = 'Notas'



    quenda = fields.Selection([('Ordinario','Ordinario'), ('Vespertino','Vespertino'), ('FPDual','FPDual')], string='Quenda')
    curso = fields.Selection([("1º",'1º'), ("2º",'2º')], string="Curso")
    nota = fields.Integer(string="Nota", max=10, min=0)
    nota_txt = fields.Text(compute="_notaTxt", store=True, string='Nota texto: ', size="15")

    anho = fields.Many2one('odoo_pruebas_relaciones.curso', ondelete="cascade", required=True)
    ciclo = fields.Many2one('odoo_pruebas_relaciones.ciclos', ondelete="cascade", required=True)
    modulo = fields.Many2one('odoo_pruebas_relaciones.modulos', ondelete="cascade", required=True)

    many = fields.Many2many('odoo_pruebas_relaciones.profesores',
                            string="notas profesores",
                            relation="odoo_basido_notas_profesores",
                            column1="nota", columns2="profesor")

    @api.depends('nota')
    def _notaTxt(self):
        try:
            for registro in self:
                if registro.nota == 0 or registro.nota <= 4:
                    registro.nota_txt = "Suspenso"
                elif registro.nota == 5:
                    registro.nota_txt = "Suficiente"
                elif registro.nota == 6:
                    registro.nota_txt = "Bien"
                elif registro.nota == 7 or registro.nota == 8:
                    registro.nota_txt = "Notable"
                elif registro.nota == 9 or registro.nota == 10:
                    registro.nota_txt = "Sobresaliente"
        except Exception as error:
            print(error)