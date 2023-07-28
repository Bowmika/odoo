from odoo import api, models,fields
from datetime import datetime, date, timedelta
import datetime



class CelebrationEvent(models.Model):
    _inherit = 'celebration.event'

    # @api.model
    # def send_anniversary_emails(self):
    #     anniversary_event =self.env['celebration.event'].search([('event_date', '=',fields.Date.today())])
    #     for event in anniversary_event:
    #         template = self.env.ref('notification.create_mail_template')
    #         template.send_mail(event.id)

    @api.model
    def send_anniversary_mail(self):
        today = fields.Date.today()
        anniversary_events = self.search([('event_date', '=', today)])
        template = self.env.ref('notification.email_template_anniversary_mail')

        for event in anniversary_events:
             template.send_mail(event.id, force_send=True)

    # self.env['mail.template'].create_mail_template(event)

    # @api.model
    # def send_birthday_emails(self):
    #     today = fields.Date.today()
    #     birthday_events = self.search([('event_date', '=', today)])
    #     template = self.env.ref('your_module.your_birthday_template')
    #
    #     for event in birthday_events:
    #         template.send_mail(event.id, force_send=True)
    #
    # @api.model
    # def send_team_anniversary_emails(self):
    #     today = fields.Date.today()
    #     team_events = self.search([('event_date', '=', today)])
    #     template = self.env.ref('your_module.your_team_anniversary_template')
    #
    #     for event in team_events:
    #         template.send_mail(event.id, force_send=True)