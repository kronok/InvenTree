from django.conf.urls import url, include

from . import views

""" URL patterns associated with project
/project/<pk>       -> Detail view of single project
/project/<pk>/parts -> Detail all parts associated with project
"""
projectdetailpatterns = [
    # Single project detail
    url(r'^$', views.ProjectDetail.as_view()),
]

projectpartpatterns = [
    # Detail of a single project part
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectPartDetail.as_view()),

    # Parts associated with a project
    url(r'^\?[^/]*/$', views.ProjectPartsList.as_view()),

    # All project parts
    url(r'^$', views.ProjectPartsList.as_view()),
]

projectcategorypatterns = [
    # List of top-level project categories
    url(r'^$', views.ProjectCategoryList.as_view()),

    # Detail of a single project category
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectCategoryDetail.as_view()),

    # Create a new category
    url(r'^new/$', views.NewProjectCategory.as_view())
]

urlpatterns = [

    # Individual project URL
    url(r'^(?P<pk>[0-9]+)/', include(projectdetailpatterns)),

    # List of all projects
    url(r'^$', views.ProjectList.as_view()),

    # Project parts
    url(r'^parts/', include(projectpartpatterns)),

    # Project categories
    url(r'^category/', include(projectcategorypatterns)),
]
