from rest_framework import serializers
from .models import Tag, Profile, Blog, Contact, Comments


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name',
                  'last_name', 'email',
                  'profile_pic', 'bio',
                  'resume']
        # first_name = serializers.CharField()
        # last_name = serializers.CharField()
        # email = serializers.EmailField()
        # profile_pic = serializers.ImageField()
        # bio = serializers.CharField()
        # resume = serializers.FileField()


class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class BlogSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(source='tags_set', many=True)

    class Meta:
        model = Blog
        fields = ['title', 'slug',
                  'sub_title', 'thumbnail', 'blog_date',
                  'body', 'featured', 'tags']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'name', 'subject', 'received_at', 'email', 'message'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id', 'name', 'date', 'blog', 'body'
        ]
