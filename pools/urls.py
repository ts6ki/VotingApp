from django.urls import path

from pools.views import (
    index,
    # hello,
    # hello_shivam,
    delete,
    create_question,
    update,
    update_one,
    create_choice,
    choice_detail_view,
    choice_update_view,
    choice_delete_view,
    choice_list_view,
    question_detail,
)

urlpatterns = [
    path("", index),
    path("delete/", delete),
    path("create/", create_question),
    path("update/", update),
    path("update_one/<str:qid>", update_one),
    # path("hello/shivam", hello_shivam),
    # path("hello/<str:first_name>", hello),
    path("choice/create/<int:q_id>/", create_choice),
    path("choice/<int:id>/", choice_detail_view),
    path("choice/<int:id>/update/", choice_update_view),
    path("choice/<int:id>/delete/", choice_delete_view),
    path("choices/<int:question_id>/", choice_list_view),

    path("detail/<str:qid>", question_detail)
]
