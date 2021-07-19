from collections import OrderedDict

from rest_framework import serializers

from .models import Interviews
from .models import Questions
from .models import AnonInterviews


class AdminInterviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interviews
        fields = ['id', 'name', 'start_date', 'end_date', 'about']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.about = validated_data.get('about', instance.about)

        instance.save()
        return instance


class QuestionsTypeSerializer(serializers.Serializer):

    question_type = serializers.CharField()


class QuestionsFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class QuestionsTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = [
            'id',
            'interview',
            'question',
            'question_type',
            'text_answer']


class QuestionsVarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = [
            'id',
            'interview',
            'question',
            'question_type',
            'var_answer_1',
            'var_answer_2',
            'var_answer_3',
            'var_answer_4',
            'var_answer_correct']


class QuestionsMvarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = [
            'id',
            'interview',
            'question',
            'question_type',
            'var_answer_1',
            'var_answer_2',
            'var_answer_3',
            'var_answer_4',
            'mvar_answer_correct']


class AnonInterviewsAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonInterviews
        fields = '__all__'
