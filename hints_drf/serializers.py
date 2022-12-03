from rest_framework import serializers
from tests.models import Question


class TestSerializer(serializers.ModelSerializer):
    correct_answer = serializers.StringRelatedField(many=True)
    test = serializers.StringRelatedField(many=False)

    class Meta:
        model = Question
        fields = ('title', 'correct_answer', 'test')
