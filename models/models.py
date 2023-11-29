# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProyectoJavierEmpresasContratadoras(models.Model):
    _name = 'proyecto_javier.empresas_contratadoras'
    _description = 'proyecto_javier.empresas_contratadoras'

    name = fields.Char(string="Nombre empresa")
    contact_name = fields.Char(string="Nombre del contacto")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefono")
    address1 = fields.Char(string="Direccion 1")
    address2 = fields.Char(string="Direccion 2")
    employees_number = fields.Integer(string='Número de empleados')
    business_type = fields.Char(string="Tipo de empresa", compute='_compute_business_type')

    @api.depends('employees_number')
    def _compute_business_type(self):
        for record in self:
            if record.employees_number:
                record.business_type = {
                    record.employees_number <= 10: 'Pequeña',
                    10 < record.employees_number <= 50: 'Mediana',
                    record.employees_number > 50: 'Grande'
                }.get(True, False)
            else:
                record.business_type = False

