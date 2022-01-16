from django_filters import CharFilter
import django_filters
from django import forms
from .models import Blog, Tag

class PostFilter(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr="icontains", label='title')
	tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Blog
		fields = ['title', 'tags']