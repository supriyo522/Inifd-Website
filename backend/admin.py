from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *

admin.site.title = 'Inifd'
admin.site.site_header = 'Inifd'
admin.site.site_title = 'Inifd admin panel'

# Register your models here.
admin.site.register(WebsiteSettings)
admin.site.register(AboutUs)

admin.site.register(
    MenuItems,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(MainBanners)
admin.site.register(SubBanners)
admin.site.register(Page)
admin.site.register(Course)
admin.site.register(Placements)
admin.site.register(Testimonials)
admin.site.register(Mentors)
admin.site.register(JuryMember)
admin.site.register(MediaCoverage)


class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    extra = 1


class EventsAdmin(admin.ModelAdmin):
    inlines = [EventGalleryInline]


admin.site.register(Events, EventsAdmin)
admin.site.register(StudentWork)
admin.site.register(Awards)
admin.site.register(GlobalOpportunities)
admin.site.register(ImageGallery)
admin.site.register(AcademicTours)
admin.site.register(PlacementPartners)
admin.site.register(FashionDesignGallery)
admin.site.register(InteriorDesignGallery)
admin.site.register(EnquiryStatus)


class CourseInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'message', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['name', 'email', 'phone', 'course', 'message']


admin.site.register(Enquiries, CourseInquiryAdmin)


class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_active']
    list_filter = ['created_at']
    search_fields = ['title', 'created_at']


admin.site.register(Blogpost, BlogpostAdmin)


class HomepageSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    search_fields = ['title']


admin.site.register(HomepageSection, HomepageSectionAdmin)


class InteriorExhibitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    search_fields = ['title']


admin.site.register(InteriorExhibition, InteriorExhibitionAdmin)


class FashionShowsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    search_fields = ['title']


admin.site.register(FashionShows, FashionShowsAdmin)


class CollaborationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    search_fields = ['title']


admin.site.register(Collaboration, CollaborationsAdmin)

admin.site.register(CareerOptions)
admin.site.register(Admission)
