from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	#user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=40)
	

	def __str__(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(Todo, on_delete=models.CASCADE)
	text = models.CharField(max_length=80)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.text
	
		
		