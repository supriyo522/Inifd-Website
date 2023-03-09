from django import forms
from django.forms import ModelForm
from mptt.forms import TreeNodeChoiceField

from .models import Awards, Enquiries, GlobalOpportunities, WebsiteSettings, AboutUs, MenuItems, MainBanners, \
    SubBanners, Mentors, MediaCoverage, \
    Events, StudentWork, AcademicTours, ImageGallery, VideoGallery, Testimonials, Placements, PlacementPartners, Page, \
    Partners, JuryMember, Blogpost, HomepageSection, Collaboration, InteriorExhibition, FashionShows, InHouseMentor, \
    Course, CareerOptions, Admission


class CourseEnquiryForm(ModelForm):
    class Meta:
        model = Enquiries
        fields = ['name', 'email', 'phone', 'course', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'txt', 'placeholder': 'Enter your name', 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'class': 'txt', 'placeholder': 'Enter your email', 'required': 'required'}),
            'phone': forms.TextInput(
                attrs={'class': 'txt', 'placeholder': 'Enter your phone', 'required': 'required'}),
            'course': forms.Select(
                attrs={'class': 'list', 'placeholder': 'Enter your course', 'required': 'required',
                       'default': 'Select Course'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': "5", 'placeholder': 'Enter your message',
                                             'required': 'required'}),
        }


class WebsiteSettingsForm(ModelForm):
    class Meta:
        model = WebsiteSettings
        fields = '__all__'

        widgets = {
            'logo': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Logo',
                       'onchange': "showPreview(event)"}),
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Website title', }),
            'address': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Address', }),
            'contact': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Contact no', }),
            'email': forms.EmailInput(
                attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email', }),
            'latitude': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Latitude', }),
            'longitude': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Longitude', }),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', }),
            'keywords': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Website keywords', }),
            'facebook': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Facebook account link', }),
            'twitter': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Twitter account link', }),
            'instagram': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Instagram account link', }),
            'youtube': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Youtube account link', }),
            'whatsapp': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Whatsapp number', }),
            'top_header_popup': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'class': 'form-check-input', 'placeholder': 'Is ', }),
            'top_header_popup_text': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Top header text', }),
        }


class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'


class MenuItemAddForm(ModelForm):
    parent = TreeNodeChoiceField(queryset=MenuItems.objects.all(), required=False)

    class Meta:
        model = MenuItems
        fields = ('title', 'parent', 'code', 'is_active', 'content',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'code': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Code', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class MainBannerAddForm(ModelForm):
    class Meta:
        model = MainBanners
        fields = ('title', 'image', 'is_active', 'link',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'link': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Link', }),
        }


class MainBannerUpdateForm(ModelForm):
    class Meta:
        model = MainBanners
        fields = ('title', 'image', 'is_active', 'link',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image',
                       'onchange': "showPreview(event)"}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'link': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Link', }),
        }


class SubBannerAddForm(ModelForm):
    class Meta:
        model = SubBanners
        fields = ('title', 'image', 'description', 'is_active', 'page',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'page': forms.Select(
                attrs={'type': 'list', 'class': 'form-control', 'placeholder': 'Link', 'required': 'required'}),

        }


class SubBannerUpdateForm(ModelForm):
    class Meta:
        model = SubBanners
        fields = ('title', 'image', 'description', 'is_active', 'page',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'page': forms.Select(
                attrs={'type': 'list', 'class': 'form-control', 'placeholder': 'Link', 'required': 'required'}),

        }


