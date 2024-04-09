# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_qrcode"
app_title = "Frappe QRcode"
app_publisher = ""
app_description = ""
app_icon = "fa fa-fire-extinguisher"
app_color = "red"
app_email = ""
app_license = "MIT"

# Jinja Filters
# ---------------
# Methods accessible to print template
jenv = {
    "methods": [
    'get_qrcode:frappe_qrcode.jinja_filters.get_qrcode'
    ]
}