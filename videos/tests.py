import pytest
from django.utils import timezone
from django.utils.text import slugify

from .models import PublishStateOptions, Video


@pytest.fixture
@pytest.mark.django_db
def video():
    return Video.objects.create(title="test title")


@pytest.mark.django_db
def test_video_model(video):
    inserted_video = Video.objects.first()
    assert inserted_video.title == "test title"
    assert inserted_video.state == PublishStateOptions.DRAFT


@pytest.mark.django_db
def test_slug_field(video):
    inserted_video = Video.objects.first()
    assert inserted_video.slug == slugify(inserted_video.title)


@pytest.mark.django_db
def test_change_state_to_publish(video):
    video.state = PublishStateOptions.PUBLISH
    video.save()
    assert video.publish_date.strftime("%Y/%m/%d-%H:%M:%S") == timezone.now().strftime(
        "%Y/%m/%d-%H:%M:%S"
    )
