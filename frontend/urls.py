from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-inifd/', views.about_inifd, name='about_inifd'),
    path('media-coverage/', views.media_coverage, name='media_coverage'),
    path('award-recognition/', views.award_and_recognition, name='award_and_recognition'),
    path('global-opportunities/', views.global_opportunities, name='global_opportunities'),
    path('global-opportunities/<int:opportunity_id><str:opportunity_slug>/', views.view_opportunity,
         name='view_opportunity'),
    path('interior-design-course/', views.interior_design_course, name='interior_design_course'),
    path('interior-design-course/career-options/', views.interior_design_course_career_option,
         name='interior_design_course_career_option'),
    path('interior-design-course/download-brochure/', views.interior_design_course_download_brochure,
         name='interior_design_course_download_brochure'),
    path('interior-design-course/admission-form/', views.interior_design_addmisson_form,
         name='interior_design_addmisson_form'),
    path('fashion-design-course/', views.fashion_design_course, name='fashion_design_course'),
    path('fashion-design-course/career-options/', views.fashion_design_course_career_option,
         name='fashion_design_course_career_option'),
    path('fashion-design-course/download-brochure/', views.fashion_design_course_download_brochure,
         name='fashion_design_course_download_brochure'),
    path('fashion-design-course/admission-form/', views.fashion_design_addmisson_form,
         name='fashion_design_admission_form'),
    path('gallery', views.gallery, name='gallery'),
    path('upcoming-events', views.upcoming_events, name='upcoming_events'),
    path('past-events', views.past_events, name='past_events'),
    path('events/<str:slug>', views.view_event, name='view_event'),
    path('stuents-work', views.students_work, name='students_work'),
    path('jury-members', views.jury_members, name='jury_members'),
    path('videos-gallery', views.videos_gallery, name='videos_gallery'),
    path('success-stories', views.success_stories, name='success_stories'),
    path('placement-support', views.placement_support, name='placement_support'),
    path('contact-us', views.contact_us, name='contact_us'),

    # Form submission
    path('submit-lead-form/', views.submit_lead_form, name='submit_course_enquiry'),
    path('lead-form/otp-verification/', views.enquiry_otp_validation, name='enquiry_otp_validation'),
    path('submit-application-form/', views.submit_application_form, name='submit_application_form'),

    path('submit-page-enquiry-form/', views.submit_page_enquiry_form, name='submit_page_enquiry_form'),
    path('view_page/<int:page_id><str:page_slug>', views.view_page, name='view_page'),

    path('handle-admission-form/', views.handle_admission_form, name='handle_admission_form'),

]