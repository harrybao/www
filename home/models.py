from django.db import models
from system.storage import ImageStorage
#用户表
class User(models.Model):
    user_id = models.CharField('用户编号',max_length = 255,primary_key = True)
    user_name = models.CharField('用户名称',max_length = 100,null = True)
    user_head = models.ImageField('用户头像',upload_to = './head/',storage =ImageStorage(),null = True)
    
    def __str__(self):
        return u'%s %s %s' % (self.user_id,self.user_name,self.user_head)
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
	school_feat =  models.CharField('院校特色',max_length = 100,null = True)
	school_tel = models.CharField('联系电话',max_length = 50,null = True)
	school_abst = models.TextField('学校简介',null = True)

	def __str__(self):
		return u'%s %s %s' % (self.school_id,self.school_name,self.school_motto)
#学校图片表
class School_Img(models.Model):
	school = models.ForeignKey("School",on_delete = models.CASCADE)
	school_pic = models.ImageField('学校图片',upload_to = './image/',storage = ImageStorage())

	def __str__(self):
		return self.school_ph
#学院表
class College(models.Model):
	College_name = models.CharField('学院名称',max_length = 200)
	school = models.ForeignKey("School",on_delete = models.CASCADE)
	college_url = models.URLField('学院网址',null = True)
	def __str__(self):
		return self.College_name


#历年分数线
class fare_line(models.Model):
	fare_batch = models.CharField('批次',max_length = 50,null = True)
	fare_science = models.CharField('理科',max_length = 20,null = True)
	fare_arts = models.CharField('文科',max_length = 20, null = True)

	def __str__(self):
		return self.fare_batch

#学校历年分数
class Over_year(models.Model):
	batch = models.CharField('批次',max_length = 100,null = True)
	dics = models.CharField('科类',max_length = 100,null = True)
	major = models.CharField('专业',max_length = 200,null = True)
	control_line = models.CharField('控制线',max_length =50,null = True)
	enrolment = models.CharField('录取人数',max_length = 50,null = True)
	highest_score =  models.CharField('最高分',max_length = 50,null = True) 
	minimum_score =  models.CharField('最低分',max_length = 50,null = True)
	average_score =  models.CharField('平均分',max_length = 50,null = True)

	def __str__(self):
		return self.batch
 
#提问者
class Questions(models.Model):
	que_tittle = models.CharField('标题',max_length = 100)
	que_text = models.CharField('问题',max_length = 255)
	que_image = models.ImageField('图片',upload_to = './quetion/',storage = ImageStorage(),null = True)
	questioner = models.CharField('提问者',max_length = 200)
	que_time = models.DateField('提问时间')
	que_view = models.CharField('查看次数',max_length = 20,null = True)

	def __str__(self):
		return self.que_tittle

#问题的回答
class que_answer(models.Model):
	question = models.ForeignKey("Questions",on_delete = models.CASCADE)
	answers = models.CharField('回复者',max_length = 200)
	ans_time = models.DateField('回复时间')

	def __str__(self):
		return self.answers

