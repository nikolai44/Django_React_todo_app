from django.http import Http404
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TaskModel


class TaskListView(APIView):
	"""all task list"""
	def get(self, request):
		queryset = TaskModel.objects.all().order_by('-id')
		serializer = TaskSerializer(queryset, many=True)
		return Response(serializer.data)


class TaskDetailView(APIView):
	"""CRUD one task"""
	def get_object(self, pk):
		try:
			return TaskModel.objects.get(pk=pk)
		except TaskModel.DoesNotExist:
			raise Http404

	def get(self, request, task_id):
		"""RETRIEVE task by task_id"""
		query = TaskModel.objects.get(id=task_id)
		serializer = TaskSerializer(query)
		return Response(serializer.data)

	def post(self, request):
		"""CREATE new task"""
		task = TaskModel()
		serializer = TaskSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(request.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, task_id):
		"""UPDATE task by task_id"""
		task = self.get_object(task_id)
		serializer = TaskSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(request.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, task_id):
		"""DELETE by task_id"""
		task = self.get_object(task_id)
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
