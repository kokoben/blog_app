from django.conf.urls import url, include
from . import views

app_name= 'posts'

# /posts/?
extra_patterns = [
	url(r'^$', views.index, name='index'),
	# /posts/2 <-- post #2 for a given user
	url(r'^(?P<post_number>\d+)/$', views.displayPost, name='display-post'),
        url(r'^reply/(?P<comment_number>\d+)/$', views.handleReply, name='handle-reply'),
        url(r'^delete/(?P<post_number>\d+)/$', views.deletePost, name='delete-post')
]

urlpatterns = [
	url(r'^$', views.UserRedirectView.as_view()),
	url(r'^posts/', include(extra_patterns)),
	url(r'^archive/$', views.archive, name='archive'),
]