class MentorAddForm(ModelForm):
    class Meta:
        model = Mentors
        fields = ('name', 'categories', 'profile_image', 'profile', 'is_active',)

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'categories': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Categories', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Profile Image', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'profile': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Profile', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class MentorUpdateForm(ModelForm):
    class Meta:
        model = Mentors
        fields = ('name', 'categories', 'profile_image', 'profile', 'is_active',)

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'categories': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Categories', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Profile Image',
                       'onchange': "showPreview(event)"}),
            'profile': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Profile', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class MediaCoverageAddForm(ModelForm):
    class Meta:
        model = MediaCoverage
        fields = ('title', 'image', 'description', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class MediaCoverageUpdateForm(ModelForm):
    class Meta:
        model = MediaCoverage
        fields = ('title', 'image', 'description', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Image',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class EventAddForm(ModelForm):
    class Meta:
        model = Events
        fields = (
            'title', 'banner', 'description', 'course_type', 'date', 'location', 'content', 'show_at_home',
            'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'list', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Date',
                       'required': 'required'}),
            'location': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Location', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class EventUpdateForm(ModelForm):
    class Meta:
        model = Events
        fields = (
            'title', 'banner', 'description', 'course_type', 'date', 'location', 'content', 'show_at_home',
            'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'list', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),

            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Date',
                       }),
            'location': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Location', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class StudentWorkAddForm(ModelForm):
    class Meta:
        model = StudentWork
        fields = ('title', 'image', 'description', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class StudentWorkUpdateForm(ModelForm):
    class Meta:
        model = StudentWork
        fields = ('title', 'image', 'description', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class AcademicTourAddForm(ModelForm):
    class Meta:
        model = AcademicTours
        fields = ('title', 'banner', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class AcademicTourUpdateForm(ModelForm):
    class Meta:
        model = AcademicTours
        fields = ('title', 'banner', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show At Home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class ImageGalleryAddForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('galley_type', 'title', 'description', 'image', 'show_in_home', 'is_active',)

        widgets = {
            'galley_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'show_in_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class ImageGalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('galley_type', 'title', 'description', 'image', 'show_in_home', 'is_active',)

        widgets = {
            'galley_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'show_in_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class VideoAddForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ('title', 'description', 'galley_type', 'url', 'show_in_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'galley_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'url': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Video Url', 'required': 'required'}),
            'show_in_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class VideoUpdateForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ('title', 'description', 'galley_type', 'url', 'show_in_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'galley_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'url': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Video Url', 'required': 'required'}),
            'show_in_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class TestimonialAddForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('title', 'description', 'image', 'year', 'course_type', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'year': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Year', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-select', 'placeholder': 'Course Type', 'required': 'required'}),

            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class TestimonialUpdateForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('title', 'description', 'image', 'year', 'course_type', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'year': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Year', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-select', 'placeholder': 'Course Type', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PlacementAddForm(forms.ModelForm):
    class Meta:
        model = Placements
        fields = ('title', 'description', 'image', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PlacementUpdateForm(forms.ModelForm):
    class Meta:
        model = Placements
        fields = ('title', 'description', 'image', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PlacementPartnerAddForm(forms.ModelForm):
    class Meta:
        model = PlacementPartners
        fields = ('title', 'image', 'show_at_home', 'course_type', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PlacementPartnerUpdateForm(forms.ModelForm):
    class Meta:
        model = PlacementPartners
        fields = ('title', 'image', 'course_type', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class AwardAddForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = ('title', 'description', 'image', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class AwardUpdateForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = ('title', 'description', 'image', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class GlobalOpportunityAddForm(forms.ModelForm):
    class Meta:
        model = GlobalOpportunities
        fields = ('title', 'description', 'banner', 'content', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class GlobalOpportunityUpdateForm(forms.ModelForm):
    class Meta:
        model = GlobalOpportunities
        fields = ('title', 'description', 'banner', 'content', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'banner': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PageAddForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'description', 'content', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PageUpdateForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'description', 'content', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PartnerAddForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ('title', 'image', 'course_type', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class PartnerUpdateForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ('title', 'image', 'course_type', 'show_at_home', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)"}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class JuryMemberAddForm(ModelForm):
    class Meta:
        model = JuryMember
        fields = ('name', 'categories', 'profile_image', 'profile', 'is_active',)

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'categories': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Categories', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Profile Image', 'required': 'required',
                       'onchange': "showPreview(event)"}),
            'profile': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Profile', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class JuryMemberUpdateForm(ModelForm):
    class Meta:
        model = JuryMember
        fields = ('name', 'categories', 'profile_image', 'profile', 'is_active',)

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'categories': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Categories', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Profile Image',
                       'onchange': "showPreview(event)"}),
            'profile': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Profile', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ('title', 'course_type', 'description', 'content', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'content': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Content', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class HomepageSectionUpdateForm(forms.ModelForm):
    class Meta:
        model = HomepageSection
        fields = ('title', 'is_active',)

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'readonly': 'readonly'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = ('title', 'image', 'is_active', 'show_at_home', 'course_type')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),

        }


class CollaborationUpdateForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = ('title', 'image', 'is_active', 'show_at_home', 'course_type')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", }),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),

        }


class InteriorExhibitionForm(forms.ModelForm):
    class Meta:
        model = InteriorExhibition
        fields = ('title', 'image', 'is_active', 'show_at_home')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),

        }


class InteriorExhibitionUpdateForm(forms.ModelForm):
    class Meta:
        model = InteriorExhibition
        fields = ('title', 'image', 'is_active', 'show_at_home')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", }),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
        }


class FashionShowForm(forms.ModelForm):
    class Meta:
        model = FashionShows
        fields = ('title', 'image', 'is_active', 'show_at_home')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
        }


class FashionShowUpdateForm(forms.ModelForm):
    class Meta:
        model = FashionShows
        fields = ('title', 'image', 'is_active', 'show_at_home')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", }),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
        }


class InHouseMentorForm(forms.ModelForm):
    class Meta:
        model = InHouseMentor
        fields = ('name', 'profile_image', 'category', 'is_active', 'show_at_home')

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", 'required': 'required'}),
            'category': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Category'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
        }


class InHouseMentorUpdateForm(forms.ModelForm):
    class Meta:
        model = InHouseMentor
        fields = ('name', 'profile_image', 'category', 'is_active', 'show_at_home')

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'profile_image': forms.FileInput(
                attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Banner',
                       'onchange': "showPreview(event)", }),
            'category': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Category'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
            'show_at_home': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Show in home'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'course_type', 'description', 'is_active')

        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'description': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),

            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class CareerOptionForm(forms.ModelForm):
    class Meta:
        model = CareerOptions
        fields = ('title', 'description', 'is_active', 'course_type')

        widgets = {
            'title': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Title', 'required': 'required'}),
            'description': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Description', 'required': 'required'}),
            'course_type': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Course Type', 'required': 'required'}),
            'is_active': forms.CheckboxInput(
                attrs={'type': 'checkbox', 'placeholder': 'Is Active'}),
        }


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('course_type', 'program', 'session', 'name', 'date_of_birth', 'gender', 'guardian_name'
                  , 'address', 'email', 'phone', 'pin_code', 'image', 'academic_1_name', 'academic_1_year',
                  'academic_1_percentage'
                  , 'academic_1_board', 'academic_1_subject', 'academic_2_name', 'academic_2_year',
                  'academic_2_percentage'
                  , 'academic_2_board', 'academic_2_subject', 'academic_3_name', 'academic_3_year',
                  'academic_3_percentage'
                  , 'academic_3_board', 'academic_3_subject')
