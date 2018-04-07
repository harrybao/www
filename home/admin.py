from django.contrib import admin
from home.models import User,School,fare_line

class AuthorUser(admin.ModelAdmin):
	list_display = ('user_id','user_name','user_head')

class AuthSchool(admin.ModelAdmin):
	list_display = ('school_id','school_name','school_motto')

admin.site.register(User,AuthorUser)
admin.site.register(School,AuthSchool)
admin.site.register(fare_line)