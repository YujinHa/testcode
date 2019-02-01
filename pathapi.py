#!/usr/bin/env python
#coding:utf8
import sys
import re #regular expression의 약자(정규 표현식)

path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 project를 반환한다.
	"""
	#레귤러 익스프레션-괄호:그룹화,\S:문자열 검색,^/:아무거나,+:이상
	p = re.findall('/project/(\w+)', path.replace("\\","/")) 
	if len(p) != 1:
		return "","경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로를 넣으면 seq를 반환한다.
	"""
	p = re.findall('/shot/(\w+)', path.replace("\\","/")) 
	if len(p) != 1:
		return "","경로에서 seq 정보를 가지고 올 수 없습니다."
	return p[0], None

def shot(path):
	"""
	경로를 넣으면 shot을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w+)', path.replace("\\","/")) 
	if len(p) != 1:
		return "","경로에서 shot 정보를 가지고 올 수 없습니다."
	return p[0], None

def task(path):
	"""
	경로를 넣으면 task를 반환한다.
	"""
	p = re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/")) 
	if len(p) != 1:
		return "","경로에서 task 정보를 가지고 올 수 없습니다."
	return p[0], None

def ver(path):
	"""
	경로를 넣으면 버전을 반환한다.
	"""
	p = re.findall("_v(\d+)", path.replace("\\","/")) 
	if len(p) != 1:
		return 0,"경로에서 버전 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

def seqnum(path):
	"""
	경로를 넣으면 시퀀스넘버를 반환한다.
	"""
	p = re.findall('(\d+)\.\w+$', path.replace("\\","/")) 
	if len(p) != 1:
		return -1,"경로에서 시퀀스 넘버 정보를 가지고 올 수 없습니다."
	return int(p[0]), None
	
def digitnum(path):
	p = re.findall('(\d+)\.\w+$', path.replace("\\","/")) 
	if len(p) != 1:
		return -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다"
	return len(p[0],None)

def toFFmpeg(path):
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return path, "경로가 시퀀스 구조가 아닙니다."
	digiNum = len(p[0])
	head, tail = path.split(p[0])
	return "%s%%%dd%s" % (head,digitNum,tail), None
