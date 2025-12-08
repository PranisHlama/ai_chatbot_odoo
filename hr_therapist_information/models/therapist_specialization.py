from odoo import fields, models

class TherapistSpecialization(models.Model):
    _name = "therapist.specialization"
    _description = "Specializations for therapists"

    name = fields.Char(string = "Specialization", required=True)
    active = fields.Boolean(string="Active", default=True)

class TherapistCerticate(models.Model):
    _name = "therapist.certificate"
    _description = "Certificates for therapists"

    name = fields.Char(string='Certificate Name')
    file = fields.Binary(string='Upload Certificate', attachment=True)
    filename = fields.Char(string='File Name')

    employee_id = fields.Many2one('hr.employee', string='Therapist', ondelete='cascade')

class TherapistLanguage(models.Model):
    _name = "therapist.language"
    _description = "Languages spoken by therapists"

    name = fields.Char(string='Language')
    employee_id = fields.Many2one('hr.employee', string='Therapist', ondelete='cascade')