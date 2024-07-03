from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id =  serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "category", "snippet", "status", "relative_url", "absolute_url", "created_date", "published_date"]
        read_only_fields = ["author"]
    
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    # a function to set how i want my jason to be shown
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        # checks if we are in list page or in detail view page
        if request.parser_context.get('kwargs').get('pk'):
            # if it is detail page, it pops and deletes some data that there is no need to show them in detail page
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            # if it is in list page, it deletes some data that there is no need to be shown in listing page
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep
    
    # override the default create method
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']