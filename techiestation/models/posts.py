# -*- coding: utf-8 -*-
import textwrap
from odoo import models, fields, api

class Posts(models.Model):
    _name = 't.posts'
    _description = "Posts"
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Post name")
    title = fields.Char(string='Post title', help='This title is to display on the hot news section')
    is_slider = fields.Boolean(string="Is Slider ?", default=False)
    slider_active = fields.Boolean(string="Active slider ?", help='This field keeps the track of the slider which is active')
    slider_image = fields.Binary(string="Slider Image", attachment="true", help="The size of this image should be 2668 * 1500 pixels")
    slider_summary = fields.Text(string="Slider summary")
    description = fields.Html(string="Description")
    sub_description = fields.Html(string='Sub Description', compute='_compute_description', help='This description is computed because to show it in website')
    thumbnail = fields.Binary(string="Thumbnail", attachment="true", help="Please upload the size of 640 * 427 pixels")
    category = fields.Selection([('mobile','Mobile'),('tablet','Tablet'),('laptop','Laptop'),('camera','Camera'),('design','Design')], string="Category")
    tag_id = fields.Many2one('t.tag', string='Tag')

    @api.multi
    @api.depends('description')
    def _compute_description(self):
        for record in self:
            if record.description:
                record.sub_description = textwrap.shorten(record.description, width=600) + "..."