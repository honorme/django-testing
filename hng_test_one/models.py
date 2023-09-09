from django.db import models

class TestOne(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.DateField()
    utc_time = models.TimeField()
    track = models.CharField(max_length=100)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.IntegerField() 
