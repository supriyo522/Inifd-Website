import json
import re
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from ipware import get_client_ip

from backend.forms import CourseEnquiryForm, AdmissionForm
from backend.models import (
    MainBanners,
    Placements,
    Mentors,
    MediaCoverage,
    Testimonials,
    AcademicTours,
    ImageGallery,
    PlacementPartners,
    Awards,
    InteriorDesignGallery,
    FashionDesignGallery,
    Events,
    Enquiries, Page, GlobalOpportunities, StudentWork, VideoGallery, JuryMember, EnquiryFormOTP,
    InteriorExhibition, FashionShows, Collaboration, InHouseMentor, Partners, Course, CareerOptions
)
# Create your views here.
from backend.tasks import send_enquiry_form_otp, send_enquiry_email


def index(request):
    main_banners = MainBanners.objects.filter(is_active=True).only('image', 'title')
    placements = Placements.objects.filter(is_active=True, show_at_home=True)[:12]
    mentors = Mentors.objects.filter(is_active=True)[:12]
    media_coverages = MediaCoverage.objects.filter(is_active=True, show_at_home=True)[:12]
    academic_tours = AcademicTours.objects.filter(is_active=True, show_at_home=True)[:10]
    collaboration_with_fashion = Partners.objects.filter(is_active=True, show_at_home=True,
                                                         course_type="fashion")[:10]
    collaboration_with_interior = Partners.objects.filter(is_active=True, show_at_home=True,
                                                          course_type="interior")[:10]
    jury_membersd = JuryMember.objects.filter(is_active=True)
    videos = VideoGallery.objects.filter(is_active=True, show_in_home=True)[:12]

    context = {
        "main_banners": main_banners,
        'events_interior': Events.objects.filter(is_active=True, show_at_home=True, course_type="interior").only(
            'banner', 'title', 'slug').order_by("-id")[:8],
        'events_fashion': Events.objects.filter(is_active=True, show_at_home=True, course_type="fashion").only(
            'banner', 'title').order_by("-id")[:8],
        "collaboration_with_fashion": collaboration_with_fashion,
        "collaboration_with_interior": collaboration_with_interior,
        "interior_exhibition": InteriorExhibition.objects.filter(is_active=True, show_at_home=True).only('image',
                                                                                                         'title')[:12],
        "fashion_shows": FashionShows.objects.filter(is_active=True, show_at_home=True).only('image',
                                                                                             'title')[:12],
        "placements": placements,
        "mentors": mentors,
        "media_coverages": media_coverages,
        'inhouse_mentors': InHouseMentor.objects.filter(is_active=True, show_at_home=True)[:12],
        "testimonials_interior": Testimonials.objects.filter(is_active=True, show_at_home=True,
                                                             course_type="interior").only('image', 'title',
                                                                                          'description')[:12],
        "testimonials_fashion": Testimonials.objects.filter(is_active=True, show_at_home=True,
                                                            course_type="fashion").only('image', 'title',
                                                                                        'description')[:12],
        "academic_tours": academic_tours,
        'partners_interior': PlacementPartners.objects.filter(is_active=True, show_at_home=True,
                                                              course_type="interior").only('image', 'title')[:12],
        'partners_fashion': PlacementPartners.objects.filter(is_active=True, show_at_home=True,
                                                             course_type="fashion").only('image', 'title')[:12],
        'jury_members': jury_membersd,
        'videos': videos,

    }
    return render(request, "frontend/index.html", context)


regex = re.compile("^[6-9]\d{9}$")


def submit_lead_form(request):
    ip, is_routable = get_client_ip(request)
    if request.method == "POST":
        data = json.loads(request.body)
        if regex.match(data["phone"]):
            new_enquiry = Enquiries.objects.create(name=data["name"], phone=data["phone"], ip_address=ip, )
            new_enquiry.save()
            send_enquiry_form_otp(data["phone"])
            return JsonResponse({"success": True, 'mobile': data["phone"]})
    else:
        return JsonResponse({"success": False})


def enquiry_otp_validation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if regex.match(data["phone"]):
            try:
                last_otp = EnquiryFormOTP.objects.filter(mobile=data["phone"]).last()
                if last_otp.is_used is False and last_otp.otp == data["otp"]:
                    last_otp.is_used = True
                    last_otp.save()
                    enquiry = Enquiries.objects.filter(phone=data["phone"]).last()
                    enquiry.is_verified = True
                    enquiry.save()
                    send_enquiry_email.delay(enquiry.id)
                    return JsonResponse({"success": True, "message": "OTP verified successfully"})
                else:
                    return JsonResponse({"success": False, "message": "OTP is invalid"})
            except EnquiryFormOTP.DoesNotExist:
                return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": False})


def submit_application_form(request):
    ip, is_routable = get_client_ip(request)
    if request.method == "POST":
        data = json.loads(request.body)
        if regex.match(data["phone"]):
            new_enquiry = Enquiries.objects.create(name=data["name"], phone=data["phone"], email=data["email"],
                                                   course=data["course"], message=data["message"], ip_address=ip, )
            new_enquiry.save()
            return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


