from django.contrib import admin
from django.urls import path,include
from HomePage import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.Home,name="Home Page"),
    path("SignUp",views.SignUp,name="User_Sign_Up"),
    path("SignIn",views.SignIn,name="User_Sign_In"),
    path('UserProfile',views.User_Authenticate,name="User_Authentication"),
    path('search_result',views.SearchResult,name='Search_Result'),
    path("Visit_Profile/<str:i>/<str:searched_by>/<str:id_of_searcher>",views.Visit_Profile,name="Visit_Profile"),
    path("Test",views.Test,name="Test_Model_Objects"),
    path("Friend_Request_Sent",views.Friend_Request_Sent,name="Friend_Request_Sent")
    # path("Visit_Profile/<str:i>/<str:searched_by>/Friend_Request_Sent",views.Handle_Friend_Request,name="Friend Request Handler"),
]
