from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
	""""""
	class Meta:
		"""docstring for Meta"""
		model = Topic
		fields = ['text']
		labels = {'text':''}
class EntryForm(forms.ModelForm):
	"""docstring for EntryForm"""
	class  Meta:
		"""docstring for  Meta"""
		model = Entry
		fields = ['text']
		labels = {'text':''}
		widgets = {'text':forms.Textarea(attrs={'cols':80})}
			
	
		
