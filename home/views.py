# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from django.db import connection
import json
import requests
import datetime
import re

PIC_URL = "https://www.wh14.club/media/"



def main(req):
    return render(req,'home/main.html')


def api(req):
	if req.method=="GET":
		ac = req.GET['ac']
		if ac == 'hostuni':
			return hostUni()

		if ac == 'detail':
			schkey = req.GET['schkey']
			return detailsch(schkey)

		if ac == 'getOpenid':
			code = req.GET['code']
			return getOpenid(code)
			
		if ac == 'userExist':
			userid = req.GET['userid']
			return userExist(userid)

		if ac == 'userInfo':
			userid = req.GET['userid']
			nickName = req.GET['nickName']
			avatarUrl = req.GET['avatarUrl']
			return userInfo(userid,nickName,avatarUrl)
			

		if ac == 'artitle':
			return artitle()

		if ac == 'schooList':
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			search = req.GET['search']
			return schooList(search,start,pageSize)

		if ac == 'getProvince':
			return getProvince()

		if ac == 'batchLine':
			province = req.GET['province']
			return batchLine(province)

		if ac == 'batchYear':
			year = req.GET['year']
			province = req.GET['province']
			return batchYear(year,province)

		if ac == 'question':
			prokey = req.GET['prokey']
			return question(prokey)

		if ac == 'answerList':
			prokey = req.GET['prokey']
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			return answerList(prokey,start,pageSize)
		if ac == 'problemView':
			prokey = req.GET['prokey']
			userid = req.GET['userid']
			return problemView(prokey,userid)

		if ac == 'askProblem':
			problem = req.GET['problem']
			userid = req.GET['userid']
			askdate = req.GET['askdate']
			return askProblem(problem,userid,askdate)
		if ac == 'userAnwswer':
			answer = req.GET['answer']
			userid = req.GET['userid']
			ansdate = req.GET['ansdate']
			queid = req.GET['prokey']
			return userAnwswer(answer,userid,ansdate,queid)

		if ac == 'searchPro':
			search = req.GET['search']
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			return searchPro(search,start,pageSize)

		if ac == 'newsList':
			userid = req.GET['userid']
			return newsList(userid)

		if ac == 'userAskProblems':
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			userid = req.GET['userid']
			return userAskProblems(start,pageSize,userid)
		if ac == 'userAnsProblems':
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			userid = req.GET['userid']
			return userAnsProblems(start,pageSize,userid)
		if ac == 'newsDetail':
			prokey = req.GET['prokey']
			userid = req.GET['userid']
			newdate = req.GET['newdate']
			return newsDetail(prokey,userid,newdate)
		if ac == 'updateNew':
			newid = req.GET['newid']
			return updateNew(newid)

		if ac == 'addArticleViews':
			articlekey = req.GET['articlekey']
			userid = req.GET['userid']
			readdate = req.GET['readdate']
			return addArticleViews(articlekey,userid,readdate)
		if ac == 'articleDetail':
			articlekey = req.GET['articlekey']
			userid = req.GET['userid']
			return articleDetail(articlekey,userid)
		if ac == 'getMoreArticle':
			catekey = req.GET['catekey']
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			return getMoreArticle(catekey,start,pageSize)

		if ac == 'getReadArticle':
			userid = req.GET['userid']
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			return getReadArticle(userid,start,pageSize)
		if ac == 'getCollArticle':
			userid = req.GET['userid']
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			return getCollArticle(userid,start,pageSize)

		if ac == 'articleCollect':
			artkey = req.GET['artkey']
			userid = req.GET['userid']
			colldate = req.GET['colldate']
			return articleCollect(artkey,userid,colldate)
		if ac == 'notArticleCollect':
			artkey = req.GET['artkey']
			userid = req.GET['userid']
			return notArticleCollect(artkey,userid)
		if ac == 'majorList':
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			search = req.GET['search']
			return majorList(search,start,pageSize)
		if ac == 'majorDetail':
			pid = req.GET['pid']
			return majorDetail(pid)

		if ac == 'majorScore':
			start = req.GET['start']
			pageSize = req.GET['pageSize']
			searchc = req.GET['searchc']
			searchm = req.GET['searchm']
			return majorScore(start,pageSize,searchm,searchc)


			


