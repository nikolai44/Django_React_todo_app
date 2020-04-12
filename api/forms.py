from django import forms
from .models import TaskModel


class TaskForm(forms.Form):
	id = forms.IntegerField(min_value=0)
	title = forms.CharField(max_length=200, required=True)
	completed = forms.BooleanField(required=True)

	def clean(self):
		data = self.cleaned_data
		id = data.get('id', None)
		title = data.get('title', None)
		completed = data.get('completed', None)
		if id is None:
			raise forms.ValidationError('empty task_id', code='empty')
		if title is None and completed is None:
			raise forms.ValidationError('empty data', code='empty')
		if not TaskModel.objects.filter(id=id).exists():
			raise forms.ValidationError('invalid task_id', code='invalid')
		return data
