import datetime
from haystack import indexes
from sigegov.models import Publications
from django.template import RequestContext, loader, Context

class PublicationsIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document = True, use_template = True)
	document_id = indexes.CharField(model_attr = 'document_id')
	state = indexes.CharField(model_attr = 'state')
        category = indexes.CharField(model_attr = 'category')
	project_title = indexes.CharField(model_attr = 'project_title')
	department_name = indexes.CharField(model_attr = 'department_name')
        #date = indexes.CharField(model_attr = 'date')
	
	project_title_auto = indexes.EdgeNgramField(model_attr='project_title')
	department_name_auto = indexes.EdgeNgramField(model_attr='department_name')
	state_auto = indexes.EdgeNgramField(model_attr='state')
	#date_auto = indexes.EdgeNgramField(model_attr='date')
	category_auto = indexes.EdgeNgramField(model_attr='category')

	def get_model(self):
		return Publications
	
	def index_queryset(self, using=None):
		return self.get_model().objects.all()
	
	def prepare(self, obj):
		data = super(PublicationsIndex, self).prepare(obj)
		if obj.attachment:
			file_data = self._get_backend(None).extract_file_contents(
				 obj.attachment,
				)
			template = loader.select_template(
				("search/indexes/sigegov/publications_text.txt", ),
				)
			data["text"] = template.render(Context({
						"object": obj,
						"file_data": file_data,
				}))
			return data 
		else:
			return data
	
