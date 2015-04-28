from django.conf.urls import patterns, include, url
from sigegov import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^authorize_user/(?P<userID>\S+)/$',views.authorize_user,name='authorize_user'),
    url(r'^user_details/(?P<userID>\S+)/$',views.user_details,name='user_details'),
    url(r'^not_authorized/$',views.not_authorized,name='not_authorized'),
    url(r'^view_publication/(?P<pubID>\S+)/$',views.view_publication,name='view_publication'),
    url(r'^process_upvote/(?P<pubID>\S+)/$',views.process_upvote,name='process_upvote'),
    url(r'^process_downvote/(?P<pubID>\S+)/$',views.process_downvote,name='process_downvote'),
    url(r'^view_statewise/$',views.view_statewise,name='view_statewise'),
    url(r'^publications/$',views.publications,name='publications'),
    url(r'^publications/(?P<stateID>\S+)/$',views.publications,name='publications'),
    url(r'^send_email_sigegov/(?P<page_path>\S+)/$',views.send_email_sigegov,name='send_email_sigegov'),
    url(r'^enter_data/$',views.enter_data,name='enter_data'),
    url(r'^create_event/$',views.create_event,name='create_event'),

    url(r'^view_request_thanks/(?P<requestID>\S+)/$',views.view_request_thanks,name='view_request_thanks'),
    url(r'^view_request/(?P<requestID>\S+)/$',views.view_request,name='view_request'),
    url(r'^requestblood_form/$',views.requestblood_form,name='requestblood_form'),
    url(r'^requestblood_thanks/$',views.requestblood_thanks,name='requestblood_thanks'),
    url(r'^donate_blood/$', views.donate_blood, name='donate_blood'),
    url(r'^donateblood_thanks/$',views.donateblood_thanks,name='donateblood_thanks'),
    url(r'^donor_list/$',views.donor_list,name='donor_list'),
    url(r'^send_email1/$',views.send_email1,name='send_email1'),
    url(r'^bloodcamp_list/$',views.bloodcamp_list,name='bloodcamp_list'),
	url(r'^main/$',views.main, name='main'),
    url(r'^bloodcamp/$',views.bloodcamp,name='bloodcamp'),
    url(r'^camps_detail/$',views.camps_detail,name='camps_detail'),
    url(r'^camp_donate/(?P<campID>\S+)$',views.camp_donate,name='camp_donate'),
    url(r'^bloodcamp_form/$',views.bloodcamp_form,name='bloodcamp_form'),
    url(r'^bloodcamp_form_thanks/$',views.bloodcamp_form_thanks,name='bloodcamp_form_thanks'),

    url(r'^drive_list/(?P<driveID>\S+)/$',views.drive_list,name='drive_list'),
    url(r'^camp_post/(?P<campID>\S+)/$',views.camp_post,name='camp_post'),
    url(r'^store_camp_post/(?P<campID>\S+)/$',views.store_camp_post,name='store_camp_post'),
 

    url(r'^drive/$', views.drive, name='drive'),

    url(r'^donor/$', views.donor, name='donor'),
    url(r'^hospital/$', views.hospital, name='hospital'),
    url(r'^recepient/$', views.recepient, name='recepient'),
    url(r'^camp/$', views.camp, name='camp'),
    url(r'^link/$', views.link, name='link'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^share/$', views.share, name='share'),
    url(r'^view_story/(?P<story_id>\S+)/$', views.view_story, name='view_story'),
    url(r'^putstory/$',views.putstory,name='putstory'),
    url(r'^putstory_thanks/$',views.putstory_thanks,name='putstory_thanks'),
	url(r'^faqs/$',views.faqs,name='faqs'),
	url(r'^feedback/$',views.feedback,name='feedback'),
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^about/$',views.about,name='about'),
	url(r'^home/$',views.home,name='home'),
	url(r'^todaycamp/$',views.todaycamp,name='todaycamp'),
	url(r'^autocomplete/$',views.autocomplete,name='autocomplete'),
    url(r'^search/$',include('haystack.urls')),
]

