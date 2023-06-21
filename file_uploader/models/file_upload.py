from odoo import models, fields


class FileUploader(models.Model):
    _name = 'file.uploader'
    _description = 'File Uploader'
    _order = 'name'

    name = fields.Char()
    file = fields.Binary()
    upload_date = fields.Datetime(default=lambda self: fields.Datetime.now())
