from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import allowedUsers
# Create your views here.
from .forms import AwardAddForm, AwardUpdateForm, GlobalOpportunityAddForm, GlobalOpportunityUpdateForm, \
    WebsiteSettingsForm, AboutUsForm, MenuItemAddForm, MainBannerAddForm, MainBannerUpdateForm, \
    SubBannerAddForm, SubBannerUpdateForm, MentorAddForm, MentorUpdateForm, MediaCoverageAddForm, \
    MediaCoverageUpdateForm, EventAddForm, EventUpdateForm, StudentWorkAddForm, StudentWorkUpdateForm, \
    AcademicTourAddForm, AcademicTourUpdateForm, ImageGalleryAddForm, ImageGalleryUpdateForm, VideoAddForm, \
    VideoUpdateForm, TestimonialAddForm, TestimonialUpdateForm, PlacementAddForm, PlacementUpdateForm, \
    PlacementPartnerUpdateForm, PlacementPartnerAddForm, PageAddForm, PageUpdateForm, PartnerAddForm, PartnerUpdateForm, \
    JuryMemberAddForm, JuryMemberUpdateForm, BlogpostForm, HomepageSectionUpdateForm, \
    CollaborationForm, CollaborationUpdateForm, InteriorExhibitionForm, InteriorExhibitionUpdateForm, FashionShowForm, \
    FashionShowUpdateForm, InHouseMentorForm, InHouseMentorUpdateForm, CourseForm, CareerOptionForm
from .models import Awards, Enquiries, EnquiryStatus, GlobalOpportunities, WebsiteSettings, AboutUs, MenuItems, \
    MainBanners, SubBanners, Mentors, \
    MediaCoverage, Events, StudentWork, AcademicTours, ImageGallery, VideoGallery, Testimonials, Placements, \
    PlacementPartners, Page, Partners, JuryMember, Blogpost, HomepageSection, Collaboration, InteriorExhibition, \
    FashionShows, InHouseMentor, Course, CareerOptions