def userInfo(userid,nickName,avatarUrl):
	try:
		user = models.User(oppen_id = userid,user_name=nickName,user_head =avatarUrl)
		user.save()
		return HttpResponse('success')
	except Exception as error:
		return HttpResponse(error)



def hostUni():	
	schools = models.School.objects.values()[0:4]
	result="{\"colist\":["
	for i in range(len(schools)):
		picture = models.SchoolImg.objects.values("school_pic").filter(school_id=schools[i]["school_id"])
		result += "{\"colname\":\""+schools[i]['school_name']+"\","
		result += "\"colpic\":\""+PIC_URL+picture[0]['school_pic']+"\","
		result += "\"badge\":\""+PIC_URL+schools[i]['school_badge']+"\","
		result += "\"colid\":\""+schools[i]['school_id']+"\","
		result += "\"coladd\":\""+schools[i]['school_address']+"\"}"
		if i<(len(schools)-1):
			result +=","
	result +="]}"
	return HttpResponse(result,content_type="application/json")


def detailsch(schkey):
	school = models.School.objects.values().filter(school_id=schkey)
	pictures = models.SchoolImg.objects.values().filter(school_id=schkey)
	colleges = models.College.objects.values().filter(school_id = schkey)
	# majors = models.majorSet.objects.values().filter(school_id = schkey)
	cursor = connection.cursor()
	cursor.execute("""select b.* from home_majorset as a left join 
		              home_professional as b on a.profess_id = b.profes_id 
		              where a.school_id ='"""+schkey+"'")
	rows = dictfetchall(cursor)
	result = "{\"schname\":\""+school[0]['school_name']+"\","
	result +="\"schmotto\":\""+school[0]['school_motto']+"\","
	result +="\"schaddress\":\""+school[0]['school_address']+"\","
	result +="\"schloca\":\""+school[0]['school_location']+"\","
	result +="\"schmold\":\""+school[0]['school_mold']+"\","
	result +="\"schurl\":\""+school[0]['school_url']+"\","
	result +="\"schtel\":\""+school[0]['school_tel']+"\","
	result +="\"abst\":\""+school[0]['school_abst'].replace('"',"'")+"\","
	if pictures:
		result +="\"piclist\":["
		for i in range(3):
			result +="{\"schpic\":\""+PIC_URL+pictures[i]['school_pic']+"\"}"
			if i<2:
				result+=","
		result += "]"
	if colleges:
		result += ",\"collegelist\":["
		for i in range(len(colleges)):
			result += "{\"college\":\""+colleges[i]['college_name']+"\"}"
			if i<(len(colleges)-1):
				result += ","
		result += "]"
	if rows:
		result += ",\"majorlist\":["
		for i in range(len(rows)):
			result += "{\"major\":\""+rows[i]['profes_name']+"\","
			result += "\"majorid\":\""+rows[i]['profes_id']+"\"}"
			if i < (len(rows)-1):
				result += ","
		result += "]"

	result +="}"
	print(result)
	return HttpResponse(result,content_type="application/json")

def getOpenid(code):
	SECRET ='8642b76873e0118924b940b0c283814c'
	APPID = 'wx7a88f9e66f67d42f'
	url = "https://api.weixin.qq.com/sns/jscode2session?appid="+APPID+"&secret="+SECRET+"&js_code="+code+"&grant_type=authorization_code"
	req = requests.get(url)
	return HttpResponse(req)
def userExist(userid):
	userinfo = models.User.objects.values().filter(oppen_id=userid)
	if userinfo:
		return HttpResponse('yes')
	else:
		return HttpResponse('no')

