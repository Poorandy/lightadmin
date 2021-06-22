# -*- coding:utf-8 -*-

"""
@File      : urls.py
@Copyright : hsmap.com
@Author    : Andy Wu
@Date      : 2021/6/22
@Desc      :
"""

from django.urls import path, re_path
from apps.simc import views

urlpatterns = [
    path('character/', views.CharacterView.as_view()),
    path('card/', views.CardView.as_view()),
    path('monster/', views.MonsterView.as_view()),
    path('battle/', views.BattleSimc.as_view()),
    path('combat/', views.BattleView.as_view()),
    path('combat_check/', views.BattleIsExist.as_view()),
]
