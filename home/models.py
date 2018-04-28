from django.db import models
from system.storage import ImageStorage
# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
#用户表
class User(models.Model):
    oppen_id = models.CharField('用户编号',max_length = 200)
    user_name = models.CharField('用户名称',max_length = 200,null = True)
    user_head = models.TextField('用户头像',null = True)
    
    def __str__(self):
        return self.user_name

    class Meta:
    	verbose_name = '用户信息管理'
    	verbose_name_plural = '用户信息管理'
#学校表
class School(models.Model):
	school_id = models.CharField('学校编号',max_length = 20,primary_key = True)
	school_name = models.CharField('学校名称',max_length = 200)
	school_badge = models.ImageField('校徽',upload_to = './badge/',storage = ImageStorage(),null = True)
	school_motto = models.CharField('校训',max_length = 100,null =True)
	school_address = models.CharField('学校地址',max_length = 200,null = True)
	school_location = models.CharField('所在地',max_length = 100,null = True)
	school_mold = models.CharField('学校类型',max_length = 100,null = True)
	school_url = models.URLField('学校网址',null = True)
	school_tel = models.CharField('联系电话',max_length = 100,null = True)
	school_abst = models.TextField('学校简介',null = True)

	def __str__(self):
		return self.school_name

	class Meta:
		verbose_name = '院校管理'
		verbose_name_plural = '院校管理'


#学校图片表
class SchoolImg(models.Model):
	school = models.ForeignKey(School,on_delete = models.CASCADE)
	school_pic = models.ImageField('图片',upload_to = './image/',storage = ImageStorage())

	class Meta:
		verbose_name = '学校图片'
		verbose_name_plural = '学校图片'

#学院表
class College(models.Model):
	college_name = models.CharField('学院名称',max_length = 200)
	school = models.ForeignKey(School,on_delete = models.CASCADE)
	def __str__(self):
		return self.college_name

	class Meta:
		verbose_name = '学院设置'
		verbose_name_plural = '学院设置'

#学校专业表
class professional(models.Model):
	profes_id  = models.CharField('专业编号',max_length = 100,primary_key = True)
	profes_name = models.CharField('专业名称',max_length = 400)
	related = models.CharField("专业介绍",max_length = 1000,null = True,blank=True)
	profess_class  = models.CharField("专业类别",max_length = 300,null = True,blank=True)
	main_class = models.CharField("学科",max_length = 300,null = True,blank=True)
	practice = models.CharField("学习课程",max_length = 1000,null = True,blank=True)
	objective = models.CharField("培养目标",max_length = 1000,null = True,blank=True)
	tra_require = models.CharField("培养要求",max_length = 1000,null = True,blank=True)
	direction = models.CharField("就业前景",max_length = 1000,null = True,blank=True)
	def __str__(self):
		return self.profes_name

	class Meta:
		verbose_name = '专业信息管理'
		verbose_name_plural = '专业信息管理'

class majorSet(models.Model):
	school = models.ForeignKey(School,on_delete = models.CASCADE)
	profess = models.ForeignKey(professional,on_delete = models.CASCADE)
	def __str__(self):
		return u'%s %s' % (self.school,self.profess)

	class Meta:
		verbose_name = '开设院校'
		verbose_name_plural = '开设院校'


		

#历年分数线
class BatchLine(models.Model):
	fare_year = models.CharField('年份',max_length = 4,null = True)
	fare_lend = models.CharField('生源地',max_length = 500,null = True)
	fare_batch = models.CharField('录取批次',max_length = 50,null = True)
	art_science = models.CharField('文理科',max_length = 50,null = True)
	control_line = models.FloatField('控制线', null = True)

	def __str__(self):
		return self.fare_year

	class Meta:
		verbose_name = '地区批次线'
		verbose_name_plural = '地区批次线'

#院校录取线
# class EnrollLine(models.Model):
# 	enroll_year = models.CharField('年份',max_length = 4,null = True)
# 	batch = models.CharField('录取批次',max_length = 100,null = True)
# 	art_science = models.CharField('文理科',max_length = 50,null = True)
# 	highest_score =  models.FloatField('最高分',null = True) 
# 	minimum_score =  models.FloatField('最低分',null = True)
# 	average_score =  models.FloatField('平均分',null = True)
# 	school = models.ForeignKey(School,on_delete = models.CASCADE)

# 	def __str__(self):
# 		return self.batch

# 	class Meta:
# 		verbose_name = '院校录取线'
# 		verbose_name_plural = '院校录取线'
 
#提问者
class Questions(models.Model):
	que_tittle = models.CharField('标题',max_length = 300,null = True)
	que_text = models.TextField('问题内容',null = True)
	questioner = models.CharField('提问者',max_length = 200)
	que_time = models.DateTimeField('提问时间')
	classify = models.CharField('问题分类',max_length = 200,null =True)

	def __str__(self):
		return self.questioner

	class Meta:
		verbose_name = '用户提的问题'
		verbose_name_plural = '用户提的问题'

#问题的回答
class queAnswer(models.Model):
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	answers = models.CharField('回复者',max_length = 200)
	ans_time = models.DateTimeField('回复时间')
	ans_text = models.TextField('回答内容',null = True)

	def __str__(self):
		return self.answers

	class Meta:
		verbose_name = '用户的回答'
		verbose_name_plural = '用户的回答'

#问题被查看记录
class quetionViews(models.Model):
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	views = models.CharField("用户编号",max_length = 200)

	class Meta:
		verbose_name = '问题查看表'
		verbose_name_plural = '问题查看表'
