from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('video_list/',views.videolist,name='video'),
    path('delete/<int:id>',views.delete,name="delete"),
    path('upload/',views.upload,name='upload'),
    path('search/',views.search,name='search'),
    path('uploadshorts/',views.uploadshorts,name='uploadshorts'),
    path('shorts/',views.shorts,name='shorts'),
    path('deleteshort/<int:id>',views.deleteshort,name='deleteshort'),
    path('exit/',views.exit,name='exit'),
    path('help/',views.help,name='help'),
    path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
path('feedback/',views.feedback,name='feedback')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