def submit_page_enquiry_form(request):
    ip, is_routable = get_client_ip(request)
    if request.method == "POST":
        form = CourseEnquiryForm(request.POST)
        # print(request.POST.get('name'))
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if regex.match(phone):
                new_query = form.save(commit=False)
                new_query.ip_address = ip
                new_query.save()
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": False})


def view_page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    form = CourseEnquiryForm
    context = {"page": page, "form": form}
    return render(request, "frontend/view_page.html", context)


def about_inifd(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/about.html", context)


def media_coverage(request):
    form = CourseEnquiryForm
    media_coverages = MediaCoverage.objects.filter(is_active=True)
    context = {"form": form, "media_coverages": media_coverages}
    return render(request, "frontend/media_coverage.html", context)


def award_and_recognition(request):
    form = CourseEnquiryForm
    awards = Awards.objects.filter(is_active=True)
    context = {"form": form, "awards": awards}
    return render(request, "frontend/award_recognition.html", context)


def global_opportunities(request):
    form = CourseEnquiryForm
    items = GlobalOpportunities.objects.filter(is_active=True)
    context = {"form": form, "global_opportunities": items}
    return render(request, "frontend/global_opportunities.html", context)


def view_opportunity(request, opportunity_id, opportunity_slug):
    opportunity = get_object_or_404(GlobalOpportunities, id=opportunity_id)
    form = CourseEnquiryForm
    context = {"opportunity": opportunity, "form": form}
    return render(request, "frontend/view_opportunity.html", context)


def interior_design_course(request):
    form = CourseEnquiryForm
    i_items = InteriorDesignGallery.objects.filter(is_active=True)
    courses = Course.objects.filter(is_active=True, course_type="interior")
    career_options = CareerOptions.objects.filter(is_active=True, course_type="interior")
    context = {"form": form, "i_items": i_items, "courses": courses, "career_options": career_options}
    return render(
        request, "frontend/interior_design/interior_design_course.html", context
    )


def interior_design_course_career_option(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/interior_design/career_options.html", context)


def interior_design_course_download_brochure(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/interior_design/download_brochure.html", context)


def interior_design_addmisson_form(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/interior_design/admission_form.html", context)


def fashion_design_course(request):
    form = CourseEnquiryForm
    f_items = FashionDesignGallery.objects.filter(is_active=True)
    courses = Course.objects.filter(is_active=True, course_type="fashion")
    career_options = CareerOptions.objects.filter(is_active=True, course_type="fashion")
    context = {"form": form, "f_items": f_items, "courses": courses, "career_options": career_options}
    return render(
        request, "frontend/fashion_design/fashion_design_course.html", context
    )


def fashion_design_course_career_option(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/fashion_design/career_options.html", context)


def fashion_design_course_download_brochure(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/fashion_design/download_brochure.html", context)


def fashion_design_addmisson_form(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/fashion_design/admission_form.html", context)


def gallery(request):
    form = CourseEnquiryForm
    items = ImageGallery.objects.filter(is_active=True, galley_type="student")
    context = {"form": form, "items": items}
    return render(request, "frontend/gallery.html", context)


def upcoming_events(request):
    form = CourseEnquiryForm
    events = Events.objects.filter(date__gte=datetime.now(), is_active=True)
    context = {"form": form, "events": events}
    return render(request, "frontend/students_life/upcoming_events.html", context)


def view_event(request, slug):
    form = CourseEnquiryForm
    event = Events.objects.get(slug=slug)
    context = {"form": form, "event": event}
    return render(request, "frontend/view_event.html", context)


def past_events(request):
    form = CourseEnquiryForm
    events = Events.objects.filter(is_active=True, date__lte=datetime.now())
    context = {"form": form, "events": events}
    return render(request, "frontend/students_life/past_events.html", context)


def students_work(request):
    form = CourseEnquiryForm
    items = StudentWork.objects.filter(is_active=True)
    context = {"form": form, "items": items}
    return render(request, "frontend/students_life/students_work.html", context)


def jury_members(request):
    form = CourseEnquiryForm
    members = JuryMember.objects.filter(is_active=True)
    context = {"form": form, "members": members}
    return render(request, "frontend/jury_members.html", context)


def videos_gallery(request):
    form = CourseEnquiryForm
    videos = VideoGallery.objects.filter(is_active=True)
    context = {"form": form, "videos": videos}
    return render(request, "frontend/students_life/videos.html", context)


def success_stories(request):
    form = CourseEnquiryForm
    stories = Testimonials.objects.filter(is_active=True)
    context = {"form": form, "stories": stories}
    return render(request, "frontend/success_stories.html", context)


def placement_support(request):
    form = CourseEnquiryForm
    placements = Placements.objects.filter(is_active=True)
    context = {"form": form, "placements": placements}
    return render(request, "frontend/placement_support.html", context)


def contact_us(request):
    form = CourseEnquiryForm
    context = {"form": form}
    return render(request, "frontend/contact_us.html", context)


def handler404(request, exception):
    return render(request, "frontend/404.html", status=404)


def handle_admission_form(request):
    if request.method == "POST":
        form_data = request.POST, request.FILES
        form = AdmissionForm(*form_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "We have received your request. We will contact you soon."})
        else:
            return JsonResponse({"status": "error", "message": "Please fill all the fields"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request"})