#数字字典表
class digital(models.Model):
	dig_id = models.CharField("数字字典编号",max_length = 20,primary_key = True)
	dig_name = models.CharField("数字字典名称",max_length = 255)

	class Meta:
		verbose_name = '数字字典'
		verbose_name_plural = '数字字典'
	
	def __str__(self):
		return self.dig_name
#字典细档表
class digdetail(models.Model):
	detail_name =models.CharField("名称",max_length = 100)
	det_remarks = models.CharField("备注" ,max_length = 500)
	digital = models.ForeignKey(digital,on_delete = models.CASCADE)
	class Meta:
		verbose_name = '数字字典详情'
		verbose_name_plural = '数字字典详情'
	def __str__(self):
		return self.detail_name

#文章表
class Article(models.Model):
	cate = models.ForeignKey(digdetail,on_delete = models.CASCADE)
	tittle = models.CharField("文章标题",max_length = 255)
	context = models.TextField("文章内容")
	art_date = models.DateField("收录时间")
	

	class Meta:
		verbose_name = '文章管理'
		verbose_name_plural = '文章管理'

	def __str__(self):
		return self.tittle

#文章阅读以及收藏表
class readCollect(models.Model):
	article = models.ForeignKey(Article,on_delete = models.CASCADE)
	user  =models.CharField("阅读用户",max_length = 200,null = True)
	read_date = models.DateTimeField("时间",null = True)
	read_collect = models.CharField("阅读或收藏",max_length = 4)


	class Meta:
		verbose_name = '文章操作表'
		verbose_name_plural = '文章操作表'

#消息表
class news(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	new_context = models.CharField("回答者主键",max_length = 200)
	new_date = models.DateTimeField("消息时间")
	readed = models.CharField("是否已读",max_length = 4,null = True)
	question = models.CharField("问题编号",max_length = 200,null = True)

	class Meta:
		verbose_name = '消息表'
		verbose_name_plural = '消息表'
	def __str__(self):
		return self.new_context


class readRecord(models.Model):
	article = models.ForeignKey(Article,on_delete = models.CASCADE)
	open_id  =models.CharField("阅读用户",max_length = 200,null = True)

	class Meta:
		verbose_name = '文章浏览记录'
		verbose_name_plural = '文章浏览记录'

class majorScore(models.Model):
	major_name = models.CharField("专业名称",max_length = 200,null = True)
	school_name = models.CharField("高校名称",max_length = 200,null = True)
	aver_score = models.CharField("平均分",max_length = 50,null = True)
	highest = models.CharField("最高分",max_length = 50,null = True)
	student_loca = models.CharField("考生地区",max_length = 100,null = True)
	category = models.CharField("科别",max_length = 50,null = True)
	par_year = models.CharField("年份",max_length = 10, null = True)
	batch = models.CharField("批次",max_length = 100,null = True)

	class Meta:
		verbose_name = '专业录取线'
		verbose_name_plural = '专业录取线'


class collegeLines(models.Model):
	enroll_year = models.CharField('年份',max_length = 10,null = True)
	batch = models.CharField('录取批次',max_length = 100,null = True)
	art_science = models.CharField('文理科',max_length = 50,null = True)
	highest_score =  models.CharField('最高分',max_length = 50,null = True) 
	minimum_score =  models.CharField('最低分',max_length = 50,null = True)
	average_score =  models.CharField('平均分',max_length = 50,null = True)
	enrill_num = models.CharField('录取人数',max_length = 50,null = True)
	school_name = models.CharField('学校名称',max_length = 200,null = True)

	class Meta:
		verbose_name = '院校分数线'
		verbose_name_plural = '院校分数线'


class specialtyScore(models.Model):
	major_name = models.CharField("专业名称",max_length = 200,null = True)
	school_name = models.CharField("高校名称",max_length = 200,null = True)
	aver_score = models.CharField("平均分",max_length = 50,null = True)
	highest = models.CharField("最高分",max_length = 50,null = True)
	minimum = models.CharField("最低分",max_length = 50,null = True)
	student_loca = models.CharField("考生地区",max_length = 100,null = True)
	category = models.CharField("科别",max_length = 50,null = True)
	par_year = models.CharField("年份",max_length = 10, null = True)
	batch = models.CharField("批次",max_length = 100,null = True)

	class Meta:
		verbose_name = '专业分数线'
		verbose_name_plural = '专业分数线'

class EnrollLine(models.Model):
	enroll_year = models.CharField('年份',max_length = 10,null = True)
	batch = models.CharField('录取批次',max_length = 100,null = True)
	art_science = models.CharField('文理科',max_length = 50,null = True)
	highest_score =  models.CharField('最高分',max_length = 50,null = True) 
	minimum_score =  models.CharField('最低分',max_length = 50,null = True)
	average_score =  models.CharField('平均分',max_length = 50,null = True)
	enrill_num = models.CharField('录取人数',max_length = 50,null = True)
	school_name = models.CharField('学校名称',max_length = 200,null = True)
	province = models.CharField('考生地区',max_length = 200,null = True)

	class Meta:
		verbose_name = '高校分数线'
		verbose_name_plural = '高校分数线'

# class KNSVNHistory(models.Model):
#     revision = models.IntegerField(verbose_name=u"修订版本", blank=True, null=True)
#     value = models.TextField(verbose_name=u"SVN属性值", blank=False, null=False, default=u"")
#     repo = models.CharField(max_length=100, verbose_name=u"SVN仓库", blank=False, null=False)
#     ctime = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True, )
#     mtime = models.DateTimeField(verbose_name=u"修改时间", auto_now=True, )

#     class Meta:
#         ordering = ['ctime']

#     def __str__(self):
#         return self.value

# class ImportFile(models.Model):

#     file = models.FileField(upload_to='./File/')
#     name = models.CharField(max_length=50, verbose_name=u'文件名')

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#         return self.name
			