def artitle():
	knowtitles = models.Article.objects.values().filter(cate_id ='2').order_by('-art_date')[0:4]
	waytitles = models.Article.objects.values().filter(cate_id ='3').order_by('-art_date')[0:4]
	konwclass = models.digdetail.objects.values().filter(id = '2')
	wayclass = models.digdetail.objects.values().filter(id = '3')
	result = "{"
	result += "\"kcateid\":\""+str(knowtitles[0]['cate_id'])+"\","
	result += "\"kclass\":\""+konwclass[0]['detail_name']+"\","
	result += "\"wcateid\":\""+str(waytitles[0]['cate_id'])+"\","
	result += "\"wclass\":\""+wayclass[0]['detail_name']+"\","
	if knowtitles:
		result += "\"ktitles\":["
		for i in range(len(knowtitles)):
			result += "{\"kkey\":\""+str(knowtitles[i]['id'])+"\","
			result += "\"adate\":\""+str(knowtitles[i]['art_date'])[5:10]+"\","
			result += "\"title\":\""+knowtitles[i]['tittle'][:17]+"\"}"
			if i<(len(knowtitles)-1):
				result +=","
		result +="],"
	if waytitles:
		result += "\"wtitles\":["
		for i in range(len(waytitles)):
			result += "{\"wkey\":\""+str(waytitles[i]['id'])+"\","
			result += "\"adate\":\""+str(waytitles[i]['art_date'])[5:10]+"\","
			result += "\"title\":\""+waytitles[i]['tittle'][:17]+"\"}"
			if i<(len(waytitles)-1):
				result +=","
		result +="]"
	result +="}"
	return HttpResponse(result,content_type="application/json")

def schooList(search,start,pageSize):
	# schools = models.School.objects.values()
	cursor = connection.cursor()
	cursor.execute("select * from home_school where school_name like '%"+search+"%' limit "+start+","+pageSize)
	schools = dictfetchall(cursor)

	result = "{\"schoolist\":["
	for i in range(len(schools)):
		result += "{\"skey\":\""+schools[i]['school_id']+"\","
		result += "\"sname\":\""+schools[i]['school_name']+"\","
		result += "\"saddress\":\""+schools[i]['school_address']+"\","
		result += "\"sbadge\":\""+PIC_URL+schools[i]['school_badge']+"\"}"
		if i< (len(schools)-1):
			result +=","
	result += "]}"
	return HttpResponse(result,content_type="application/json")

def getProvince():
	cursor = connection.cursor()
	cursor.execute("select fare_lend from home_batchline group by fare_lend")
	rows = dictfetchall(cursor)
	result = "{"
	if rows:
		result += "\"lend\":["
		for i in range(len(rows)):
			result += "\""+rows[i]['fare_lend']+"\""
			if i < (len(rows)-1):
				result += ","
		result += "]}"
	return HttpResponse(result,content_type="application/json")

def batchLine(province):
	batchs = models.BatchLine.objects.values().filter(fare_year__range=[2012,2017],fare_lend = province)	
	# cursor = connection.cursor()
	# cursor.execute("select fare_lend from home_batchline group by fare_lend")
	# rows = dictfetchall(cursor)
	one_aci = batchs.filter(fare_batch='本科一批',art_science = '理科').order_by('fare_year')
	one_art = batchs.filter(fare_batch='本科一批',art_science = '文科').order_by('fare_year')
	two_aci = batchs.filter(fare_batch='本科二批',art_science = '理科').order_by('fare_year')
	two_art = batchs.filter(fare_batch='本科二批',art_science = '文科').order_by('fare_year')
	trd_aci = batchs.filter(fare_batch='专科',art_science = '理科').order_by('fare_year')
	trd_art = batchs.filter(fare_batch='专科',art_science = '文科').order_by('fare_year')
	# result = "{"
	# if rows:
	# 	result += "\"lend\":["
	# 	for i in range(len(rows)):
	# 		result += "\""+rows[i]['fare_lend']+"\""
	# 		if i < (len(rows)-1):
	# 			result += ","
	# 	result += "],"
	result = "{\"years\":["
	for i in range(len(one_aci)):
		result += "\""+str(one_aci[i]['fare_year'])+"\""
		if i <(len(one_aci)-1):
			result += ","
	result +="],\"one_aci\":["

	for i in range(len(one_aci)):
		result += "\""+str(one_aci[i]['control_line'])+"\""
		if i < (len(one_aci)-1):
			result += ","
	result +="],\"one_art\":["

	for i in range(len(one_art)):
		result += "\""+str(one_art[i]['control_line'])+"\""
		if i < (len(one_art)-1):
			result += ","
	result +="],\"two_aci\":["

	for i in range(len(two_aci)):
		result += "\""+str(two_aci[i]['control_line'])+"\""
		if i < (len(two_aci)-1):
			result += ","
	result +="],\"two_art\":["

	for i in range(len(two_art)):
		result += "\""+str(two_art[i]['control_line'])+"\""
		if i < (len(two_art)-1):
			result += ","
	result +="],\"trd_aci\":["

	for i in range(len(trd_aci)):
		result += "\""+str(trd_aci[i]['control_line'])+"\""
		if i < (len(trd_aci)-1):
			result += ","
	result +="],\"trd_art\":["

	for i in range(len(trd_art)):
		result += "\""+str(trd_art[i]['control_line'])+"\""
		if i < (len(trd_art)-1):
			result += ","
	result +="]}"

	return HttpResponse(result,content_type="application/json")

