from django.db import models
from system.storage import ImageStorage
#用户表
class User(models.Model):
    oppen_id = models.CharField('用户编号',max_length = 255)
    user_name = models.CharField('用户名称',max_length = 100,null = True)
    user_head = models.ImageField('用户头像',upload_to = './head/',storage =ImageStorage(),null = True)
    
    def __str__(self):
        return self.user_name

    class Meta:
    	verbose_name = '用户信息管理'
    	verbose_name_plural = '用户信息管理'
#学校表
class School(models.Model):
	school_id = models.CharField('学校编号',max_length = 20,primary_key = True)
	school_name = models.CharField('学校名称',max_length = 100)
	school_badge = models.ImageField('校徽',upload_to = './badge/',storage = ImageStorage(),null = True)
	school_motto = models.CharField('校训',max_length = 60,null =True)
	school_address = models.CharField('学校地址',max_length = 200,null = True)
	school_location = models.CharField('所在地',max_length = 100,null = True)
	school_mold = models.CharField('学校类型',max_length = 100,null = True)
	school_belong = models.CharField('学校隶属',max_length = 50,null = True)
	school_url = models.URLField('学校网址',null = True)
	school_tel = models.CharField('联系电话',max_length = 50,null = True)
	school_abst = models.TextField('学校简介',null = True)

	def __str__(self):
		return self.school_name

	class Meta:
		verbose_name = '院校资料管理'
		verbose_name_plural = '院校资料管理'


#学校图片表
class SchoolImg(models.Model):
	school = models.ForeignKey(School,on_delete = models.CASCADE)
	school_pic = models.ImageField('学校图片',upload_to = './image/',storage = ImageStorage())

	class Meta:
		verbose_name = '学校图片'
		verbose_name_plural = '学校图片'

	# def __str__(self):
	# 	return self.school
#学院表
class College(models.Model):
	college_name = models.CharField('学院名称',max_length = 200)
	school = models.ForeignKey(School,on_delete = models.CASCADE)
	college_url = models.URLField('学院网址',null = True)
	def __str__(self):
		return self.college_name

	class Meta:
		verbose_name = '院校学院设置'
		verbose_name_plural = '院校学院设置'

#学校专业表
class professional(models.Model):
	profes_id  = models.CharField('专业编号',max_length = 200,primary_key = True)
	profes_name = models.CharField('专业名称',max_length = 200)
	related = models.TextField("相关专业",null = True)
	profess_class  = models.CharField("科类",max_length = 255,null = True)
	main_class = models.TextField("主干学科",null = True)
	main_cource =  models.TextField("主要课程",null = True)
	practice = models.TextField("实践教学",null = True)
	objective = models.TextField("培养目标",null = True)
	tra_require = models.TextField("培养要求",null = True)
	direction = models.TextField("就业方向",null = True)
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
		verbose_name = '院校专业设置'
		verbose_name_plural = '院校专业设置'


		

#历年分数线
class BatchLine(models.Model):
	fare_year = models.CharField('年份',max_length = 4,null = True)
	fare_lend = models.CharField('生源地',max_length = 200,null = True)
	fare_batch = models.CharField('录取批次',max_length = 50,null = True)
	art_science = models.CharField('文理科',max_length = 50,null = True)
	control_line = models.CharField('控制线',max_length = 20, null = True)

	def __str__(self):
		return self.fare_year

	class Meta:
		verbose_name = '历年批次线'
		verbose_name_plural = '历年批次线'

#院校录取线
class EnrollLine(models.Model):
	enroll_year = models.CharField('年份',max_length = 4,null = True)
	batch = models.CharField('录取批次',max_length = 100,null = True)
	art_science = models.CharField('文理科',max_length = 50,null = True)
	dics = models.CharField('科类',max_length = 100,null = True)
	major = models.CharField('专业',max_length = 200,null = True)
	control_line = models.CharField('控制线',max_length =50,null = True)
	enrolment = models.CharField('录取人数',max_length = 50,null = True)
	highest_score =  models.CharField('最高分',max_length = 50,null = True) 
	minimum_score =  models.CharField('最低分',max_length = 50,null = True)
	average_score =  models.CharField('平均分',max_length = 50,null = True)
	school = models.ForeignKey(School,on_delete = models.CASCADE)

	def __str__(self):
		return self.batch

	class Meta:
		verbose_name = '院校录取线'
		verbose_name_plural = '院校录取线'
 
#提问者
class Questions(models.Model):
	que_tittle = models.CharField('标题',max_length = 100)
	que_text = models.TextField('问题内容',null = True)
	que_image = models.ImageField('图片',upload_to = './quetion/',storage = ImageStorage(),null = True)
	questioner = models.CharField('提问者',max_length = 200)
	que_time = models.DateField('提问时间')

	def __str__(self):
		return self.que_tittle

	class Meta:
		verbose_name = '用户提的问题'
		verbose_name_plural = '用户提的问题'

#问题的回答
class queAnswer(models.Model):
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	answers = models.CharField('回复者',max_length = 200)
	ans_time = models.DateField('回复时间')
	ans_text = models.TextField('回答内容',null = True)

	def __str__(self):
		return self.answers

	class Meta:
		verbose_name = '用户的回答'
		verbose_name_plural = '用户的回答'

#问题被查看记录
class quetionViews(models.Model):
	question = models.ForeignKey(Questions,on_delete = models.CASCADE)
	views = models.ForeignKey("User",on_delete = models.CASCADE)

	class Meta:
		verbose_name = '院校名称'
		verbose_name_plural = '院校名称'
#数字字典表
class category(models.Model):
	cate_id = models.CharField("文章类别编号",max_length = 20,primary_key = True)
	cate_name = models.CharField("文章类别名称",max_length = 255)

	class Meta:
		verbose_name = '文章类别'
		verbose_name_plural = '文章类别'
	
	def __str__(self):
		return self.cate_name

#文章表
class Article(models.Model):
	tittle = models.CharField("文章标题",max_length = 255)
	context = models.TextField("文章内容")
	art_date = models.DateField("收录时间")
	cate = models.ForeignKey(category,on_delete = models.CASCADE)

	class Meta:
		verbose_name = '高考文章管理'
		verbose_name_plural = '高考文章管理'

	def __str__(self):
		return self.tittle

#文章阅读表
class artRead(models.Model):
	article = models.ForeignKey(Article,on_delete = models.CASCADE)
	user  =models.ForeignKey(User,on_delete = models.CASCADE)
	read_date = models.DateField("阅读时间")

	class Meta:
		verbose_name = '文章阅读记录'
		verbose_name_plural = '文章阅读记录'

#文章收藏表
class artCollect(models.Model):
	article = models.ForeignKey(Article,on_delete = models.CASCADE)
	user  =models.ForeignKey(User,on_delete = models.CASCADE)
	acollect_date = models.DateField("阅读时间")


	class Meta:
		verbose_name = '文章收藏记录'
		verbose_name_plural = '文章收藏记录'




class news(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	new_context = models.TextField("消息内容")
	new_date = models.DateField("消息时间")

	class Meta:
		verbose_name = '消息'
		verbose_name_plural = '消息'
	def __str__(self):
		return self.new_context