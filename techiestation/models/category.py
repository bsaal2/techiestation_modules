# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Category(models.Model):
    _name = 't.category'
    _description = "Category"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Category Name')
    description = fields.Text(string='Description')