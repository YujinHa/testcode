#!/usr/bin/env python
#coding:utf8
import os
import sys
import subprocess

def searchExt(rootPath, ext):
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if root == rootPath:
			continue
		for f in files:
			basename, e = os.path.splitext(f)
			if e !=  ext:
				continue
			if dirs:
				results.append("/".join([root]+dirs+[f]))
			else:
				results.append("/".join([root,f]))
	return results

def proxyPath(p):
"""
경로를 입력받고 Proxy 경로를 반환한다.
"/project/circle/in/aces_exr/aaa/test.0001.exr"
"/project/circle/in/aces_exr/aaa_proxy/test.0001.exr"
"""
	if os.path.isdir(p):
		#폴더인데 끝이 "/"로 끝나면 "/"를 제거후 _proxy를 붙힌다.
		if p.endwiths("/"):
			return p[:-1] + "_proxy"
		#폴더라면 그냥 _proxy를 붙힌다.
		return p + "proxy"
	d, f = os.path.split(p)
	return d+"_proxy"

def genProxy(files):
"""
proxy 이미지를 생성한다
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
#	print 
#	l = len(exrs)
#	~/tmp/proxy -f image2 -start_number 078471 -r 24 -i ~/tmp/proxy/A003C025_150830_R0D0.%6d.jpg -vframes l -vcodec 1ibx264 -vf scale=1280:-1 -color_primaries bt709 -color_trc bt709 -colorspace bt709 output.mov

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	proxy = "tmp/proxy"
	item = searchExt(root,".exr")
	genProxy(item)
