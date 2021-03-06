#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'azrael'

'''
Configuration
'''

import config_default

class Dict(dict):
	'''
	simple dict but support access as s.y style
	'''
	def __init__(self, names=(), values=(), **kw):
		super(Dict, self).__init__(**kw)
		for k, v in zip(names,  values):
			self[k] = v

	def __getter__(slef, key):
		try:
			self[key]
		except KeyError:
			raise AttributeError(r"'DIct' object has no attribute '%s'" % key)

	def __setter__(self, key, value):
		self[key] = value

def merge(defaults, override):
	r = {}
	for k, v in defaults.iteritems():
		if k in override:
			if isinstance(v, dict):
				r[k] = merge(v, override[k])
			else:
				r[k] = override[k]
		else:
			r[k] = v
	return r

def toDict(d):
	D = Dict()
	for k, v in d.iteritems():
		D[k] = toDict(v) if isinstance(v, dict) else v
	return D

configs = config_default.configs

try:
	import config_override
	configs = merge(configs, config_override.configs)
except ImportError:
	pass
configs = toDict(configs)
print configs