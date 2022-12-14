from django.contrib import admin

from .models import Video, VideoPublishedProxy


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "slug",
        "state",
        "is_published",
        "publish_date",
        "description",
        "video_id",
    ]
    list_filter = ["active", "state"]
    search_fields = ["title"]
    readonly_fields = ["id", "is_published", "publish_date"]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(VideoPublishedProxy)
class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "publish_date", "description", "video_id"]
    search_fields = ["title"]
    readonly_fields = ["id", "is_published", "publish_date"]
    prepopulated_fields = {"slug": ["title"]}

    def get_queryset(self, request):
        return super().get_queryset(request).filter(active=True)
