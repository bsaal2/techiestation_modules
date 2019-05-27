# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tag(models.Model):
    _name = 't.tag'
    _description = "News Tag"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Tag Name')
    description = fields.Text(string='Description')