def batchYear(year,province):
	batchs = list(models.BatchLine.objects.values().filter(fare_year= year,fare_lend = province))
	data = json.dumps(batchs)
	return HttpResponse(data)


def searchPro(search,start,pageSize):
	cursor = connection.cursor()
	cursor.execute("""select a.id as proid,a.que_text,a.que_time,b.oppen_id,b.user_name ,b.user_head 
					  from home_questions as a left join home_user as b on a.questioner = b.oppen_id 
					  where a.que_text like '%"""+search+"""%'order by a.que_time desc limit """+start+","+pageSize)
	rows = dictfetchall(cursor)
	result = "{\"problems\":["
	for i in range(len(rows)):
		answers = models.queAnswer.objects.values().filter(question_id = rows[i]['proid'])
		views =  models.quetionViews.objects.values().filter(question_id = rows[i]['proid'])		
		
		result += "{\"prokey\":\""+str(rows[i]['proid'])+"\","
		if answers:
			result += "\"ansnum\":\""+str(len(answers))+"\","
		if views:
			result += "\"viewnum\":\""+str(len(views))+"\","
		result += "\"procontext\":\""+rows[i]['que_text']+"\","
		result += "\"protime\":\""+str(rows[i]['que_time'])+"\","
		enddate = datetime.datetime.now()
		times = (enddate-rows[i]['que_time']).seconds
		dates = (enddate-rows[i]['que_time']).days
		if dates>0:
			result += "\"diffd\":\""+dateDifference(dates)+"\","
		else:
			result += "\"diffd\":\""+timeDifference(times)+"\","
		result += "\"openid\":\""+rows[i]['oppen_id']+"\","
		result += "\"uname\":\""+rows[i]['user_name']+"\","
		result += "\"uhead\":\""+rows[i]['user_head']+"\"}"
		if i< (len(rows)-1):
			result += ","
	result += "]}"
	return HttpResponse(result,content_type="application/json")

def question(prokey):
	cursor = connection.cursor()
	cursor.execute("""select a.id as proid,a.que_text,a.que_time,b.oppen_id,b.user_name ,b.user_head 
					  from home_questions as a left join home_user as b on a.questioner = b.oppen_id
					  where a.id = """+prokey)
	rows = dictfetchall(cursor)
	answers = models.queAnswer.objects.values('answers').filter(question_id=prokey)

	if answers:
		result = "{\"nums\":\""+str(len(answers))+"\","
	else:
		result = "{\"nums\":\"0\","
	result += "\"prokey\":\""+str(rows[0]['proid'])+"\","
	result += "\"procontext\":\""+rows[0]['que_text']+"\","
	result += "\"protime\":\""+str(rows[0]['que_time'])+"\","
	result += "\"openid\":\""+rows[0]['oppen_id']+"\","
	result += "\"uname\":\""+rows[0]['user_name']+"\","
	result += "\"uhead\":\""+rows[0]['user_head']+"\"}"
	return HttpResponse(result,content_type="application/json")

