# -*- coding: utf-8 -*-
import logging
from odoo.addons.website.controllers.main import Website
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class Home(http.Controller):
    @http.route('/home', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('techiestation.home')

class Mobile(http.Controller):
    @http.route('/mobile', auth='public', website=True)
    def home(self, **kw):
        mobile = http.request.env["t.posts"]
        return http.request.render('techiestation.mobile',{
            'mobilelist' : mobile.search([('category','=','mobile')],offset=2,order='create_date desc')
        })    

class Tablet(http.Controller):
    @http.route('/tablet', auth='public', website=True)
    def home(self, **kw):
        tablet = http.request.env["t.posts"]
        return http.request.render('techiestation.tablet',{
            'tabletlist' : tablet.search([('category','=','tablet')],order='create_date desc')
        })      

class Laptop(http.Controller):
    @http.route('/laptop', auth='public', website=True)
    def home(self, **kw):
        laptop = http.request.env["t.posts"]
        return http.request.render('techiestation.laptop',{
            'laptoplist' : laptop.search([('category','=','laptop')],order='create_date desc')
        })    

class Camera(http.Controller):
    @http.route('/camera', auth='public', website=True)
    def home(self, **kw):
        camera = http.request.env["t.posts"]
        return http.request.render('techiestation.camera',{
            'cameralist' : camera.search([('category','=','camera')],order='create_date desc')
        }) 

class Design(http.Controller):
    @http.route('/design', auth='public', website=True)
    def home(self, **kw):
        design = http.request.env["t.posts"]
        return http.request.render('techiestation.design',{
            'designlist' : design.search([('category','=','design')],order='create_date desc')
        })

class Detail(http.Controller):
    @http.route('/detail/<model("t.posts"):post>', auth='public', website=True)
    def detail(self, post):
        return http.request.render('techiestation.detail',{
            "post" : post
        }) 

class Connect(http.Controller):
    @http.route('/connect', auth='public', website=True)
    def detail(self, **kw):
        return http.request.render('techiestation.connect')

class Test(http.Controller):
    @http.route('/test/<model("t.posts"):post>', auth='public', website=True)
    def test(self, post):
        _logger.warn("========== POST =======" + str(post) ) 
        return "<h1>{}</h1>".format(post.name)

class TechieStationHome(Website):
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        slider = http.request.env["t.posts"].search([('is_slider','=',True)])

        mobileTop = http.request.env["t.posts"].search([('category','=','mobile')],order='create_date desc',limit=2)
        mobileDown = http.request.env["t.posts"].search([('category','=','mobile')],offset=2,order='create_date desc',limit=3)
        
        tabletTop = http.request.env["t.posts"].search([('category','=','tablet')],order='create_date desc',limit=2)
        tabletDown = http.request.env["t.posts"].search([('category','=','tablet')],offset=2,order='create_date desc',limit=3)

        cameraTop = http.request.env["t.posts"].search([('category','=','camera')],order='create_date desc',limit=2)
        cameraDown = http.request.env["t.posts"].search([('category','=','camera')],offset=2,order='create_date desc',limit=3)

        laptopTop = http.request.env["t.posts"].search([('category','=','laptop')],order='create_date desc',limit=2)
        laptopDown = http.request.env["t.posts"].search([('category','=','laptop')],offset=2,order='create_date desc',limit=3)

        designTop = http.request.env["t.posts"].search([('category','=','design')],order='create_date desc',limit=2)
        designDown = http.request.env["t.posts"].search([('category','=','design')],offset=2,order='create_date desc',limit=3)

        data = {
            'sliderlist' : slider,
            'mobileTop' : mobileTop,
            'mobileDown' : mobileDown,
            'tabletTop' : tabletTop,
            'tabletDown' : tabletDown,
            'cameraTop' : cameraTop,
            'cameraDown' : cameraDown,
            'laptopTop' : laptopTop,
            'laptopDown' : laptopDown,
            'designTop' : designTop,
            'designDown' : designDown
        }

        homepage = request.website.homepage_id
        if homepage and (
                homepage.sudo().is_visible or request.env.user.has_group('base.group_user')) and homepage.url == '/':
            return http.request.render('techiestation.home',{
                'data' : data
            })

        website_page = request.env['ir.http']._serve_page()
        if website_page:
            return website_page
        else:
            top_menu = request.website.menu_id
            first_menu = top_menu and top_menu.child_id and top_menu.child_id.filtered(lambda menu: menu.is_visible)
            if first_menu and first_menu[0].url not in ('/', '') and (
                    not (first_menu[0].url.startswith(('/?', '/#', ' ')))):
                return http.request.render('techiestation.home',{
                    'data' : data,
                })

        raise request.not_found()       