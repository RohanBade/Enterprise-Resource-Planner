from django.contrib import admin
from home.models import Transaction

admin.site.site_header = "Enterprise Resource Planner(E.R.P.) Admin Panel"
admin.site.site_title = "ERP Admin Portal"
admin.site.index_title = "Welcome to E.R.P. Researcher Portal"

# Register your models here.
admin.site.register(Transaction)
