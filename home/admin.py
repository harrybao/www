from django.contrib import admin
from home import models

# from .utils import import_user


class ReadOnlyModelAdmin(admin.ModelAdmin):
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.site_header = '高校本后台管理中心'
admin.site.site_title = '高效本'

class TextTinymce_Admin(admin.ModelAdmin):

	class Media:
		js = [
			'/static/tinymce/js/jquery.min.js',
			'/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',
		]


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

class AuthUser(ReadOnlyModelAdmin):
	list_display = ('oppen_id','user_name','user_head')
	inlines = [UserNews]
		

class AuthSchool(admin.ModelAdmin):
	list_display = ('school_id','school_name','school_location','school_address')
	fields = (('school_id','school_name'),'school_motto',('school_badge','school_url'),
		       ('school_address','school_location'),('school_mold','school_tel'),
		       'school_abst')
	inlines = [ImgLine,CollageLine]
	list_per_page = 10
	ordering = ('school_id',)
	class Media:
		js = [
			'/static/tinymce/js/jquery.min.js',
			'/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',
		]

class AuthProfess(admin.ModelAdmin):
	list_display = ('profes_id','profes_name','profess_class')
	fields = (('profes_id','profes_name'),('profess_class','related'),'main_class',
				'practice','objective','tra_require','direction')
	inlines = [ProfessLine]
	list_per_page = 10
	search_fields  =('profes_name','main_class')

class AuthEnroll(admin.ModelAdmin):
	list_display = ('enroll_year','school_name','batch','art_science','highest_score','minimum_score','average_score')
	list_per_page = 10
	ordering = ('-enroll_year',)


class AuthBatch(admin.ModelAdmin):
	list_display = ('fare_year','fare_lend','fare_batch','art_science','control_line')
	list_per_page = 10
	ordering = ('-fare_year',)

class AuthArticle(admin.ModelAdmin):
	list_display =('tittle','art_date')
	fields = ('cate',('tittle','art_date'),'context')
	inlines = [ArticleRead]
	list_per_page = 10
	class Media:
		js = [
			'/static/tinymce/js/jquery.min.js',
			'/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',
		]

class AuthDigital(admin.ModelAdmin):
	inlines = [DigitalDetail]

class AuthQuestions(admin.ModelAdmin):
	inlines = [QuestionRead]

class AuthScore(admin.ModelAdmin):
	list_display =('major_name','aver_score','student_loca','batch')
	list_per_page = 10
	search_fields  =('major_name','batch')
		
class AuthCollegeLine(admin.ModelAdmin):
	list_display = ('enroll_year','batch','art_science','highest_score','minimum_score','average_score')
	list_per_page = 10
	ordering = ('-enroll_year',)


# class KNImportFileAdmin(admin.ModelAdmin):

#     list_display = ('file','name',)
#     list_filter = ['name',]

#     def save_model(self, request, obj, form, change):

#         re = super(KNImportFileAdmin,self).save_model(request, obj, form, change)
#         import_user(self, request, obj, change)
#         return re
# admin.site.register(models.ImportFile,KNImportFileAdmin)

admin.site.register(models.User,AuthUser)
admin.site.register(models.School,AuthSchool)
# admin.site.register(models.queAnswer)
admin.site.register(models.professional,AuthProfess)
admin.site.register(models.majorScore,AuthScore)
admin.site.register(models.BatchLine,AuthBatch)
admin.site.register(models.EnrollLine,AuthEnroll)
# admin.site.register(models.collegeLines,AuthCollegeLine)
# admin.site.register(models.Questions,AuthQuestions)
admin.site.register(models.Article,AuthArticle)
admin.site.register(models.digital,AuthDigital)