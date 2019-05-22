# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Posts(models.Model):
    _name = 't.posts'
    _description = "Posts"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Post name")
    title = fields.Char(string='Post title')
    is_slider = fields.Boolean(string="Is Slider ?", default=False)
    slider_image = fields.Binary(string="Slider Image", attachment="true")
    slider_summary = fields.Text(string="Slider summary")
    description = fields.Html(string="Description")
    thumbnail = fields.Binary(string="Thumbnail", attachment="true", help="Please upload the size of 100 * 100")
    category = fields.Selection([('mobile','Mobile'),('tablet','Tablet'),('laptop','Laptop'),('camera','Camera'),('design','Design')], string="Category")