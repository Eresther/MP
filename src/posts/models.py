from __future__ import unicode_literals

from django.db import models

# Create your models here.
#MVC MODEL VIEW CONTROLLER

#Create Post Table
class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

class Processor(models.Model):
	proc_model = models.CharField(max_length=100)
	proc_socket = models.IntegerField()
	proc_watts = models.IntegerField()
	proc_content = models.TextField()
	proc_cost = models.IntegerField()
	proc_image = models.FileField(null=True,blank=True, upload_to='media')
	proc_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.proc_model

class Motherboard(models.Model):
	mobo_model = models.CharField(max_length=100)
	mobo_socket = models.IntegerField()
	mobo_watts = models.IntegerField()
	mobo_content = models.TextField()
	mobo_cost = models.IntegerField()
	mobo_image = models.FileField(null=True,blank=True)
	mobo_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.mobo_model

class Memory(models.Model):
	mem_model = models.CharField(max_length=100)
	mem_socket = models.IntegerField()
	mem_watts = models.IntegerField()
	mem_content = models.TextField()
	mem_cost = models.IntegerField()
	mem_image = models.FileField(null=True,blank=True)
	mem_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.mem_model

class Storage(models.Model):
	store_model = models.CharField(max_length=100)
	store_watts = models.IntegerField()
	store_content = models.TextField()
	store_cost = models.IntegerField()
	store_image = models.FileField(null=True,blank=True)
	store_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.store_model

class GPU(models.Model):
	GPU_model = models.CharField(max_length=100)
	GPU_watts = models.IntegerField()
	GPU_content = models.TextField()
	GPU_cost = models.IntegerField()
	GPU_image = models.FileField(null=True,blank=True)
	GPU_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.GPU_model

class PSU(models.Model):
	PSU_model = models.CharField(max_length=100)
	PSU_watts = models.IntegerField()
	PSU_content = models.TextField()
	PSU_cost = models.IntegerField()
	PSU_image = models.FileField(null=True,blank=True)
	PSU_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.PSU_model

class Case(models.Model):
	case_model = models.CharField(max_length=100)
	case_content = models.TextField()
	case_cost = models.IntegerField()
	case_image = models.FileField(null=True,blank=True)
	case_qty = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.case_model

class Contact(models.Model):
	email = models.EmailField(max_length=120)
	subject = models.CharField(max_length=120)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.email

class Order(models.Model):
	email = models.EmailField(max_length=120)
	proc = models.ForeignKey('Processor')
	mem = models.ForeignKey('Memory')
	stor = models.ForeignKey('Storage')
	gpu = models.ForeignKey('GPU')
	psu = models.ForeignKey('PSU')
	mobo = models.ForeignKey('Motherboard')
	case = models.ForeignKey('Case')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return str(self.email)