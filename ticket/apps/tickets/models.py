from django.contrib.auth import get_user_model
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import ImageField
from django.db.models import IntegerField
from django.db.models import TextChoices

from ticket.apps.core.models import TimeStampedModel

User = get_user_model()


class Ticket(TimeStampedModel):
    class Status(TextChoices):
        INCOMPLETE = "incomplete", "Incomplete"
        COMPLETE = "complete", "Complete"

    user = ForeignKey(User, on_delete=CASCADE)
    images = IntegerField()
    status = CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.INCOMPLETE,
    )

    def __str__(self):
        return f"{self.images} - {self.status}"

    @property
    def images_count(self):
        return self.all_images.count()


class Image(TimeStampedModel):
    ticket = ForeignKey(Ticket, related_name="all_images", on_delete=CASCADE)
    image = ImageField(upload_to="images/")

    def __str__(self):
        return f"Image {self.pk} - Ticket {self.ticket_id}"
