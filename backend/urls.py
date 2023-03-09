from django.urls import path

from . import views

urlpatterns = [
    path('', views.backend_login, name='backend_login'),
    path('logout/', views.backend_logout, name='backend_logout'),
    path('dashboard', views.backend_dashboard, name='backend_dashboard'),
    path('website-settings', views.backend_website_settings, name='backend_website_settings'),
    path('website-settings/about-us', views.backend_about_us, name='backend_about_us'),
    path('menu-items', views.backend_menu_items, name='backend_menu_items'),
    path('menu-items/add', views.backend_add_menu_item, name='backend_add_menu_item'),
    path('leads-enquiry', views.backend_leads_enquiry, name='backend_leads_enquiry'),
    path('leads-enquiry/details/<int:enquiry_id>', views.backend_leads_enquiry_details,
         name='backend_leads_enquiry_details'),
    path('leads-enquiry/<int:enquiry_id>update', views.backend_leads_enquiry_update,
         name='backend_leads_enquiry_update'),

    # Banners
    path('banners', views.backend_main_banners, name='backend_main_banners'),
    path('banners/add', views.backend_add_main_banner, name='backend_add_main_banner'),
    path('banners/<int:banner_id>update', views.backend_update_main_banner, name='backend_update_main_banner'),

    # Sub Banners
    path('sub-banners', views.backend_sub_banners, name='backend_sub_banners'),
    path('sub-banners/add', views.backend_add_sub_banner, name='backend_add_sub_banner'),
    path('sub-banners/<int:banner_id>update', views.backend_update_sub_banner, name='backend_update_sub_banner'),

    # Mentors
    path('mentors', views.backend_mentors, name='backend_mentors'),
    path('mentors/add', views.backend_add_mentor, name='backend_add_mentor'),
    path('mentors/<int:mentor_id>update', views.backend_update_mentor, name='backend_update_mentor'),

    # Media coverage
    path('media-coverages', views.backend_media_coverages, name='backend_media_coverages'),
    path('media-coverages/add', views.backend_add_media_coverage, name='backend_add_media_coverage'),
    path('media-coverages/<int:media_coverage_id>update', views.backend_update_media_coverage,
         name='backend_update_media_coverage'),

    # Events
    path('events', views.backend_events, name='backend_events'),
    path('events/past-events', views.backend_past_events, name='backend_past_events'),
    path('events/upcoming-events', views.backend_upcoming_events, name='backend_upcoming_events'),
    path('events/<int:event_id>view', views.backend_view_event, name='backend_view_event'),
    path('events/add', views.backend_add_event, name='backend_add_event'),
    path('events/<int:event_id>update', views.backend_update_event, name='backend_update_event'),

    # Student's work
    path('students-work', views.backend_student_works, name='backend_student_works'),
    path('students-work/add', views.backend_add_student_work, name='backend_add_student_work'),
    path('students-work/<int:student_work_id>update', views.backend_update_student_work,
         name='backend_update_student_work'),

    # Academic tours
    path('academic-tours', views.backend_academic_tours, name='backend_academic_tours'),
    path('academic-tours/add', views.backend_add_academic_tour, name='backend_add_academic_tour'),
    path('academic-tours/<int:academic_tour_id>update', views.backend_update_academic_tour,
         name='backend_update_academic_tour'),

    # Image gallery
    path('image-gallery', views.backend_image_gallery, name='backend_image_gallery'),
    path('image-gallery/add', views.backend_add_image_gallery, name='backend_add_image_gallery'),
    path('image-gallery/<int:image_id>update', views.backend_update_image_gallery,
         name='backend_update_image_gallery'),

    # Video gallery
    path('video-gallery', views.backend_video_gallery, name='backend_video_gallery'),
    path('video-gallery/add', views.backend_add_video_gallery, name='backend_add_video_gallery'),
    path('video-gallery/<int:video_id>update', views.backend_update_video_gallery,
         name='backend_update_video_gallery'),

    # Testimonials
    path('testimonials', views.backend_testimonials, name='backend_testimonials'),
    path('testimonials/add', views.backend_add_testimonial, name='backend_add_testimonial'),
    path('testimonials/<int:testimonial_id>update', views.backend_update_testimonial,
         name='backend_update_testimonial'),

    # Placements
    path('placements', views.backend_placements, name='backend_placements'),
    path('placements/add', views.backend_add_placement, name='backend_add_placement'),
    path('placements/<int:placement_id>update', views.backend_update_placement,
         name='backend_update_placement'),

    # Placement partners
    path('placement-partners', views.backend_placement_partners, name='backend_placement_partners'),
    path('placement-partners/add', views.backend_add_placement_partner, name='backend_add_placement_partner'),
    path('placement-partners/<int:placement_partner_id>update', views.backend_update_placement_partner,
         name='backend_update_placement_partner'),

    # Partners
    path('partners', views.backend_partners, name='backend_partners'),
    path('partners/add', views.backend_add_partner, name='backend_add_partner'),
    path('partners/<int:partner_id>update', views.backend_update_partner,
         name='backend_update_partner'),

    # Awards
    path('awards', views.backend_awards, name='backend_awards'),
    path('awards/add', views.backend_add_award, name='backend_add_award'),
    path('awards/<int:award_id>update', views.backend_update_award, name='backend_update_award'),

    # Global opportunities
    path('global-opportunities', views.backend_global_opportunities, name='backend_global_opportunities'),
    path('global-opportunities/add', views.backend_add_global_opportunity, name='backend_add_global_opportunity'),
    path('global-opportunities/<int:global_opportunity_id>update', views.backend_update_global_opportunity,
         name='backend_update_global_opportunity'),

    # Pages
    path('pages', views.backend_pages, name='backend_pages'),
    path('pages/add', views.backend_add_page, name='backend_add_page'),
    path('pages/<int:page_id>update', views.backend_update_page, name='backend_update_page'),

    # Mentors
    path('jury-members', views.backend_jurymembers, name='backend_jury_members'),
    path('jury-member/add', views.backend_add_jurymember, name='backend_add_jurymember'),
    path('jury-member/<int:mentor_id>update', views.backend_update_jurymember, name='backend_update_jurymember'),

    # Blogpost
    path('blogposts', views.backend_blogposts, name='backend_blogposts'),
    path('blogposts/add', views.backend_add_blogpost, name='backend_add_blogpost'),
    path('blogposts/<int:blogpost_id>update', views.backend_update_blogpost, name='backend_update_blogpost'),

    # Blogpost
    path('homepage_sections', views.backend_homepage_sections, name='backend_homepage_sections'),
    path('homepage_sections/<int:homepage_section_id>update', views.backend_update_homepage_section,
         name='backend_update_homepage_section'),

    # Collaborations
    path('collaborations', views.backend_partners, name='backend_collaborations'),
    path('collaborations/add', views.backend_add_partner, name='backend_add_collaboration'),
    path('collaborations/<int:collaboration_id>update', views.backend_update_partner,
         name='backend_update_collaboration'),

    # Interior exhibitions
    path('interior-exhibitions', views.backend_interior_exhibitions, name='backend_interior_exhibitions'),
    path('interior-exhibitions/add', views.backend_add_interior_exhibition, name='backend_add_interior_exhibition'),
    path('interior-exhibitions/<int:interior_exhibition_id>update', views.backend_update_interior_exhibition,
         name='backend_update_interior_exhibition'),

    # Fashion Shows
    path('fashion-shows', views.backend_fashion_shows, name='backend_fashion_shows'),
    path('fashion-shows/add', views.backend_add_fashion_show, name='backend_add_fashion_show'),
    path('fashion-shows/<int:fashion_show_id>update', views.backend_update_fashion_show,
         name='backend_update_fashion_show'),

    # Inhouse Mentors
    path('inhouse-mentors', views.backend_inhouse_mentors, name='backend_inhouse_mentors'),
    path('inhouse-mentors/add', views.backend_add_inhouse_mentor, name='backend_add_inhouse_mentor'),
    path('inhouse-mentors/<int:inhouse_mentor_id>update', views.backend_update_inhouse_mentor,
         name='backend_update_inhouse_mentor'),

    # Courses
    path('courses', views.backend_courses, name='backend_courses'),
    path('courses/add', views.backend_add_course, name='backend_add_course'),
    path('courses/<int:course_id>update', views.backend_update_course, name='backend_update_course'),

    # Career options
    path('career-options', views.backend_course_career_options, name='backend_course_career_options'),
    path('career-options/add', views.backend_add_course_career_option, name='backend_add_course_career_option'),
    path('career-options/<int:career_option_id>update', views.backend_update_course_career_option,
            name='backend_update_course_career_option'),
]
