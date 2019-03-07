from django.db import models

# Create your models here.

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	#date = models.DateField()
	#time = models.TimeField()

	def __str__(self):
		return self.item + ' | ' + str(self.completed) 