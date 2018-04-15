from django.contrib import admin
from home.models import User,School,SchoolImg,College,professional,majorSet,BatchLine,EnrollLine,Questions,queAnswer,quetionViews,Article,artRead,artCollect,category


class AuthorUser(admin.ModelAdmin):
	list_display = ('oppen_id','user_name','user_head')

class AuthSchool(admin.ModelAdmin):
	list_display = ('school_id','school_name','school_motto','school_address')
	fields = (('school_id','school_name'),'school_badge','school_motto',
		       ('school_address','school_location'),('school_mold','school_belong'),
		       'school_tel','school_url','school_abst')

admin.site.register(User,AuthorUser)
admin.site.register(School,AuthSchool)
admin.site.register(SchoolImg)
admin.site.register(College)
admin.site.register(professional)
admin.site.register(majorSet)
admin.site.register(BatchLine)
admin.site.register(EnrollLine)
admin.site.register(Questions)
admin.site.register(queAnswer)
admin.site.register(quetionViews)
admin.site.register(Article)
admin.site.register(artRead)
admin.site.register(artCollect)
admin.site.register(category)