def backend_login(request):
    if request.user.is_authenticated:
        return redirect('backend_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('backend_dashboard')
            else:
                messages.error(request, 'Your account is not active or not staff or superuser')
        else:
            messages.error(request, 'Invalid login details supplied')
    return render(request, 'backend/login.html')


@login_required(login_url='backend_login/')
def backend_logout(request):
    logout(request)
    return redirect('backend_login')


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'counselor', 'marketing'])
def backend_dashboard(request):
    total_enquiries = Enquiries.objects.all().count()
    recent_enquiries = Enquiries.objects.all().order_by('-id')[:10]
    context = {'total_enquiries': total_enquiries, 'recent_enquiries': recent_enquiries}
    return render(request, 'backend/dashboard.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'marketing'])
def backend_website_settings(request):
    w_settings = WebsiteSettings.objects.get(id=1)
    form = WebsiteSettingsForm(instance=w_settings)
    if request.method == 'POST':
        form = WebsiteSettingsForm(request.POST, request.FILES or None, instance=w_settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Website settings updated successfully')
            return redirect('backend_website_settings')

    context = {'form': form}
    return render(request, 'backend/website_settings/website_settings.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_about_us(request):
    about_us = AboutUs.objects.first()
    form = AboutUsForm(instance=about_us)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Us updated successfully')
            return redirect('backend_about_us')
    context = {'form': form}
    return render(request, 'backend/website_settings/about_us.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_menu_items(request):
    menu_items = MenuItems.objects.all().order_by('-id')
    context = {'menu_items': menu_items}
    return render(request, 'backend/menu_items/menu_items.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_menu_item(request):
    form = MenuItemAddForm
    if request.method == 'POST':
        form = MenuItemAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            messages.success(request, 'Menu Item added successfully')
            return redirect('backend_menu_items')
        else:
            print(form.errors)
            messages.error(request, 'Menu Item not added')
    context = {'form': form}
    return render(request, 'backend/menu_items/add_menu_item.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'counselor'])
def backend_leads_enquiry(request):
    enquiries = Enquiries.objects.all().order_by('-id')
    context = {'enquiries': enquiries}
    return render(request, 'backend/leads/leads_enquiry.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'counselor'])
def backend_leads_enquiry_details(request, enquiry_id):
    enquiry = Enquiries.objects.get(id=enquiry_id)
    context = {'enquiry': enquiry}
    return render(request, 'backend/leads/leads_enquiry_details.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'counselor'])
def backend_leads_enquiry_update(request, enquiry_id):
    enquiry = Enquiries.objects.get(id=enquiry_id)
    if request.method == "POST":
        status = request.POST['status']
        remark = request.POST['remark']
        print(status, remark)
        new_status = EnquiryStatus.objects.create(status=status, remarks=remark,
                                                  updated_by=request.user, enquiry=enquiry)
        new_status.save()
        messages.success(request, f'Enquiry #{enquiry.id} status updated successfully')
        return redirect('backend_leads_enquiry')
    context = {'enquiry': enquiry}
    return render(request, 'backend/leads/update_enquiry.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_main_banners(request):
    main_banners = MainBanners.objects.all().order_by('-id')
    context = {'main_banners': main_banners}
    return render(request, 'backend/main_banner/main_banners.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_main_banner(request):
    form = MainBannerAddForm
    if request.method == 'POST':
        form = MainBannerAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_banner = form.save(commit=False)
            new_banner.created_by = request.user
            new_banner.save()
            messages.success(request, 'Main Banner added successfully')
            return redirect('backend_main_banners')
        else:
            print(form.errors)
            messages.error(request, 'Main Banner not added')
    context = {'form': form}
    return render(request, 'backend/main_banner/add_main_banner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_main_banner(request, banner_id):
    banner = MainBanners.objects.get(id=banner_id)
    form = MainBannerUpdateForm(instance=banner)
    if request.method == 'POST':
        form = MainBannerUpdateForm(request.POST, request.FILES or None, instance=banner)
        if form.is_valid():
            new_banner = form.save(commit=False)
            new_banner.created_by = request.user
            new_banner.save()
            messages.success(request, 'Main Banner updated successfully')
            return redirect('backend_main_banners')
        else:
            print(form.errors)
            messages.error(request, 'Main Banner not updated')
    context = {'form': form, 'banner': banner}
    return render(request, 'backend/main_banner/update_main_banner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_sub_banners(request):
    sub_banners = SubBanners.objects.all().order_by('-id')
    context = {'sub_banners': sub_banners}
    return render(request, 'backend/sub_banner/sub_banners.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_sub_banner(request):
    form = SubBannerAddForm
    if request.method == 'POST':
        form = SubBannerAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_banner = form.save(commit=False)
            new_banner.created_by = request.user
            new_banner.save()
            messages.success(request, 'Sub Banner added successfully')
            return redirect('backend_sub_banners')
        else:
            print(form.errors)
            messages.error(request, f'Sub Banner not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/sub_banner/add_sub_banner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_sub_banner(request, banner_id):
    banner = SubBanners.objects.get(id=banner_id)
    form = SubBannerUpdateForm(instance=banner)
    if request.method == 'POST':
        form = SubBannerUpdateForm(request.POST, request.FILES or None, instance=banner)
        if form.is_valid():
            new_banner = form.save(commit=False)
            new_banner.created_by = request.user
            new_banner.save()
            messages.success(request, 'Sub Banner updated successfully')
            return redirect('backend_sub_banners')
        else:
            print(form.errors)
            messages.error(request, f'Sub Banner not updated, {form.errors}')
    context = {'form': form, 'banner': banner}
    return render(request, 'backend/sub_banner/update_sub_banner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_mentors(request):
    mentors = Mentors.objects.all().order_by('-id')
    context = {'mentors': mentors}
    return render(request, 'backend/mentor/mentors.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_mentor(request):
    form = MentorAddForm
    if request.method == 'POST':
        form = MentorAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_mentor = form.save(commit=False)
            new_mentor.created_by = request.user
            new_mentor.save()
            messages.success(request, 'Mentor added successfully')
            return redirect('backend_mentors')
        else:
            print(form.errors)
            messages.error(request, f'Mentor not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/mentor/add_mentor.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_mentor(request, mentor_id):
    mentor = Mentors.objects.get(id=mentor_id)
    form = MentorUpdateForm(instance=mentor)
    if request.method == 'POST':
        form = MentorUpdateForm(request.POST, request.FILES or None, instance=mentor)
        if form.is_valid():
            new_mentor = form.save(commit=False)
            new_mentor.created_by = request.user
            new_mentor.save()
            messages.success(request, 'Mentor updated successfully')
            return redirect('backend_mentors')
        else:
            print(form.errors)
            messages.error(request, f'Mentor not updated, {form.errors}')
    context = {'form': form, 'mentor': mentor}
    return render(request, 'backend/mentor/update_mentor.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_media_coverages(request):
    media_coverages = MediaCoverage.objects.all().order_by('-id')
    context = {'media_coverages': media_coverages}
    return render(request, 'backend/media_coverage/media_coverages.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_media_coverage(request):
    form = MediaCoverageAddForm
    if request.method == 'POST':
        form = MediaCoverageAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_media_coverage = form.save(commit=False)
            new_media_coverage.created_by = request.user
            new_media_coverage.save()
            messages.success(request, 'Media Coverage added successfully')
            return redirect('backend_media_coverages')
        else:
            print(form.errors)
            messages.error(request, f'Media Coverage not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/media_coverage/add_media_coverage.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_media_coverage(request, media_coverage_id):
    media_coverage = MediaCoverage.objects.get(id=media_coverage_id)
    form = MediaCoverageUpdateForm(instance=media_coverage)
    if request.method == 'POST':
        form = MediaCoverageUpdateForm(request.POST, request.FILES or None, instance=media_coverage)
        if form.is_valid():
            new_media_coverage = form.save(commit=False)
            new_media_coverage.created_by = request.user
            new_media_coverage.save()
            messages.success(request, 'Media Coverage updated successfully')
            return redirect('backend_media_coverages')
        else:
            print(form.errors)
            messages.error(request, f'Media Coverage not updated, {form.errors}')
    context = {'form': form, 'media_coverage': media_coverage}
    return render(request, 'backend/media_coverage/update_media_coverage.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_events(request):
    events = Events.objects.all().order_by('-id')
    context = {'events': events}
    return render(request, 'backend/event/events.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_past_events(request):
    events = Events.objects.filter(date__lte=datetime.now())
    context = {'events': events}
    return render(request, 'backend/event/past_events.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_upcoming_events(request):
    events = Events.objects.filter(date__gte=datetime.now())
    context = {'events': events}
    return render(request, 'backend/event/upcoming_events.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_view_event(request, event_id):
    event = Events.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'backend/event/view_event.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_event(request):
    form = EventAddForm
    if request.method == 'POST':
        form = EventAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.created_by = request.user
            new_event.save()
            messages.success(request, 'Event added successfully')
            return redirect('backend_events')
        else:
            print(form.errors)
            messages.error(request, f'Event not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/event/add_event.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_event(request, event_id):
    event = Events.objects.get(id=event_id)
    form = EventUpdateForm(instance=event)
    if request.method == 'POST':
        form = EventUpdateForm(request.POST, request.FILES or None, instance=event)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.created_by = request.user
            new_event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('backend_events')
        else:
            print(form.errors)
            messages.error(request, f'Event not updated, {form.errors}')
    context = {'form': form, 'event': event}
    return render(request, 'backend/event/update_event.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_student_works(request):
    student_works = StudentWork.objects.all().order_by('-id')
    context = {'student_works': student_works}
    return render(request, 'backend/student_work/student_works.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_student_work(request):
    form = StudentWorkAddForm
    if request.method == 'POST':
        form = StudentWorkAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_student_work = form.save(commit=False)
            new_student_work.created_by = request.user
            new_student_work.save()
            messages.success(request, 'Student Work added successfully')
            return redirect('backend_student_works')
        else:
            print(form.errors)
            messages.error(request, f'Student Work not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/student_work/add_student_work.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_student_work(request, student_work_id):
    student_work = StudentWork.objects.get(id=student_work_id)
    form = StudentWorkUpdateForm(instance=student_work)
    if request.method == 'POST':
        form = StudentWorkUpdateForm(request.POST, request.FILES or None, instance=student_work)
        if form.is_valid():
            new_student_work = form.save(commit=False)
            new_student_work.created_by = request.user
            new_student_work.save()
            messages.success(request, 'Student Work updated successfully')
            return redirect('backend_student_works')
        else:
            print(form.errors)
            messages.error(request, f'Student Work not updated, {form.errors}')
    context = {'form': form, 'student_work': student_work}
    return render(request, 'backend/student_work/update_student_work.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_academic_tours(request):
    academic_tours = AcademicTours.objects.all().order_by('-id')
    context = {'academic_tours': academic_tours}
    return render(request, 'backend/academic_tour/academic_tours.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_academic_tour(request):
    form = AcademicTourAddForm
    if request.method == 'POST':
        form = AcademicTourAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_academic_tour = form.save(commit=False)
            new_academic_tour.created_by = request.user
            new_academic_tour.save()
            messages.success(request, 'Academic Tour added successfully')
            return redirect('backend_academic_tours')
        else:
            print(form.errors)
            messages.error(request, f'Academic Tour not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/academic_tour/add_academic_tour.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_academic_tour(request, academic_tour_id):
    academic_tour = AcademicTours.objects.get(id=academic_tour_id)
    form = AcademicTourUpdateForm(instance=academic_tour)
    if request.method == 'POST':
        form = AcademicTourUpdateForm(request.POST, request.FILES or None, instance=academic_tour)
        if form.is_valid():
            new_academic_tour = form.save(commit=False)
            new_academic_tour.created_by = request.user
            new_academic_tour.save()
            messages.success(request, 'Academic Tour updated successfully')
            return redirect('backend_academic_tours')
        else:
            print(form.errors)
            messages.error(request, f'Academic Tour not updated, {form.errors}')
    context = {'form': form, 'academic_tour': academic_tour}
    return render(request, 'backend/academic_tour/update_academic_tour.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_image_gallery(request):
    images = ImageGallery.objects.all().order_by('-id')
    context = {'images': images}
    return render(request, 'backend/gallery/image_gallery/image_galery.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_image_gallery(request):
    form = ImageGalleryAddForm
    if request.method == 'POST':
        form = ImageGalleryAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.created_by = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            return redirect('backend_image_gallery')
        else:
            print(form.errors)
            messages.error(request, f'Image not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/gallery/image_gallery/add_image_gallery.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_image_gallery(request, image_id):
    image = ImageGallery.objects.get(id=image_id)
    form = ImageGalleryUpdateForm(instance=image)
    if request.method == 'POST':
        form = ImageGalleryUpdateForm(request.POST, request.FILES or None, instance=image)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.created_by = request.user
            new_image.save()
            messages.success(request, 'Image updated successfully')
            return redirect('backend_image_gallery')
        else:
            print(form.errors)
            messages.error(request, f'Image not updated, {form.errors}')
    context = {'form': form, 'image': image}
    return render(request, 'backend/gallery/image_gallery/update_image_gallery.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_video_gallery(request):
    videos = VideoGallery.objects.all().order_by('-id')
    context = {'videos': videos}
    return render(request, 'backend/gallery/video_gallery/video_gallery.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_video_gallery(request):
    form = VideoAddForm
    if request.method == 'POST':
        form = VideoAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.created_by = request.user
            new_video.save()
            messages.success(request, 'Video added successfully')
            return redirect('backend_video_gallery')
        else:
            print(form.errors)
            messages.error(request, f'Video not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/gallery/video_gallery/add_video.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_video_gallery(request, video_id):
    video = VideoGallery.objects.get(id=video_id)
    form = VideoUpdateForm(instance=video)
    if request.method == 'POST':
        form = VideoUpdateForm(request.POST, request.FILES or None, instance=video)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.created_by = request.user
            new_video.save()
            messages.success(request, 'Video updated successfully')
            return redirect('backend_video_gallery')
        else:
            print(form.errors)
            messages.error(request, f'Video not updated, {form.errors}')
    context = {'form': form, 'video': video}
    return render(request, 'backend/gallery/video_gallery/update_video.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_testimonials(request):
    testimonials = Testimonials.objects.all().order_by('-id')
    context = {'testimonials': testimonials}
    return render(request, 'backend/testimonial/testimonials.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_testimonial(request):
    form = TestimonialAddForm
    if request.method == 'POST':
        form = TestimonialAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_testimonials = form.save(commit=False)
            new_testimonials.created_by = request.user
            new_testimonials.save()
            messages.success(request, 'Testimonials added successfully')
            return redirect('backend_testimonials')
        else:
            print(form.errors)
            messages.error(request, f'Testimonials not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/testimonial/add_testimonial.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_testimonial(request, testimonial_id):
    testimonial = Testimonials.objects.get(id=testimonial_id)
    form = TestimonialUpdateForm(instance=testimonial)
    if request.method == 'POST':
        form = TestimonialUpdateForm(request.POST, request.FILES or None, instance=testimonial)
        if form.is_valid():
            new_testimonial = form.save(commit=False)
            new_testimonial.created_by = request.user
            new_testimonial.save()
            messages.success(request, 'Testimonials updated successfully')
            return redirect('backend_testimonials')
        else:
            print(form.errors)
            messages.error(request, f'Testimonials not updated, {form.errors}')
    context = {'form': form, 'testimonial': testimonial}
    return render(request, 'backend/testimonial/update_testimonial.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_placements(request):
    placements = Placements.objects.all().order_by('-id')
    context = {'placements': placements}
    return render(request, 'backend/placement/placements.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_placement(request):
    form = PlacementAddForm
    if request.method == 'POST':
        form = PlacementAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_placement = form.save(commit=False)
            new_placement.created_by = request.user
            new_placement.save()
            messages.success(request, 'Placement added successfully')
            return redirect('backend_placements')
        else:
            print(form.errors)
            messages.error(request, f'Placement not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/placement/add_placement.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_placement(request, placement_id):
    placement = Placements.objects.get(id=placement_id)
    form = PlacementUpdateForm(instance=placement)
    if request.method == 'POST':
        form = PlacementUpdateForm(request.POST, request.FILES or None, instance=placement)
        if form.is_valid():
            new_placement = form.save(commit=False)
            new_placement.created_by = request.user
            new_placement.save()
            messages.success(request, 'Placement updated successfully')
            return redirect('backend_placements')
        else:
            print(form.errors)
            messages.error(request, f'Placement not updated, {form.errors}')
    context = {'form': form, 'placement': placement}
    return render(request, 'backend/placement/update_placement.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_placement_partners(request):
    placement_partners = PlacementPartners.objects.all()
    context = {'placement_partners': placement_partners}
    return render(request, 'backend/placement/placement_partner/placement_partners.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_placement_partner(request):
    form = PlacementPartnerAddForm
    if request.method == 'POST':
        form = PlacementPartnerAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_placement_partner = form.save(commit=False)
            new_placement_partner.created_by = request.user
            new_placement_partner.save()
            messages.success(request, 'Placement Partner added successfully')
            return redirect('backend_placement_partners')
        else:
            print(form.errors)
            messages.error(request, f'Placement Partner not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/placement/placement_partner/add_placement_partner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_placement_partner(request, placement_partner_id):
    placement_partner = PlacementPartners.objects.get(id=placement_partner_id)
    form = PlacementPartnerUpdateForm(instance=placement_partner)
    if request.method == 'POST':
        form = PlacementPartnerUpdateForm(request.POST, request.FILES or None, instance=placement_partner)
        if form.is_valid():
            new_placement_partner = form.save(commit=False)
            new_placement_partner.created_by = request.user
            new_placement_partner.save()
            messages.success(request, 'Placement Partner updated successfully')
            return redirect('backend_placement_partners')
        else:
            print(form.errors)
            messages.error(request, f'Placement Partner not updated, {form.errors}')
    context = {'form': form, 'placement_partner': placement_partner}
    return render(request, 'backend/placement/placement_partner/update_placement_partner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_awards(request):
    awards = Awards.objects.all().order_by('-id')
    context = {'awards': awards}
    return render(request, 'backend/awards/awards.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_award(request):
    form = AwardAddForm
    if request.method == 'POST':
        form = AwardAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_award = form.save(commit=False)
            new_award.created_by = request.user
            new_award.save()
            messages.success(request, 'Award added successfully')
            return redirect('backend_awards')
        else:
            print(form.errors)
            messages.error(request, f'Award not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/awards/add_award.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_award(request, award_id):
    award = Awards.objects.get(id=award_id)
    form = AwardUpdateForm(instance=award)
    if request.method == 'POST':
        form = AwardUpdateForm(request.POST, request.FILES or None, instance=award)
        if form.is_valid():
            new_award = form.save(commit=False)
            new_award.created_by = request.user
            new_award.save()
            messages.success(request, 'Award updated successfully')
            return redirect('backend_awards')
        else:
            print(form.errors)
            messages.error(request, f'Award not updated, {form.errors}')
    context = {'form': form, 'award': award}
    return render(request, 'backend/awards/update_award.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_global_opportunities(request):
    global_opportunities = GlobalOpportunities.objects.all().order_by('-id')
    context = {'global_opportunities': global_opportunities}
    return render(request, 'backend/global_opportunities/global_opportunities.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_global_opportunity(request):
    form = GlobalOpportunityAddForm
    if request.method == 'POST':
        form = GlobalOpportunityAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_global_opportunity = form.save(commit=False)
            new_global_opportunity.created_by = request.user
            new_global_opportunity.save()
            messages.success(request, 'Global Opportunity added successfully')
            return redirect('backend_global_opportunities')
        else:
            print(form.errors)
            messages.error(request, f'Global Opportunity not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/global_opportunities/add_global_opportunity.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_global_opportunity(request, global_opportunity_id):
    global_opportunity = GlobalOpportunities.objects.get(id=global_opportunity_id)
    form = GlobalOpportunityUpdateForm(instance=global_opportunity)
    if request.method == 'POST':
        form = GlobalOpportunityUpdateForm(request.POST, request.FILES or None, instance=global_opportunity)
        if form.is_valid():
            new_global_opportunity = form.save(commit=False)
            new_global_opportunity.created_by = request.user
            new_global_opportunity.save()
            messages.success(request, 'Global Opportunity updated successfully')
            return redirect('backend_global_opportunities')
        else:
            print(form.errors)
            messages.error(request, f'Global Opportunity not updated, {form.errors}')
    context = {'form': form, 'global_opportunity': global_opportunity}
    return render(request, 'backend/global_opportunities/update_global_opportunity.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_pages(request):
    pages = Page.objects.all().order_by('-id')
    context = {'pages': pages}
    return render(request, 'backend/pages/pages.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_page(request):
    form = PageAddForm
    if request.method == 'POST':
        form = PageAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_page = form.save(commit=False)
            new_page.created_by = request.user
            new_page.save()
            messages.success(request, 'Page added successfully')
            return redirect('backend_pages')
        else:
            print(form.errors)
            messages.error(request, f'Page not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/pages/add_page.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_page(request, page_id):
    page = Page.objects.get(id=page_id)
    form = PageUpdateForm(instance=page)
    if request.method == 'POST':
        form = PageUpdateForm(request.POST, request.FILES or None, instance=page)
        if form.is_valid():
            new_page = form.save(commit=False)
            new_page.created_by = request.user
            new_page.save()
            messages.success(request, 'Page updated successfully')
            return redirect('backend_pages')
        else:
            print(form.errors)
            messages.error(request, f'Page not updated, {form.errors}')
    context = {'form': form, 'page': page}
    return render(request, 'backend/pages/update_page.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_partners(request):
    partners = Partners.objects.all().order_by('-id')
    context = {'partners': partners}
    return render(request, 'backend/partners/partners.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_partner(request):
    form = PartnerAddForm
    if request.method == 'POST':
        form = PartnerAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_partner = form.save(commit=False)
            new_partner.created_by = request.user
            new_partner.save()
            messages.success(request, 'Partner added successfully')
            return redirect('backend_partners')
        else:
            print(form.errors)
            messages.error(request, f'Partner not added, {form.errors}')
    context = {'form': form}
    return render(request, 'backend/partners/add_partner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_partner(request, partner_id):
    partner = Partners.objects.get(id=partner_id)
    form = PartnerUpdateForm(instance=partner)
    if request.method == 'POST':
        form = PartnerUpdateForm(request.POST, request.FILES or None, instance=partner)
        if form.is_valid():
            new_partner = form.save(commit=False)
            new_partner.created_by = request.user
            new_partner.save()
            messages.success(request, 'Partner updated successfully')
            return redirect('backend_partners')
        else:
            print(form.errors)
            messages.error(request, f'Partner not updated, {form.errors}')
    context = {'form': form, 'partner': partner}
    return render(request, 'backend/partners/update_partner.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_jurymembers(request):
    jury_members = JuryMember.objects.all().order_by('-id')
    context = {'jury_members': jury_members}
    return render(request, 'backend/jury_members/jury_members.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_jurymember(request):
    form = JuryMemberAddForm
    if request.method == 'POST':
        form = JuryMemberAddForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_jury_member = form.save(commit=False)
            new_jury_member.created_by = request.user
            new_jury_member.save()
            messages.success(request, 'Jury Member added successfully')
            return redirect('backend_jury_members')
        else:
            print(form.errors)
            messages.error(request, f'Jury Member not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/jury_members/add_jurymember.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_jurymember(request, mentor_id):
    jury_member = JuryMember.objects.get(id=mentor_id)
    form = JuryMemberUpdateForm(instance=jury_member)
    if request.method == 'POST':
        form = JuryMemberUpdateForm(request.POST, request.FILES or None, instance=jury_member)
        if form.is_valid():
            new_jury_member = form.save(commit=False)
            new_jury_member.save()
            messages.success(request, 'Jury Member updated successfully')
            return redirect('backend_jury_members')
        else:
            print(form.errors)
            messages.error(request, f'Jury Member not updated, {form.errors}')
    context = {'form': form, 'jury_member': jury_member}
    return render(request, 'backend/jury_members/update_jurymember.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'marketing'])
def backend_blogposts(request):
    blog_posts = Blogpost.objects.all().order_by('-id')
    context = {'blog_posts': blog_posts}
    return render(request, 'backend/blogpost/blogposts.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'marketing'])
def backend_add_blogpost(request):
    form = BlogpostForm
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.created_by = request.user
            new_blogpost.save()
            messages.success(request, 'Blogpost added successfully')
            return redirect('backend_blogposts')
        else:
            print(form.errors)
            messages.error(request, f'Blogpost not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/blogpost/add_blogpost.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff', 'marketing'])
def backend_update_blogpost(request, blogpost_id):
    blogpost = Blogpost.objects.get(id=blogpost_id)
    form = BlogpostForm(instance=blogpost)
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES or None, instance=blogpost)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.save()
            messages.success(request, 'Blogpost updated successfully')
            return redirect('backend_blogposts')
        else:
            print(form.errors)
            messages.error(request, f'Blogpost not updated, {form.errors}')
    context = {'form': form, 'blogpost': blogpost}
    return render(request, 'backend/blogpost/update_blogpost.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_homepage_sections(request):
    homepage_sections = HomepageSection.objects.all().order_by('-id')
    context = {'homepage_sections': homepage_sections}
    return render(request, 'backend/homepage_sections/homepage_sections.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_homepage_section(request, homepage_section_id):
    homepage_section = HomepageSection.objects.get(id=homepage_section_id)
    form = HomepageSectionUpdateForm(instance=homepage_section)
    if request.method == 'POST':
        form = HomepageSectionUpdateForm(request.POST, request.FILES or None, instance=homepage_section)
        if form.is_valid():
            new_homepage_section = form.save(commit=False)
            new_homepage_section.save()
            messages.success(request, 'Homepage section updated successfully')
            return redirect('backend_homepage_sections')
        else:
            print(form.errors)
            messages.error(request, f'Homepage section not updated, {form.errors}')
    context = {'form': form, 'homepage_section': homepage_section}
    return render(request, 'backend/homepage_sections/update_homepage_sections.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_collaborations(request):
    collaborations = Collaboration.objects.all().order_by('-id')
    context = {'collaborations': collaborations}
    return render(request, 'backend/collaboration/collaborations.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_collaboration(request):
    form = CollaborationForm
    if request.method == 'POST':
        form = CollaborationForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_collaboration = form.save(commit=False)
            new_collaboration.created_by = request.user
            new_collaboration.save()
            messages.success(request, 'Collaboration added successfully')
            return redirect('backend_collaborations')
        else:
            print(form.errors)
            messages.error(request, f'Collaboration not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/collaboration/add_collaboration.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_collaboration(request, collaboration_id):
    collaboration = Collaboration.objects.get(id=collaboration_id)
    form = CollaborationUpdateForm(instance=collaboration)
    if request.method == 'POST':
        form = CollaborationUpdateForm(request.POST, request.FILES or None, instance=collaboration)
        if form.is_valid():
            new_collaboration = form.save(commit=False)
            new_collaboration.save()
            messages.success(request, 'Collaboration updated successfully')
            return redirect('backend_collaborations')
        else:
            print(form.errors)
            messages.error(request, f'Collaboration not updated, {form.errors}')
    context = {'form': form, 'collaboration': collaboration}
    return render(request, 'backend/collaboration/update_collaboration.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_interior_exhibitions(request):
    interior_exhibitions = InteriorExhibition.objects.all().order_by('-id')
    context = {'interior_exhibitions': interior_exhibitions}
    return render(request, 'backend/interior_exhibition/exhibitions.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_interior_exhibition(request):
    form = InteriorExhibitionForm
    if request.method == 'POST':
        form = InteriorExhibitionForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_interior_exhibition = form.save(commit=False)
            new_interior_exhibition.created_by = request.user
            new_interior_exhibition.save()
            messages.success(request, 'Interior exhibition added successfully')
            return redirect('backend_interior_exhibitions')
        else:
            print(form.errors)
            messages.error(request, f'Interior exhibition not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/interior_exhibition/add_exhibition.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_interior_exhibition(request, interior_exhibition_id):
    interior_exhibition = InteriorExhibition.objects.get(id=interior_exhibition_id)
    form = InteriorExhibitionUpdateForm(instance=interior_exhibition)
    if request.method == 'POST':
        form = InteriorExhibitionUpdateForm(request.POST, request.FILES or None, instance=interior_exhibition)
        if form.is_valid():
            new_interior_exhibition = form.save(commit=False)
            new_interior_exhibition.save()
            messages.success(request, 'Interior exhibition updated successfully')
            return redirect('backend_interior_exhibitions')
        else:
            print(form.errors)
            messages.error(request, f'Interior exhibition not updated, {form.errors}')
    context = {'form': form, 'interior_exhibition': interior_exhibition}
    return render(request, 'backend/interior_exhibition/update_exhibition.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_fashion_shows(request):
    fashion_shows = FashionShows.objects.all().order_by('-id')
    context = {'fashion_shows': fashion_shows}
    return render(request, 'backend/fashion_shows/fashion_shows.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_fashion_show(request):
    form = FashionShowForm
    if request.method == 'POST':
        form = FashionShowForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_fashion_show = form.save(commit=False)
            new_fashion_show.created_by = request.user
            new_fashion_show.save()
            messages.success(request, 'Fashion show added successfully')
            return redirect('backend_fashion_shows')
        else:
            print(form.errors)
            messages.error(request, f'Fashion show not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/fashion_shows/add_fashion_show.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_fashion_show(request, fashion_show_id):
    fashion_show = FashionShows.objects.get(id=fashion_show_id)
    form = FashionShowUpdateForm(instance=fashion_show)
    if request.method == 'POST':
        form = FashionShowUpdateForm(request.POST, request.FILES or None, instance=fashion_show)
        if form.is_valid():
            new_fashion_show = form.save(commit=False)
            new_fashion_show.save()
            messages.success(request, 'Fashion show updated successfully')
            return redirect('backend_fashion_shows')
        else:
            print(form.errors)
            messages.error(request, f'Fashion show not updated, {form.errors}')
    context = {'form': form, 'fashion_show': fashion_show}
    return render(request, 'backend/fashion_shows/update_fashion_show.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_inhouse_mentors(request):
    inhouse_mentors = InHouseMentor.objects.all().order_by('-id')
    context = {'inhouse_mentors': inhouse_mentors}
    return render(request, 'backend/inhouse_mentor/inhouse_mentors.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_inhouse_mentor(request):
    form = InHouseMentorForm
    if request.method == 'POST':
        form = InHouseMentorForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_inhouse_mentor = form.save(commit=False)
            new_inhouse_mentor.created_by = request.user
            new_inhouse_mentor.save()
            messages.success(request, 'In house mentor added successfully')
            return redirect('backend_inhouse_mentors')
        else:
            print(form.errors)
            messages.error(request, f'In house mentor not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/inhouse_mentor/add_inhouse_mentor.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_inhouse_mentor(request, inhouse_mentor_id):
    inhouse_mentor = InHouseMentor.objects.get(id=inhouse_mentor_id)
    form = InHouseMentorUpdateForm(instance=inhouse_mentor)
    if request.method == 'POST':
        form = InHouseMentorUpdateForm(request.POST, request.FILES or None, instance=inhouse_mentor)
        if form.is_valid():
            new_inhouse_mentor = form.save(commit=False)
            new_inhouse_mentor.save()
            messages.success(request, 'In house mentor updated successfully')
            return redirect('backend_inhouse_mentors')
        else:
            messages.error(request, f'In house mentor not updated, {form.errors}')
    context = {'form': form, 'inhouse_mentor': inhouse_mentor}
    return render(request, 'backend/inhouse_mentor/update_inhouse_mentor.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_courses(request):
    courses = Course.objects.prefetch_related().filter(is_active=True).order_by('-id')
    context = {'courses': courses}
    return render(request, 'backend/courses/courses.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_course(request):
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.created_by = request.user
            new_course.save()
            messages.success(request, 'Course added successfully')
            return redirect('backend_courses')
        else:
            messages.error(request, f'Course not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/courses/add_course.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.save()
            messages.success(request, 'Course updated successfully')
            return redirect('backend_courses')
        else:
            messages.error(request, f'Course not updated, {form.errors}')
    context = {'form': form, 'course': course}
    return render(request, 'backend/courses/update_course.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_course_career_options(request):
    career_options = CareerOptions.objects.all().order_by('-id')
    context = {'career_options': career_options}
    return render(request, 'backend/career_options/career_options.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_add_course_career_option(request):
    form = CareerOptionForm
    if request.method == 'POST':
        form = CareerOptionForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_career_option = form.save(commit=False)
            new_career_option.created_by = request.user
            new_career_option.save()
            messages.success(request, 'Career option added successfully')
            return redirect('backend_course_career_options')
        else:
            messages.error(request, f'Career option not added,  {form.errors}')
    context = {'form': form}
    return render(request, 'backend/career_options/add_career_option.html', context)


@login_required(login_url='backend_login/')
@allowedUsers(['admin', 'staff'])
def backend_update_course_career_option(request, career_option_id):
    career_option = CareerOptions.objects.get(id=career_option_id)
    form = CareerOptionForm(instance=career_option)
    if request.method == 'POST':
        form = CareerOptionForm(request.POST, instance=career_option)
        if form.is_valid():
            new_career_option = form.save(commit=False)
            new_career_option.save()
            messages.success(request, 'Career option updated successfully')
            return redirect('backend_course_career_options')
        else:
            messages.error(request, f'Career option not updated, {form.errors}')
    context = {'form': form, 'career_option': career_option}
    return render(request, 'backend/career_options/update_career_option.html', context)