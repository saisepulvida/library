# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookExtension(models.Model):
    _inherit = "library.book"
    _description = "Library Extension"

    author_id = fields.Many2one('res.partner', string="Author",
                       required=True)

    category_id = fields.Many2many('library.book.category', string="Category")


