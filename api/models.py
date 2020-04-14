from django.db import models
import simplejson


class TaskQuerySet(models.QuerySet):
	def serialize(self):
		values = list(self.values('id', 'title', 'completed'))
		return simplejson.dumps(values)


class TaskManager(models.Manager):
	def get_queryset(self):
		return TaskQuerySet(self.model, using=self._db)


class TaskModel(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False, blank=True, null=True)
	objects = TaskManager()

	def __str__(self):
		return self.title

	def serialize(self):
		"""[{"id":53,"title":"koshka1","completed":false}]"""
		data = {
			'id': self.pk,
			'title': self.title,
			'completed': self.completed,
		}
		return simplejson.dumps(data)

