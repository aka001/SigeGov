from haystack.forms import SearchForm

class PublicationsSearchForm(SearchForm):
	def no_query_found(self):
		return self.searchqueryset.all()
	
