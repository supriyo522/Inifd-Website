import requests
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from solo.models import SingletonModel
from .tasks import *
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class WebsiteSettings(SingletonModel):
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    top_header_popup = models.BooleanField(default=False)
    top_header_popup_text = models.TextField(blank=True, null=True)


TYPE_CHOICES = (
    ('interior', 'Interior Design'),
    ('fashion', 'Fashion Design'),
)


class AboutUs(SingletonModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = RichTextField(blank=True, null=True)


class MenuItems(MPTTModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    content = RichTextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '-' + str(self.code))
        super(MenuItems, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['code']


class MainBanners(models.Model):
    image = models.ImageField(upload_to='main_banners', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MainBanners, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=MainBanners)
# def compress_banner_image_task(instance, **kwargs):
#     compress_banner_image.delay(instance.id)


class SubBanners(models.Model):
    image = models.ImageField(upload_to='main_banners', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    page = models.OneToOneField('backend.Page', on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubBanners, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=SubBanners)
# def compress_sub_banner_image_task(instance, **kwargs):
#     compress_sub_banner_image.delay(instance.id)


class Course(models.Model):
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.course_type

    class Meta:
        unique_together = ('course_type', 'name')


class CareerOptions(models.Model):
    course_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title


class Admission(models.Model):
    course_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    program = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')), max_length=10)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='admission', blank=True, null=True)
    academic_1_name = models.CharField(max_length=100, blank=True, null=True)
    academic_1_year = models.CharField(max_length=100, blank=True, null=True)
    academic_1_percentage = models.CharField(max_length=100, blank=True, null=True)
    academic_1_board = models.CharField(max_length=100, blank=True, null=True)
    academic_1_subject = models.CharField(max_length=100, blank=True, null=True)
    academic_2_name = models.CharField(max_length=100, blank=True, null=True)
    academic_2_year = models.CharField(max_length=100, blank=True, null=True)
    academic_2_percentage = models.CharField(max_length=100, blank=True, null=True)
    academic_2_board = models.CharField(max_length=100, blank=True, null=True)
    academic_2_subject = models.CharField(max_length=100, blank=True, null=True)
    academic_3_name = models.CharField(max_length=100, blank=True, null=True)
    academic_3_year = models.CharField(max_length=100, blank=True, null=True)
    academic_3_percentage = models.CharField(max_length=100, blank=True, null=True)
    academic_3_board = models.CharField(max_length=100, blank=True, null=True)
    academic_3_subject = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


COURSE_TYPE_CHOICES = (
    ('interior', 'Interior Design'),
    ('fashion', 'Fashion Design'),
)


class Collaboration(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=COURSE_TYPE_CHOICES)
    image = models.ImageField(upload_to='collaboration', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Collaboration, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Placements(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='placement', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Placements, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=Placements)
# def compress_placement_image_task(instance, **kwargs):
#     compress_placement_image.delay(instance.id)


class InteriorExhibition(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='exhibition', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(InteriorExhibition, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=InteriorExhibition)
# def compress_interior_exhibition_image_task(instance, **kwargs):
#     compress_interior_exhibition_image.delay(instance.id)


class FashionShows(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='fashion_shows', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FashionShows, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='testimonials', blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Testimonials, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=Testimonials)
# def compress_testimonial_image_task(instance, **kwargs):
#     compress_testimonial_image.delay(instance.id)


class Mentors(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    categories = models.CharField(blank=True, null=True, max_length=1000)
    profile_image = models.ImageField(upload_to='mentors', blank=True, null=True)
    profile = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Mentors, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=Mentors)
# def compress_mentor_image_task(instance, **kwargs):
#     compress_mentor_profile_image.delay(instance.id)


class MediaCoverage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media_coverage', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MediaCoverage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=MediaCoverage)
# def compress_media_coverage_image_task(instance, **kwargs):
#     compress_media_coverage_image.delay(instance.id)


class Events(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.CharField(blank=True, null=True, max_length=1000)
    banner = models.ImageField(upload_to='events', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=100)
    content = RichTextField(blank=True, null=True)
    is_upcoming = models.BooleanField(default=False)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.date.timestamp()))
        super(Events, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=Events)
# def compress_events_image_task(instance, **kwargs):
#     compress_event_banner.delay(instance.id)


class InHouseMentor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='in_house_mentors', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    show_at_home = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=InHouseMentor)
# def compress_in_house_mentor_image_task(instance, **kwargs):
#     compress_inhouse_mentor_image.delay(instance.id)


class EventGallery(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='past_events', blank=True, null=True)


# @receiver(post_save, sender=EventGallery)
# def compress_event_gallery_image_task(instance, **kwargs):
#     compress_event_gallery_image.delay(instance.id)


class Awards(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='awards', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Awards, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=Awards)
# def compress_awards_image_task(instance, **kwargs):
#     compress_award_image.delay(instance.id)


class GlobalOpportunities(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to='global_opportunities', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(GlobalOpportunities, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=GlobalOpportunities)
# def compress_global_opportunities_image_task(instance, **kwargs):
#     compress_global_opportunity_banner.delay(instance.id)


class AcademicTours(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    banner = models.ImageField(upload_to='academic_tour', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(AcademicTours, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=AcademicTours)
# def compress_academic_tours_image_task(instance, **kwargs):
#     compress_academic_tour_banner.delay(instance.id)


class ImageGallery(models.Model):
    gallery_type_choices = (
        ('student', 'student'),
        ('general', 'general'),
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    galley_type = models.CharField(max_length=100, blank=True, null=True, choices=gallery_type_choices)
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    show_in_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ImageGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=ImageGallery)
# def compress_image_gallery_image_task(instance, **kwargs):
#     compress_imagegallery_image.delay(instance.id)


class VideoGallery(models.Model):
    gallery_type_choices = (
        ('student', 'student'),
        ('general', 'general'),
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    galley_type = models.CharField(max_length=100, blank=True, null=True, choices=gallery_type_choices)
    url = models.URLField(blank=True, null=True)
    show_in_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(VideoGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='partners', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Partners, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PlacementPartners(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='placement_partners', blank=True, null=True)
    show_at_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PlacementPartners, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=PlacementPartners)
# def compress_placement_partners_image_task(instance, **kwargs):
#     compress_placement_partner_image.delay(instance.id)


class EnquiryFormOTP(models.Model):
    mobile = models.CharField(max_length=10, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mobile + ' - ' + self.otp


class Enquiries(models.Model):
    course_choices = (
        ('Interior designer', 'Interior designer'),
        ('Fashion designer', 'Fashion designer'),
        ('Other', 'Other')
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True, choices=course_choices)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(blank=True, null=True, max_length=100)
    data = models.JSONField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(blank=True, null=True, max_length=100, default='Pending')
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Enquiries, dispatch_uid="enquiry_email")
def enquiries_signals(sender, created, instance, **kwargs):
    if created:
        try:
            response = requests.get(f'http://ip-api.com/json/{instance.ip_address}')
            instance.data = response.json()
            instance.save()
        except Exception as e:
            print(e)


class EnquiryStatus(models.Model):
    enquiry = models.ForeignKey(Enquiries, on_delete=models.CASCADE)
    status = models.CharField(blank=True, null=True, max_length=100, default='Pending')
    remarks = models.TextField(blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.enquiry.name


@receiver(post_save, sender=EnquiryStatus, dispatch_uid="enquiry_status")
def update_enquiry_status(sender, created, instance, **kwargs):
    if created:
        instance.enquiry.status = instance.status
        instance.enquiry.save()


class FashionDesignGallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='fashion_design_gallery', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FashionDesignGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=FashionDesignGallery, dispatch_uid="fashion_design_gallery")
# def compress_fashion_design_gallery_image_task(instance, **kwargs):
#     compress_fashion_design_gallery_image.delay(instance.id)


class InteriorDesignGallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='interior_design_gallery', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(InteriorDesignGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=InteriorDesignGallery, dispatch_uid="interior_design_gallery")
# def compress_interior_design_gallery_image_task(instance, **kwargs):
#     compress_interior_design_gallery_image.delay(instance.id)


class StudentWork(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='student_work', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(StudentWork, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=StudentWork, dispatch_uid="student_work")
# def compress_student_work_image_task(instance, **kwargs):
#     compress_student_work_image.delay(instance.id)


class Page(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=10000)
    content = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class PageGallery(models.Model):
        page = models.ForeignKey('backend.Page', on_delete=models.CASCADE)
        image = models.ImageField(upload_to='pages', blank=True, null=True)


class JuryMember(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    categories = models.CharField(blank=True, null=True, max_length=1000)
    profile_image = models.ImageField(upload_to='jury members', blank=True, null=True)
    profile = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class Blogpost(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    description = models.CharField(blank=True, null=True, max_length=10000)
    content = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blogpost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class HomepageSection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(HomepageSection, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
