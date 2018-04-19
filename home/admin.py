from django.contrib import admin
from home import models


admin.site.site_header = '高校本后台管理'
admin.site.site_title = '高效本'


class CollageLine(admin.TabularInline):
	model = models.College
	extra = 1
class UserNews(admin.TabularInline):
	model = models.news
	extra = 1

class ProfessLine(admin.TabularInline):
	model = models.majorSet
	extra = 1
	fk_name = "profess"

class ImgLine(admin.TabularInline):
	model = models.SchoolImg
	extra = 1

class DigitalDetail(admin.TabularInline):
	model = models.digdetail
	extra = 1

class ArticleRead(admin.TabularInline):
	model = models.readCollect
	extra = 1

class QuestionRead(admin.TabularInline):
	model = models.quetionViews
	extra = 1

class AuthUser(admin.ModelAdmin):
	list_display = ('oppen_id','user_name','user_head')
	inlines = [UserNews]
		

class AuthSchool(admin.ModelAdmin):
	list_display = ('school_id','school_name','school_location','school_address')
	fields = (('school_id','school_name'),'school_motto',('school_badge','school_url'),
		       ('school_address','school_location'),('school_mold','school_tel'),
		       'school_abst')
	inlines = [ImgLine,CollageLine]

class AuthProfess(admin.ModelAdmin):
	list_display = ('profes_id','profes_name','profess_class')
	fields = (('profes_id','profes_name'),('profess_class','related'),'main_class',
				'practice','objective','tra_require','direction')
	inlines = [ProfessLine]

class AuthEnroll(admin.ModelAdmin):
	list_display = ('enroll_year','batch','art_science','highest_score','minimum_score','average_score')
	fields = (('enroll_year','batch'),('art_science','school'),
				('highest_score','minimum_score','average_score'))

class AuthBatch(admin.ModelAdmin):
	list_display = ('fare_year','fare_lend','fare_batch','art_science','control_line')
	list_per_page = 10

class AuthArticle(admin.ModelAdmin):
	list_display =('tittle','art_date')
	fields = ('cate',('tittle','art_date'),'context')
	inlines = [ArticleRead]

class AuthDigital(admin.ModelAdmin):
	inlines = [DigitalDetail]

class AuthQuestions(admin.ModelAdmin):
	inlines = [QuestionRead]
		


admin.site.register(models.User,AuthUser)
admin.site.register(models.School,AuthSchool)
# admin.site.register(models.College,AuthCollege)
admin.site.register(models.professional,AuthProfess)
# admin.site.register(models.majorSet,AuthMajorSet)
admin.site.register(models.BatchLine,AuthBatch)
admin.site.register(models.EnrollLine,AuthEnroll)
admin.site.register(models.Questions,AuthQuestions)
admin.site.register(models.Article,AuthArticle)
admin.site.register(models.digital,AuthDigital)