from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from hints_drf.serializers import TestSerializer
from tests.models import Question, Test


class TestViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = TestSerializer
    http_method_names = ['get']

    @action(methods=['get'], detail=True)
    def test(self, request, pk=None):
        tests = Test.objects.get(pk=pk)
        question = Question.objects.filter(test_id=pk)
        return Response({'test': tests.title, 'question': [q.title for q in question]})
