# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class course(models.Model):
    _name = "eka.course"
    _description = "eka.course"

    name = fields.Char(string="name", required=True)
    description = fields.Text()
    instructor = fields.Char(string="instuctor")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='reponsible', index=True)


class session(models.Model):
    _name = "eka.session"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "eka.session"

    name = fields.Char(string="name", required=True,tracking=True)
    sequence = fields.Char(string="Sequence", copy=False, readonly=True, default=lambda self: _('new'))
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2))
    seat = fields.Integer(string="number of seat")
    # attened_ids=fields.Many2many('res.partner',string="Attendees")
    instructor_id = fields.Many2one('res.partner', string="instructor")
    course_id = fields.Many2one('eka.course', ondelete='Cascade', string='course', required=True)
    session_record=fields.Integer(string="session record",compute='_compute_session_record')

    state = fields.Selection([(
        'draft', 'Draft'),
        ('done', 'Done'), ('cancel', 'Cancelled'), ],
        required=True, default='draft')
    def _compute_session_record(self):
        # session_record=self.env['eka.session'].search_count([('session_id','=',self.id)])
        self.session_record=10



    def button_done(self):
        self.state='done'


    def button_rest(self):
        self.state='draft'


    def button_cancel(self):
        self.state='cancel'


    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = 'new session'
        if vals.get('sequence', _('new')) == _('new'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('eka.session') or _('new')
        res = super(session, self).create(vals)
        return res




# class products(models.Model):
#     name="eka.product"
#     _inherit="product.template"