def answerList(prokey,start,pageSize):
	# return HttpResponse("ddd")
	cursor = connection.cursor()
	cursor.execute("""select a.question_id,a.ans_text,a.ans_time,b.oppen_id,b.user_name,b.user_head 
					  from home_queanswer as a left join home_user as b on a.answers = b.oppen_id 
					  where a.question_id ="""+prokey+" order by a.ans_time desc limit "+start+","+pageSize)
	rows = dictfetchall(cursor)
	# if rows:
	result = "{\"nums\":\""+str(len(rows))+"\",\"answerlist\":["
	for i in range(len(rows)):
		result += "{\"quekey\":\""+str(rows[i]['question_id'])+"\","
		result += "\"anscontext\":\""+rows[i]['ans_text']+"\","
		result += "\"ansdate\":\""+str(rows[i]['ans_time'])+"\","
		result += "\"userid\":\""+rows[i]['oppen_id']+"\","
		result += "\"uname\":\""+rows[i]['user_name']+"\","
		result += "\"uhead\":\""+rows[i]['user_head']+"\"}"
		if i< (len(rows)-1):
			result += ","
	result += "]}"
	return HttpResponse(result,content_type="application/json")

def problemView(prokey,userid):
	try:
		quetionview = models.quetionViews(views = userid,question_id = prokey)
		quetionview.save()
		return HttpResponse("success")
	except Exception as error:
		return HttpResponse(error)


def askProblem(problem,userid,askdate):
	try:
		question = models.Questions(que_text=problem,questioner=userid,que_time=askdate)
		question.save()
		return HttpResponse("success")
	except Exception as error:
		return HttpResponse(error)
def userAnwswer(answer,userid,ansdate,queid):
	try:
		queanswer = models.queAnswer(answers = userid,ans_time=ansdate,ans_text= answer,question_id = queid)
		queanswer.save()
		user = models.User.objects.values().filter(oppen_id = userid)
		question = models.Questions.objects.values().filter(id = queid)
		userque = models.User.objects.values().filter(oppen_id = question[0]['questioner'])

		new = models.news(user_id = userque[0]['id'],new_context=user[0]['id'],new_date=ansdate,question=queid,readed ='no' )
		new.save()
		return HttpResponse("success")
	except Exception as error:
		return HttpResponse(error)

def newsList(userid):
	user = models.User.objects.values().filter(oppen_id = userid)
	cursor = connection.cursor()
	cursor.execute("""select a.*,b.user_name,b.oppen_id from home_news as a left join home_user as b 
					  on a.new_context=b.id where readed = 'no' and user_id="""+str(user[0]['id']))
	rows = dictfetchall(cursor)

	result = "{\"newslist\":["
	if rows:
		for i in range(len(rows)):
			result += "{\"newcont\":\""+rows[i]['user_name']+"\","
			result += "\"newdate\":\""+str(rows[i]['new_date'])+"\","
			result += "\"ansid\":\""+rows[i]['oppen_id']+"\","
			result += "\"prokey\":\""+rows[i]['question']+"\","
			result += "\"newid\":\""+str(rows[i]['id'])+"\"}"
			if i<(len(rows)-1):
				result +=","
		result += "]}"
		return HttpResponse(result,content_type="application/json")
	else:
		return HttpResponse('')

def userAskProblems(start,pageSize,userid):
	cursor = connection.cursor()
	cursor.execute("""select a.id as proid,a.que_text,a.que_time,b.oppen_id,b.user_name ,b.user_head 
					  from home_questions as a left join home_user as b on a.questioner = b.oppen_id 
					  where questioner='"""+userid+"' order by a.que_time desc limit "+start+","+pageSize)
	rows = dictfetchall(cursor)
	result = "{\"problems\":["
	for i in range(len(rows)):
		result += "{\"context\":\""+rows[i]['que_text']+"\","
		result += "\"ckey\":\""+str(rows[i]['proid'])+"\","
		result += "\"protime\":\""+str(rows[i]['que_time'])+"\","
		result += "\"openid\":\""+rows[i]['oppen_id']+"\","
		result += "\"uname\":\""+rows[i]['user_name']+"\","
		result += "\"uhead\":\""+rows[i]['user_head']+"\"}"
		if i< (len(rows)-1):
			result += ","
	result += "]}"
	return HttpResponse(result,content_type="application/json")

