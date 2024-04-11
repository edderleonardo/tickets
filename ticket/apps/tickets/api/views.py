from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ticket.apps.tickets.models import Image
from ticket.apps.tickets.models import Ticket

from .serializers import ImageSerializer
from .serializers import TicketSerializer


class TicketCreateAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(ticket=self.request.user.ticket_set.first())

    def create(self, request, *args, **kwargs):
        ticket = request.user.ticket_set.first()
        ticket_total_images = ticket.images
        ticket_images_count = ticket.all_images.count()
        if ticket_images_count >= ticket_total_images:
            ticket.status = Ticket.Status.COMPLETE
            ticket.save()
            return Response(
                {"message": "Ticket already has the maximum number of images"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)
