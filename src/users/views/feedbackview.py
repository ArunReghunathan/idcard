from src.common.libraries.customview import CustomModelViewSet
from src.common.libraries.loggingmixin import LoggingMixin
from src.users.models.feedbackmodel import Feedback
from src.users.serializer.feedbackserializer import FeedbackSerializer


class FeedbackView(LoggingMixin, CustomModelViewSet):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    model = Feedback