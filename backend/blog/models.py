from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=False)
    last_name = models.CharField(max_length=200, blank=True, null=False)
    email = models.EmailField(max_length=255, unique=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/%Y%m%d/", default='/avatar.png')
    bio = models.TextField(null=True, blank=True)
    resume = models.FileField(null=True, blank=True,
                              upload_to='resume/%Y/%m/%d/')

    def __str__(self):
        name = str(self.first_name + ' ' + self.last_name)
        return name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    sub_title = models.TextField(null=False)
    thumbnail = models.ImageField(null=False,
                                  upload_to="blog/%Y/%m/%d/")
    blog_date = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['blog_date']


class Comments(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blog


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=400)
    received_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
