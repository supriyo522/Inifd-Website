import random
import requests
from PIL import Image
from inifd.celery_app import app
from django.core.mail import get_connection, EmailMessage
from django.template.loader import get_template

import backend.models
from inifd import settings


@app.task(bind=True)
def compress_banner_image(self, banner_id):
    banner = backend.models.MainBanners.objects.get(id=banner_id)
    if banner.image:
        image = Image.open(banner.image.path)
        image.save(banner.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_sub_banner_image(self, sub_banner_id):
    sub_banner = backend.models.SubBanners.objects.get(id=sub_banner_id)
    if sub_banner.image:
        image = Image.open(sub_banner.image.path)
        image.save(sub_banner.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_placement_image(self, placement_id):
    placement = backend.models.Placements.objects.get(id=placement_id)
    if placement.image:
        image = Image.open(placement.image.path)
        image.save(placement.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_interior_exhibition_image(self, interior_exhibition_id):
    interior_exhibition = backend.models.InteriorExhibition.objects.get(id=interior_exhibition_id)
    if interior_exhibition.image:
        image = Image.open(interior_exhibition.image.path)
        image.save(interior_exhibition.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_fashion_show_image(self, fashion_show_id):
    fashion_show = backend.models.FashionShows.objects.get(id=fashion_show_id)
    if fashion_show.image:
        image = Image.open(fashion_show.image.path)
        image.save(fashion_show.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_inhouse_mentor_image(self, inhouse_mentor_id):
    inhouse_mentor = backend.models.InHouseMentor.objects.get(id=inhouse_mentor_id)
    if inhouse_mentor.profile_image:
        image = Image.open(inhouse_mentor.image.path)
        image.save(inhouse_mentor.profile_image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_testimonial_image(self, testimonial_id):
    testimonial = backend.models.Testimonials.objects.get(id=testimonial_id)
    if testimonial.image:
        image = Image.open(testimonial.image.path)
        image.save(testimonial.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_mentor_profile_image(self, mentor_id):
    mentor = backend.models.Mentors.objects.get(id=mentor_id)
    if mentor.profile_image:
        image = Image.open(mentor.profile_image.path)
        image.save(mentor.profile_image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_media_coverage_image(self, media_coverage_id):
    media_coverage = backend.models.MediaCoverage.objects.get(id=media_coverage_id)
    if media_coverage.image:
        image = Image.open(media_coverage.image.path)
        image.save(media_coverage.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_event_banner(self, event_id):
    event = backend.models.Events.objects.get(id=event_id)
    if event.banner:
        image = Image.open(event.banner.path)
        image.save(event.banner.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_event_gallery_image(self, event_gallery_id):
    event_gallery = backend.models.EventGallery.objects.get(id=event_gallery_id)
    if event_gallery.image:
        image = Image.open(event_gallery.image.path)
        image.save(event_gallery.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_award_image(self, award_id):
    award = backend.models.Awards.objects.get(id=award_id)
    if award.image:
        image = Image.open(award.image.path)
        image.save(award.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_global_opportunity_banner(self, global_opportunity_id):
    global_opportunity = backend.models.GlobalOpportunities.objects.get(id=global_opportunity_id)
    if global_opportunity.banner:
        image = Image.open(global_opportunity.banner.path)
        image.save(global_opportunity.banner.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_academic_tour_banner(self, academic_tour_id):
    academic_tour = backend.models.AcademicTours.objects.get(id=academic_tour_id)
    if academic_tour.banner:
        image = Image.open(academic_tour.banner.path)
        image.save(academic_tour.banner.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_imagegallery_image(self, imagegallery_id):
    imagegallery = backend.models.ImageGallery.objects.get(id=imagegallery_id)
    if imagegallery.image:
        image = Image.open(imagegallery.image.path)
        image.save(imagegallery.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_placement_partner_image(self, placement_partner_id):
    placement_partner = backend.models.PlacementPartners.objects.get(id=placement_partner_id)
    if placement_partner.image:
        image = Image.open(placement_partner.image.path)
        image.save(placement_partner.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_fashion_design_gallery_image(self, fashion_design_gallery_id):
    fashion_design_gallery = backend.models.FashionDesignGallery.objects.get(id=fashion_design_gallery_id)
    if fashion_design_gallery.image:
        image = Image.open(fashion_design_gallery.image.path)
        image.save(fashion_design_gallery.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_interior_design_gallery_image(self, interior_design_gallery_id):
    interior_design_gallery = backend.models.InteriorDesignGallery.objects.get(id=interior_design_gallery_id)
    if interior_design_gallery.image:
        image = Image.open(interior_design_gallery.image.path)
        image.save(interior_design_gallery.image.path, optimize=True, quality=60)


@app.task(bind=True)
def compress_student_work_image(self, student_work_id):
    student_work = backend.models.StudentWork.objects.get(id=student_work_id)
    if student_work.image:
        image = Image.open(student_work.image.path)
        image.save(student_work.image.path, optimize=True, quality=60)


@app.task(bind=True)
def send_enquiry_email(self, enquiry_id):
    enquiry = backend.models.Enquiries.objects.get(id=enquiry_id)
    connection = get_connection(backend=settings.EMAIL_BACKEND, host=settings.EMAIL_HOST, port=settings.EMAIL_PORT,
                                username=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD,
                                use_tls=settings.EMAIL_USE_TLS, fail_silently=False)

    template = get_template('backend/emails/enquiry_email.html')
    message = template.render({'enquiry': enquiry})
    email_subject = 'New enquiry received '
    to_email = ['kky751990@gmail.com', 'inifdezo@gmail.com']
    email = EmailMessage(email_subject, message, to=to_email,
                         connection=connection)
    email.content_subtype = 'html'
    email.send()


@app.task(bind=True)
def send_enquiry_form_otp(self, mobile):
    otp = random.randint(1000, 9999)
    template = "OTP LOGIN"
    mobile = str(mobile)
    url = f'https://2factor.in/API/V1/a23eba5f-0f0d-11ed-9c12-0200cd936042/SMS/{mobile}/{otp}/{template}'
    response = requests.get(url)
    data = response.json()
    print(data)
    if data['Status'] == 'Success':
        backend.models.EnquiryFormOTP.objects.create(mobile=mobile, otp=otp)
        return True
    else:
        return False
