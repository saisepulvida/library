# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'name must be unique!')
    ]

