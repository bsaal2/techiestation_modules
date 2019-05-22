# -*- coding: utf-8 -*-
from odoo.addons.website.controllers.main import Website
from odoo import http
from odoo.http import request


class Home(http.Controller):
    @http.route('/home', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.home')

class Mobile(http.Controller):
    @http.route('/mobile', auth='public', website=True)
    def home(self, **kw):
        mobile = http.request.env["t.posts"]
        return http.request.render('techiestation.mobile',{
            'mobilelist' : mobile.search([])
        })    

class Tablet(http.Controller):
    @http.route('/tablet', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.tablet')      

class Laptop(http.Controller):
    @http.route('/laptop', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.laptop')    

class Camera(http.Controller):
    @http.route('/camera', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.camera') 

class Design(http.Controller):
    @http.route('/design', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.design')

class Detail(http.Controller):
    @http.route('/detail', auth='public', website=True)
    def detail(self, **kw):
        return http.request.render('techiestation.detail') 

class Connect(http.Controller):
    @http.route('/connect', auth='public', website=True)
    def detail(self, **kw):
        return http.request.render('techiestation.connect')

class TechieStationHome(Website):
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        homepage = request.website.homepage_id
        if homepage and (
                homepage.sudo().is_visible or request.env.user.has_group('base.group_user')) and homepage.url == '/':
            return http.request.render('techiestation.home')

        website_page = request.env['ir.http']._serve_page()
        if website_page:
            return website_page
        else:
            top_menu = request.website.menu_id
            first_menu = top_menu and top_menu.child_id and top_menu.child_id.filtered(lambda menu: menu.is_visible)
            if first_menu and first_menu[0].url not in ('/', '') and (
                    not (first_menu[0].url.startswith(('/?', '/#', ' ')))):
                return http.request.render('techiestation.home')

        raise request.not_found()       