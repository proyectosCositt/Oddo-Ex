# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MiModelo(models.Model):
    _name = 'mi_modulo.mi_modelo'
    _description = 'Modelo de ejemplo'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    date = fields.Date(string='Fecha', default=fields.Date.today)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado', default='borrador')
    
    @api.model
    def create(self, vals):
        res = super(MiModelo, self).create(vals)
        # Lógica personalizada al crear registros
        return res
    
    def action_confirmar(self):
        for record in self:
            record.state = 'confirmado'
    
    def action_cancelar(self):
        for record in self:
            record.state = 'cancelado'
    
    def action_borrador(self):
        for record in self:
            record.state = 'borrador' 