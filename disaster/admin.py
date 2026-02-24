from django.contrib import admin
from .models import *

admin.site.register(State)
admin.site.register(Village)
admin.site.register(DisasterPrediction)
admin.site.register(Alert)
admin.site.register(VolunteerFeedback)
admin.site.register(ResourceRecommendation)
