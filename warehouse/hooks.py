from . import __version__ as app_version

app_name = "warehouse"
app_title = "warehouse"
app_publisher = "wahni"
app_description = "warehouse"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "test@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/warehouse/css/warehouse.css"
# app_include_js = "/assets/warehouse/js/warehouse.js"

# include js, css files in header of web template
# web_include_css = "/assets/warehouse/css/warehouse.css"
# web_include_js = "/assets/warehouse/js/warehouse.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "warehouse/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "warehouse.install.before_install"
# after_install = "warehouse.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "warehouse.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
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
# 		"warehouse.tasks.all"
# 	],
# 	"daily": [
# 		"warehouse.tasks.daily"
# 	],
# 	"hourly": [
# 		"warehouse.tasks.hourly"
# 	],
# 	"weekly": [
# 		"warehouse.tasks.weekly"
# 	]
# 	"monthly": [
# 		"warehouse.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "warehouse.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "warehouse.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "warehouse.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"warehouse.auth.validate"
# ]
fixtures = [{
    "dt": "Custom Field",
    "filters": [["name", "in",['Project-note', 'Project-open_walls2','Project-portal_frame2','Project-x__bracing2','Project-right_endwall_lew_bracing_type','Project-right_endwall_condition__along_gl_8','Project-left_endwall_open_walls','Project-portals_frame','Project-x__bracing1','Project-lew_bracing_type','Project-left_endwall_condition__along_gl_1','Project-open_walls','Project-portal_frames','Project-x__bracings','Project-fsw_bracing_type','Project-far_side_wall_condition_along_gl_a','Project-__open_walls','Project-right_lf','Project-portal_frame','Project-x__bracing','Project-note2']]]
}]
