from django.urls import path
from . views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,

	Level1services,
    Level1infrustructure,
	Level1mandatory,
    Level1personels,

    Level2services,
    Level2infrustructure,
	Level2mandatory,
    Level2personels,

    Level3services,
    Level3infrustructure,
	Level3mandatory,
    Level3personels,

	Level4services,
    Level4admin,
    Level4infrustructure,
	Level4mandatory,
    Level4personels,

    Level5services,
    Level5infrustructure,
	Level5mandatory,
    Level5personels,
	)

from . import views





urlpatterns = [
path('',PostListView.as_view(), name='blog-home'),
path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
path('post/new/',PostCreateView.as_view(), name='post-create'),
path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
path('about/',views.about, name='blog-about'),

path('level1services/', views.Level1services, name='level1-services'),
path('level1infrus/', views.Level1infrustructure, name='level1-infrustructure'),
path('level1mandat/', views.Level1mandatory, name = 'level1-mandatory'),
path('level1persons/', views.Level1personels, name='level1-personels'),


path('level2services/', views.Level2services, name='level2-services'),
path('level2infrus/', views.Level2infrustructure, name='level2-infrustructure'),
path('level2mandat/', views.Level2mandatory, name = 'level2-mandatory'),
path('level2persons/', views.Level2personels, name='level2-personels'),

path('level3services/', views.Level3services, name='level3-services'),
path('level3infrus/', views.Level3infrustructure, name='level3-infrustructure'),
path('level3mandat/', views.Level3mandatory, name = 'level3-mandatory'),
path('level3persons/', views.Level3personels, name='level3-personels'),


path('level4services/', views.Level4services, name='level4-services'),
path('level4admin/', views.Level4admin, name='level4admin-unit'),
path('level4infrus/', views.Level4infrustructure, name='level4-infrustructure'),
path('level4mandat/', views.Level4mandatory, name = 'level4-mandatory'),
path('level4persons/', views.Level4personels, name='personnels'),


path('level5services/', views.Level5services, name='level5-services'),
path('level5infrus/', views.Level5infrustructure, name='level5-infrustructure'),
path('level5mandat/', views.Level5mandatory, name = 'level5-mandatory'),
path('level5persons/', views.Level5personels, name='level5-personels'),

]