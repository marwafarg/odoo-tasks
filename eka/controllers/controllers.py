# from odoo import http
#
#
# class partner(http.Controller):
#     @http.route(['/api/partner/'],auth='public',csrf=False,type='json',methods=['POST'])
#     def create_sale(self, **kw):
#         print(http.request)
#         print(kw)
#         new_partner = http.request.env['res.partner'].sudo().create(kw)
#         if new_partner:
#             return "partner is created"
#         else:
#             return "no partner request"
# #



  # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class PartnerForm(http.Controller):
    # mention class name
    @http.route(['/customer/form'], type='http', auth="public", website=True)
    #mention a url for redirection.
    #define the type of controller which in this case is ‘http’.
    #mention the authentication to be either public or user.
    def partner_form(self, **post):
    #create method
    #this will load the form webpage
        return request.render("eka.tmp_customer_form", {})
    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone')
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("eka.tmp_customer_form_success", vals)
        #finally send a request to render the thank you page#












# -*- coding: utf-8 -*-
# from odoo import http
