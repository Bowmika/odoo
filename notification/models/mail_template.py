from odoo import models, fields, api


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    # @api.model
    # def create_mail_template(self,event):
    #     template = self.create({
    #         'name': 'My Email Template',
    #         'model_id': self.env.ref('notification.model_celebration_event').id,  # Replace with the actual model reference
    #         'subject': 'My Subject',
    #         'email_from': 'idigi.sneha@gmail.com',
    #         'email_to': '${object.email}',  # Example of using a placeholder
    #         'body_html': '<p>This is the content of my email template.</p>',
    #         # Add any additional fields you defined in the model
    #         # 'additional_field': 'Value'
    #     })
        # template=self.env.ref('notification.create_mail_template')
        # template.send_mail(event.id, force_send=True)

