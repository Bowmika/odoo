from odoo import models, fields,api

class CelebrationEvent(models.Model):
    _name = 'celebration.event'
    _description = 'Celebration Event'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email', required=True)
    event_date = fields.Date('Event Date', required=True)


