from rest_framework import serializers

from ticket.apps.tickets.models import Image
from ticket.apps.tickets.models import Ticket

from ..tasks import upload_image_to_cloudinary


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("images",)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)

    def create(self, validated_data):
        image = super().create(validated_data)
        image_path = image.image.path

        res = upload_image_to_cloudinary.delay(image_path)

        image_url = res.get()
        if image_url:
            image.image = image_url
            image.save()
        else:
            raise Exception("Error al subir la imagen a Cloudinary")
        return image
