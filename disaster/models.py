from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    population = models.IntegerField()

    def _str_(self):
        return f"{self.name} ({self.state.name})"


class DisasterPrediction(models.Model):
    DISASTER_TYPES = [
        ('Flood', 'Flood'),
        ('Heatwave', 'Heatwave'),
        ('Landslide', 'Landslide'),
    ]

    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    disaster_type = models.CharField(max_length=50, choices=DISASTER_TYPES)
    risk_score = models.FloatField()
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Alert(models.Model):
    CHANNELS = [
        ('SMS', 'SMS'),
        ('Voice', 'Voice'),
        ('CellBroadcast', 'CellBroadcast'),
    ]

    prediction = models.ForeignKey(DisasterPrediction, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    message = models.TextField()
    channel = models.CharField(max_length=50, choices=CHANNELS)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Sent")


class VolunteerFeedback(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    reporter_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    report = models.TextField()
    severity = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)


class ResourceRecommendation(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    disaster_type = models.CharField(max_length=50)
    evacuees_estimated = models.IntegerField()
    food_packets = models.IntegerField()
    water_litres = models.IntegerField()
    medical_teams = models.IntegerField()
    rescue_boats = models.IntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)
