from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
  changefreq = "weekly"
  priority = 0.8
  protocol = 'http'


  def items(self):
        return Blog.objects.all()

  def lastmod(self, obj):
        return obj.blog_date
        
  def location(self,obj):
        return '/blog/%s' % (obj.slug)
