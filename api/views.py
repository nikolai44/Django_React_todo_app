from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .models import TaskModel
import simplejson


class TaskListView(View):
	"""all task list"""
	def get(self, request):
		data = TaskModel.objects.all().serialize()
		return HttpResponse(data, status=200, content_type='application/json')


class TaskDetailView(View):
	"""CRUD one task"""
	def get(self, request, task_id, *args, **kwargs):
		"""RETRIEVE task by task_id"""
		data = TaskModel.objects.get(id=task_id).serialize()
		return HttpResponse(data, status=200, content_type='application/json')

	def post(self, request, *args, **kwargs):
		"""CREATE new task"""
		data = simplejson.loads(request.body)
		task = TaskModel()
		task.title = data['title']
		task.completed = data['completed']
		task.save()
		return HttpResponse(status=200)

	def put(self, request, task_id, *args, **kwargs):
		"""UPDATE task by task_id"""
		data = simplejson.loads(request.body)
		if not TaskModel.objects.filter(id=task_id).exists():
			return HttpResponse(status=400)
		task = TaskModel.objects.get(id=task_id)
		task.title = data['title']
		task.completed = data['completed']
		task.save()
		return HttpResponse(status=200)

	def delete(self, request, task_id, *args, **kwargs):
		"""DELETE by task_id"""
		TaskModel.objects.get(id=task_id).delete()
		return HttpResponse(status=200)
