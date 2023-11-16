# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proyecto_javier_empresas_contratadoras(models.Model):
    _name = 'proyecto_javier.empresas_contratadoras'
    _description = 'proyecto_javier.empresas_contratadoras'

    name = fields.Char(string="Nombre empresa")
    contact_name = fields.Char(string="Nombre del contacto")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefono")
    address1 = fields.Char(string="Direccion 1")
    address2 = fields.Char(string="Direccion 2")