def userAnsProblems(start,pageSize,userid):
	cursor = connection.cursor()
	cursor.execute("""select a.question_id,a.ans_text,a.ans_time,b.oppen_id,b.user_name,b.user_head, 
					  c.que_text,d.user_name as askname from home_queanswer as a left join 
					  home_user as b on a.answers = b.oppen_id left join home_questions as c 
					  on a.question_id = c.id left join home_user as d on c.questioner=d.oppen_id
					  where a.answers ='"""+userid+"' order by a.ans_time desc limit "+start+","+pageSize)
	rows = dictfetchall(cursor)
	result = "{\"answers\":["
	for i in range(len(rows)):
		result += "{\"context\":\""+rows[i]['ans_text']+"\","
		result += "\"ckey\":\""+str(rows[i]['question_id'])+"\","
		result += "\"protime\":\""+str(rows[i]['ans_time'])+"\","
		result += "\"openid\":\""+rows[i]['oppen_id']+"\","
		result += "\"uname\":\""+rows[i]['user_name']+"\","
		result += "\"askcontext\":\""+rows[i]['que_text']+"\","
		result += "\"askname\":\""+rows[i]['askname']+"\","
		result += "\"uhead\":\""+rows[i]['user_head']+"\"}"
		if i< (len(rows)-1):
			result += ","
	result += "]}"
	return HttpResponse(result,content_type="application/json")
def newsDetail(prokey,userid,newdate):
	cursor = connection.cursor()
	cursor.execute("""select a.que_text,b.user_name as uname,c.ans_text,c.ans_time,
					  d.user_name,d.user_head from home_questions as a left join 
					  home_user as b on a.questioner = b.oppen_id left join 
					  home_queanswer as c on a.id = c.question_id left join 
					  home_user as d on c.answers = d.oppen_id 
					  where a.id = """+prokey+" and c.answers='"+userid+"' and ans_time = '"+newdate+"'")
	rows = dictfetchall(cursor)
	result = "{\"ansname\":\""+rows[0]['user_name']+"\","
	result += "\"anshead\":\""+rows[0]['user_head']+"\","
	result += "\"ansdate\":\""+str(rows[0]['ans_time'])+"\","
	result += "\"anscontext\":\""+rows[0]['ans_text']+"\","
	result += "\"askname\":\""+rows[0]['uname']+"\","
	result += "\"askcontext\":\""+rows[0]['que_text']+"\"}"
	return HttpResponse(result,content_type="application/json")

def updateNew(newid):
	try:
		models.news.objects.filter(id = newid).update(readed = 'yes')
		return HttpResponse("success")
	except Exception as error:
		return HttpResponse(error)

def addArticleViews(articlekey,userid,readdate):
	try:		
		readrecord = models.readRecord(article_id= articlekey,open_id = userid)
		readrecord.save()
		artview = models.readCollect.objects.values().filter(user = userid ,article_id= articlekey,read_collect = 'read')
		if artview:
			pass
		else:
			articleview = models.readCollect(article_id = articlekey,user = userid,read_date=readdate,read_collect='read')
			articleview.save()
		return HttpResponse('success')
	except Exception as error:
		return HttpResponse(error)

def articleCollect(artkey,userid,colldate):
	try:
		collexist = models.readCollect.objects.values().filter(user = userid,article_id = artkey,read_collect = 'coll')
		if collexist:
			pass
		else:
			collect = models.readCollect(article_id = artkey,user =userid,read_date =colldate,read_collect = 'coll')
			collect.save()
		return HttpResponse('success')
	except Exception as error:
		return HttpResponse(error)
def notArticleCollect(artkey,userid):
	try:
		models.readCollect.objects.filter(user = userid,article_id = artkey,read_collect = 'coll').delete()
		return HttpResponse('success')
	except Exception as error:
		return HttpResponse(error)

