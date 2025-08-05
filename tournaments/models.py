from django.db import models

# Create your models here.
class Tournament(models.Model):
    SPORT_CHOICES = [
        ('Cricket', 'Cricket'), ('Football', 'Football'), ('Badminton', 'Badminton'),
        ('Running', 'Running'), ('Gym', 'Gym'), ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'), ('Kabaddi', 'Kabaddi'), ('Yoga', 'Yoga'),
        ('Basketball', 'Basketball'), ('Chess', 'Chess'), ('Table Tennis', 'Table Tennis'),
    ]
    LEVEL_CHOICES = [
        ('Corporate', 'Corporate'), ('School', 'School'), ('College/University', 'College/University'),
        ('Club/Academy', 'Club/Academy'), ('District', 'District'), ('State', 'State'),
        ('Zonal/Regional', 'Zonal/Regional'), ('National', 'National'), ('International', 'International'),
    ]
    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=50, choices=SPORT_CHOICES)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    official_url = models.URLField()
    streaming_links = models.URLField(blank=True, null=True)
    tournament_image = models.URLField(blank=True, null=True)
    summary = models.TextField(max_length=300)

    def __str__(self):
        return self.name