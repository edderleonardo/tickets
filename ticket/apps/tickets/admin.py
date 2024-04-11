from django.contrib import admin

from ticket.apps.tickets.models import Image
from ticket.apps.tickets.models import Ticket

admin.site.register(Ticket)
admin.site.register(Image)
