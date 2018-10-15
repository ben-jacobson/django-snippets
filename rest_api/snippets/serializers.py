from rest_framework import serializers
from snippets.models import Snippet#, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

# Serializers are similar to forms in that they can mirror model attributes with one line of code. In the example below, we've been more verbose because we need to customize this a bit

# if you want to model a Serializer on a model, use serailizers.ModelSerializer as seen above. Below is the long-hand way of doing this. 

'''class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})  # this is controlling how this field needs to be rendered when outputting HTML. This is similar to using Django Forms widget=widgets.Textarea
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # if you call serializer.save() if will run the create or update method. we overwrite them below.

    # Serailizers don't just serialize, they de-serialize too!
    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    # Another reason why Serializers are similar to Forms, are that you can validate data with them, in almost exactly the same way
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data. 
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''