def articleDetail(articlekey,userid):
	article = models.Article.objects.values().filter(id=articlekey)
	views = models.readRecord.objects.values().filter(article_id=articlekey)
	collect = models.readCollect.objects.values().filter(article_id = articlekey,user= userid,read_collect='coll')


	result = "{\"tittle\":\""+article[0]['tittle']+"\","
	if collect:
		result += "\"collect\":\"coll\","
	else:
		result += "\"collect\":\"notc\","
	result += "\"context\":\""+article[0]['context'].replace('"',"'")+"\","
	result += "\"artkey\":\""+str(article[0]['id'])+"\","
	result += "\"artdate\":\""+str(article[0]['art_date'])+"\","
	result += "\"views\":\""+str(len(views))+"\"}"

	return HttpResponse(result,content_type="application/json")
def getMoreArticle(catekey,start,pageSize):
	# article = models.Article.objects.values().filter(cate_id = catekey)
	cursor = connection.cursor()
	cursor.execute("select * from home_article where cate_id="+catekey+" order by art_date desc limit "+start+","+pageSize)
	article = dictfetchall(cursor)
	result = "{\"articleList\":["
	for i in range(len(article)):
		result += "{\"tittle\":\""+article[i]['tittle']+"\","
		result += "\"artkey\":\""+str(article[i]['id'])+"\","
		result += "\"artdate\":\""+str(article[i]['art_date'])+"\","
		# dr = re.compile(r'<[^>]+>',re.S)
		# result += "\"context\":\""+dr.sub('',article[i]['context'].replace('"',"“"))[:45]+"..\"}"
		result += "\"context\":\""+filter_tags(article[i]['context']).replace('"','“')[:45]+"..\"}"
		if i<(len(article)-1):
			result += ","
	result +="]}"
	return HttpResponse(result,content_type="application/json")

def getReadArticle(userid,start,pageSize):
	cursor = connection.cursor()
	cursor.execute("""select b.*,c.detail_name,a.read_date from home_readcollect as a left join home_article as b
					  on a.article_id = b.id left join home_digdetail as c 
					  on b.cate_id = c.id where read_collect='read' and
					  user='"""+userid+"' order by read_date desc limit "+start+","+pageSize)
	article = dictfetchall(cursor)
	result = "{\"articleList\":["
	for i in range(len(article)):
		result += "{\"tittle\":\""+article[i]['tittle']+"\","
		result += "\"artkey\":\""+str(article[i]['id'])+"\","
		result += "\"artdate\":\""+str(article[i]['read_date'])+"\","
		result += "\"classname\":\""+article[i]['detail_name']+"\","
		# dr = re.compile(r'<[^>]+>',re.S)
		# result += "\"context\":\""+dr.sub('',article[i]['context'].replace('"','“'))[:45]+"..\"}"
		result += "\"context\":\""+filter_tags(article[i]['context']).replace('"','“')[:45]+"..\"}"
		if i<(len(article)-1):
			result += ","
	result +="]}"
	return HttpResponse(result,content_type="application/json")


def getCollArticle(userid,start,pageSize):
	cursor = connection.cursor()
	cursor.execute("""select b.*,c.detail_name,a.read_date from home_readcollect as a left join home_article as b
					  on a.article_id = b.id left join home_digdetail as c 
					  on b.cate_id = c.id where read_collect='coll' and
					  user='"""+userid+"' order by read_date desc limit "+start+","+pageSize)
	article = dictfetchall(cursor)
	result = "{\"articleList\":["
	for i in range(len(article)):
		result += "{\"tittle\":\""+article[i]['tittle']+"\","
		result += "\"artkey\":\""+str(article[i]['id'])+"\","
		result += "\"artdate\":\""+str(article[i]['read_date'])+"\","
		result += "\"classname\":\""+article[i]['detail_name']+"\","
		# dr = re.compile(r'<[^>]+>',re.S)
		# result += "\"context\":\""+dr.sub('',article[i]['context'])[:45]+"..\"}"
		result += "\"context\":\""+filter_tags(article[i]['context']).replace('"','“')[:45]+"..\"}"
		if i<(len(article)-1):
			result += ","
	result +="]}"
	return HttpResponse(result,content_type="application/json")

