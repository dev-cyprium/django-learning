from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return "[{date}]: {text}".format(date=self.pub_date, text=self.question_text)
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)
	choice_text = models.CharField(max_length=200)
	
	def __str__(self):
		return "{choice_text}: {votes}".format(choice_text=self.choice_text, votes=self.votes)