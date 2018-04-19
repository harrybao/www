# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from django.db import connection
import json
import requests
from django.core import serializers

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
			user = models.User(oppen_id = userid,user_name=nickName,user_head =avatarUrl)
			user.save()
			return HttpResponse('success')

		if ac == 'artitle':
			return artitle()

		if ac == 'schooList':
			return schooList()

			


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
	return HttpResponse(result)

	# cursor = connection.cursor()
	# cursor.execute("select * from home_school limit 6")
	# rows = dictfetchall(cursor)
	# for i in range(len(rows)):
	# 	cur = connection.cursor()
	# 	cur.execute("select school_pic from home_schoolimg where school_id='%s'" % rows[i]['school_id'])
	# 	rowspic = dictfetchall(cur)
	# 	result +="{\"colname\":\""+rows[i]['school_name']+"\","
	# 	result +="\"badge\":\""badgerows[i]['school_badge']+"\","
	# 	result +="\"colid\":\""+rows[i]['school_id']+"\","
	# 	result +="\"colpic\":\""+PIC_URL+rowspic[0]['school_pic']+"\","
	# 	result +="\"coladd\":\""+rows[i]['school_address']+"\"}"
	# 	if i<(len(rows)-1):
	# 		result +=","
	# result +="]}"
	# return HttpResponse(result)

def detailsch(schkey):
	school = models.School.objects.values().filter(school_id=schkey)
	pictures = models.SchoolImg.objects.values().filter(school_id=schkey)

	result = "{\"schname\":\""+school[0]['school_name']+"\","
	result +="\"schmotto\":\""+school[0]['school_motto']+"\","
	result +="\"schaddress\":\""+school[0]['school_address']+"\","
	result +="\"schloca\":\""+school[0]['school_location']+"\","
	result +="\"schmold\":\""+school[0]['school_mold']+"\","
	result +="\"schbelong\":\""+school[0]['school_belong']+"\","
	result +="\"schurl\":\""+school[0]['school_url']+"\","
	result +="\"schtel\":\""+school[0]['school_tel']+"\","
	result +="\"abst\":\""+school[0]['school_abst'].replace(' ','')+"\","
	result +="\"piclist\":["
	for i in range(3):
		result +="\"{schpic\":\""+PIC_URL+pictures[i]['school_pic']+"\"}"
		if i<2:
			result+=","
	result +="]}"




	# cursor = connection.cursor()
	# cursor.execute("select * from home_school where school_id ='%s'" %schkey)
	# rows =dictfetchall(cursor)
	# result = "{\"abst\":\""+school[0]['school_abst']+"\"}"
	return HttpResponse(result)

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
	knowtitles = models.Article.objects.values().filter(cate_id ='2')[0:4]
	waytitles = models.Article.objects.values().filter(cate_id ='3')[0:4]
	result = "{"
	if knowtitles:
		result += "\"ktitles\":["
		for i in range(len(knowtitles)):
			result += "{\"kkey\":\""+str(knowtitles[i]['id'])+"\","
			result += "\"title\":\""+knowtitles[i]['tittle']+"\"}"
			if i<(len(knowtitles)-1):
				result +=","
		result +="],"
	if waytitles:
		result += "\"wtitles\":["
		for i in range(len(waytitles)):
			result += "{\"wkey\":\""+str(waytitles[i]['id'])+"\","
			result += "\"title\":\""+waytitles[i]['tittle']+"\"}"
			if i<(len(waytitles)-1):
				result +=","
		result +="]"
	result +="}"
	return HttpResponse(result)

def schooList():
	schools = models.School.objects.values()

	result = "{\"schoolist\":["
	if schools:
		for i in range(len(schools)):
			result += "{\"skey\":\""+schools[i]['school_id']+"\","
			result += "\"sname\":\""+schools[i]['school_name']+"\","
			result += "\"saddress\":\""+schools[i]['school_address']+"\","
			result += "\"sbadge\":\""+PIC_URL+schools[i]['school_badge']+"\"}"
			if i< (len(schools)-1):
				result +=","
		result += "]}"
	return HttpResponse(result)
	# schools = list(models.School.objects.values("school_badge","school_name","school_id",schoo))
	# data = json.dumps(schools)
	return HttpResponse(data)



def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
