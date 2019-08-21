# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "zuvi"
app_title = "Zuvi"
app_publisher = "GreyCube Technologies"
app_description = "Customization for zuviuslifesciences"
app_icon = "octicon octicon-beaker"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zuvi/css/zuvi.css"
# app_include_js = "/assets/zuvi/js/zuvi.js"

# include js, css files in header of web template
# web_include_css = "/assets/zuvi/css/zuvi.css"
# web_include_js = "/assets/zuvi/js/zuvi.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "zuvi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "zuvi.install.before_install"
# after_install = "zuvi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zuvi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice": {
		"validate": "zuvi.api.calculate_contribution",
	}
}
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zuvi.tasks.all"
# 	],
# 	"daily": [
# 		"zuvi.tasks.daily"
# 	],
# 	"hourly": [
# 		"zuvi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zuvi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"zuvi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "zuvi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zuvi.event.get_events"
# }

