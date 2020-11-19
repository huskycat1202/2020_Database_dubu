from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    #main
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('rooms',views.rooms,name="rooms"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),

    #admin
    path('admin/login',admin_views.adminLogin,name="admin_login"),
    path('admin/logout',admin_views.adminLogout,name="admin_logout"),
    path('admin/manage_depart',admin_views.manage_depart,name="manage_depart"),
    path('admin/manage_staff',admin_views.manage_staff,name="manage_staff"),

    #tool
    path('admin/manage_staff/del',admin_views.delete_staff,name="delete_staff"),
    path('admin/manage_staff/add',admin_views.insert_staff,name="insert_staff"),
    path('admin/manage_staff/edit',admin_views.edit_staff,name="edit_staff"),
    path('admin/manage_staff/add_work',admin_views.insert_staff_working,name="insert_staff_working"),
    path('admin/manage_staff/del_work',admin_views.delete_staff_working,name="delete_staff_working"),
    path('admin/manage_staff/add_holi',admin_views.insert_staff_holiday,name="insert_staff_holiday"),
    path('admin/manage_staff/del_holi',admin_views.delete_staff_holiday,name="delete_staff_holiday"),
    path('admin/staff/change_status',admin_views.change_staff_status,name="change_staff_status"),

    # front admin
    path('admin/staff',admin_views.staff,name="staff"),
    path('admin/s_reservation',admin_views.s_reservation,name="s_reservation"),
    path('admin/room_select',admin_views.room_select,name="room_select"),
    path('admin/parking',admin_views.parking,name="parking"),
    path('admin/product',admin_views.product,name="product"),
    path('admin/engineer',admin_views.engineer,name="engineer"),
    path('admin/staff_search',admin_views.staff_search,name="staff_search"),

]