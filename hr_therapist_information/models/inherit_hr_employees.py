from odoo import api, models, fields

class InheritHrEmployee(models.Model):
    _inherit = "hr.employee"

    license_number = fields.Char(string="License Number")
    license_expiry_date = fields.Date(string="License Expiry Date")
    specialization_ids = fields.Many2many("therapist.specialization", 'employee_specialization_rel', 'employee_id', 'specialization_id', string="Specialization", required=True)
  
    years_of_experience = fields.Integer(string="Years of Experience")
    # therapy_modalities = fields.Many2many
    areas_of_expertise = fields.Char(string="Areas of Expertise")
    language_ids = fields.One2many(comodel_name='therapist.language', inverse_name='employee_id', string="Languages Spoken")
    availability_status = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('on_leave', 'On Leave')
    ], string="Availability Status", default='available')
    therapy_style = fields.Selection([
        ('cbt', 'Cognitive Behavioral Therapy'),
        ('dbt', 'Dialectical Behavior Therapy'),
        ('humanistic', 'Humanistic Therapy'),
        ('psychodynamic', 'Psychodynamic Therapy'),
        ('integrative', 'Integrative Therapy')
    ])

    therapy_choice = fields.Selection([
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('chat', 'Chat')
    ])
    client_age_groups = fields.Char(string="Client Age Groups")
    
    certificate_ids = fields.One2many(comodel_name="therapist.certificate", inverse_name="employee_id", string="Certificates")
    
    population = fields.Selection([
        ('children', 'Children'),
        ('adults', 'Adults'),
        ('seniors', 'Seniors'),
        ('couples', 'Couples'),
        ], string="Population Served")
    