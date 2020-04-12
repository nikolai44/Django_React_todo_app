from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .models import TaskModel
from .forms import TaskForm
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
		print(request.body)
		form = TaskForm(simplejson.loads(request.body))
		if form.is_valid():
			form.save()
			return HttpResponse(status=200)
		errors = simplejson.dumps(form.errors)
		return HttpResponse(errors, status=200, content_type='application/json')

	def put(self, request, task_id, *args, **kwargs):
		"""UPDATE task by task_id"""
		pass

	def delete(self, request, task_id, *args, **kwargs):
		"""DELETE by task_id"""
		TaskModel.objects.get(id=task_id).delete()
		return HttpResponse(status=200)


