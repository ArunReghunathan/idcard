from rest_framework_mongoengine.serializers import DocumentSerializer

from src.users.models.feedbackmodel import Feedback


class FeedbackSerializer(DocumentSerializer):
    class Meta:
        model = Feedback
        depth = 4
        fields = '__all__'
