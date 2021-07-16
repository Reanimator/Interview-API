from rest_framework import serializers

from .models import Interviews


class AdminAddInterviewsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    about = serializers.CharField()

    def create(self, validated_data):
        return Interviews.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.about = validated_data.get('about', instance.about)

        instance.save()
        return instance


class QuestionsSerializer(serializers.ModelSerializer):
    print('QuestionsSerializer')