def majorList(search,start,pageSize):
	cursor = connection.cursor()
	cursor.execute("select * from home_professional where profes_name like '%"+search+"%' limit "+start+","+pageSize)
	rows = dictfetchall(cursor)

	result = "{\"majorList\":["
	for i in range(len(rows)):
		result += "{\"majorid\":\""+rows[i]['profes_id']+"\","
		result += "\"majorname\":\""+rows[i]['profes_name']+"\","
		result += "\"cate\":\""+rows[i]['profess_class']+"\","
		if(len(rows[i]['related'])>44):
			result += "\"related\":\""+rows[i]['related'][:44]+"..\"}"
		else:
			result += "\"related\":\""+rows[i]['related'][:44]+"\"}"
		if i < (len(rows)-1):
			result += ","
	result += "]}"
	return HttpResponse(result,content_type="application/json")

def majorDetail(pid):
	major = models.professional.objects.values().filter(profes_id = pid)

	result = "{\"pid\":\""+major[0]['profes_id']+"\","
	result += "\"pname\":\""+major[0]['profes_name']+"\","
	result += "\"related\":\""+major[0]['related']+"\","
	result += "\"pclass\":\""+major[0]['profess_class']+"\","
	result += "\"mclass\":\""+major[0]['main_class']+"\","
	result += "\"practice\":\""+major[0]['practice']+"\","
	result += "\"objective\":\""+major[0]['objective']+"\","
	result += "\"trequire\":\""+major[0]['tra_require']+"\","
	result += "\"direction\":\""+major[0]['direction']+"\"}"
	return HttpResponse(result,content_type="application/json")

def majorScore(start,pageSize,searchm,searchc):
	cursor = connection.cursor()

	cursor.execute("select * from home_majorscore where major_name like '%"+searchm+"%' and school_name like '%"+searchc+"%' limit "+start+","+pageSize)
	rows = dictfetchall(cursor)
	result = "{\"scorelist\":["
	for i in range(len(rows)):
		result += "{\"major_name\":\""+rows[i]['major_name']+"\","
		result += "\"school_name\":\""+rows[i]['school_name']+"\","
		result += "\"aver_score\":\""+rows[i]['aver_score']+"\","
		result += "\"highest\":\""+rows[i]['highest']+"\","
		result += "\"student_loca\":\""+rows[i]['student_loca']+"\","
		result += "\"category\":\""+rows[i]['category']+"\","
		result += "\"par_year\":\""+rows[i]['par_year']+"\","
		result += "\"batch\":\""+rows[i]['batch']+"\"}"
		if i < (len(rows)-1):
			result += ","
	result += "]}"

	return HttpResponse(result,content_type = "application/json")


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def filter_tags(htmlstr):
	dr = re.compile(r'<[^>]+>',re.S)
	s = dr.sub('',htmlstr)
	s=replaceCharEntity(s)#替换实体
	return s


def replaceCharEntity(htmlstr):
	CHAR_ENTITIES={'nbsp':' ','160':' ','lt':'<','60':'<',
					'gt':'>','62':'>','amp':'&','38':'&','quot':'"','34':'"',}
	re_charEntity=re.compile(r'&#?(?P<name>\w+);')
	sz=re_charEntity.search(htmlstr)
	while sz:
		entity=sz.group()#entity全称，如&gt;
		key=sz.group('name')#去除&;后entity,如&gt;为gt
		try:
			htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
			sz=re_charEntity.search(htmlstr)
		except KeyError:
			htmlstr=re_charEntity.sub('',htmlstr,1)
			sz=re_charEntity.search(htmlstr)
	return htmlstr

def timeDifference(times):
	s = ""
	if times < 60:
		s = "刚刚"
	elif (times/60)<60:
		s = str((int(times/60)))+"分钟前"
	elif (times/3600)<24:
		s = str(int(times/3600))+"小时前"
	else:
		s = str(int(times/86400))+"天前"
	return s

def dateDifference(dates):
	s = ""
	if dates <30:
		s = str(dates)+"天前"
	elif (dates/30)<12:
		s = str(int(dates/30))+"月前"
	else:
		s = str(int(dates/360))+"年前"
	return s


