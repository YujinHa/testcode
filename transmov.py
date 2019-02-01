#!/usr/bin/env python
#coding:utf8
import os
import sys
import subprocess
import pathapi

def searchExt(rootPath, ext):
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if root == rootPath:
			continue
		for f in files:
			basename, e = os.path.splitext(f)
			if e !=  ext:
				continue
			results.append("/".join([root]+dirs+[f]))
	return results

def genProxy(proxy, files):
	"""
	file 리스트를 받아서 proxy경로에 프록시 이미지를 생성한다.
	"""
	for src in files:
		p, f = os.path.split(src)
		basename,ext = os.path.splitext(f)
		proxyDir = proxy + p
		if not os.path.exists(proxyDir):
			os.makedir(proxyDir)
		dst = proxyDir + "/" + basename + ".jpg"
		cmd = ["convert", src, dst]
		p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		if err:
			sys.stderr.write(err)
		sys.stdout.write(out)

def genMov(rootPath,ext):
	"""
	path 경로에 있는 파일을 이용해서 mov를 생성한다.
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if not files:
			continue
		files.sort()
		start = "/".join([root]+dirs+[files[0]])
		end = "/".join([root]+dirs+[files[-1]])
		seqfile, err = pathapi.toffmpeg(start)
		if err:
			sys.stderr.write(err)
		startframe, err = pathapi.sequm(start)
		if err:
			sys.stderr.write(err)
		errframe, err = pathapi.sequm(end)
		if err:
			sys.stderr.write(err)
		print seqfile, startframe, endframe

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	proxy = "tmp/proxy"
	items = searchExt(root,".exr")
	genMov(proxy + root, ".jpg")
