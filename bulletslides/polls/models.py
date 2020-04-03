from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):

	#variables
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	#string output for question_text
	def __str__(self):
		return self.question_text

	#returns true if published in last day
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	#variable, Question object as argument
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#other vars
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


	#string output for choice_text
	def __str__(self):
		return self.choice_text