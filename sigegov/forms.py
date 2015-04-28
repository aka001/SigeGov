from haystack.forms import SearchForm
from django import forms
class PublicationsSearchForm(SearchForm):
	def no_query_found(self):
		return self.searchqueryset.all()

class UploadEventForm(forms.Form):
	event = forms.CharField(max_length=50)
	organiser = forms.CharField(max_length=50)
	attachment = forms.FileField()
	
