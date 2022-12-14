from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class PublishStateOptions(models.TextChoices):
    PUBLISH = "PU", "Publish"
    DRAFT = "DR", "Draft"


class VideoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=Video.VideoStateOptions.PUBLISH)


# Create your models here.
class Video(models.Model):
    VideoStateOptions = PublishStateOptions

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    state = models.CharField(
        max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT
    )
    publish_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs) -> None:
        if self.slug is None:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"

    objects = models.Manager()
    published = VideoManager()
