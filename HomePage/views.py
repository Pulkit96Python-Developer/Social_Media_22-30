from ast import Name
from multiprocessing.dummy import Array
from numbers import Number
from os import uname
from pyexpat import model
from unicodedata import name
from django.shortcuts import render,HttpResponse
from HomePage import models
import json
import sys
from array import *
from django.views.generic import TemplateView
# Create your views here.

def Home(request):
    return render(request,'home.html')

def SignUp(request):
    # obj=models.NewUser.objects.all()
    # for i in range(len(obj)):
    #     obj.delete()
    
    user=models.NewUser()
    
    if request.method=='POST':
        DB_mobile=models.NewUser.objects.values_list("Phone")
        # DB_mobile will hold the list of Mobile nos. stored in the Database
        
        Form_mobile=request.POST.get('Phone')
    # return HttpResponse(str(Form_mobile))
    # user.Phone=Form_mobile
    # user.save()
    # return HttpResponse(str(user.Phone))
    # return HttpResponse("Users Deleted")
    #     # return HttpResponse(request.method+" "+str(Form_mobile))
    #     # return HttpResponse(str(len(DB_mobile)))
        if len(DB_mobile)!=0:
            for i in range(len(DB_mobile)):
                if Form_mobile==str(DB_mobile[i][0]):
                    return HttpResponse("This mobile no. is already used")
            else:
                user.Phone=Form_mobile
                user.Name=request.POST.get('Name')
                user.Password=request.POST.get("Password")
                user.Email=request.POST.get('Email')
                user.No_of_Friends=0
                user.save()
                user_name=models.NewUser.objects.get(Name=request.POST.get('Name'))
                user.DB_ID_of_the_requester=user_name.id
                user.save()
                return render(request,'User_Created.html')
        else:
            user.Phone=Form_mobile
            user.Name=request.POST.get('Name')
            user.Password=request.POST.get("Password")
            user.Email=request.POST.get('Email')
            user.No_of_Friends=0
            user.save()
            return render(request,'User_Created.html')


def SignIn(request):
    return render(request,'SignIn.html')

def User_Authenticate(request):
    if request.method=='POST':
        uname=models.NewUser.objects.values_list('Name')
        mob=models.NewUser.objects.values_list('Phone')
        pwd=models.NewUser.objects.values_list('Password')

        name_form=request.POST.get('Name/Phone')
        pwd_form=request.POST.get('Password')
        validate=False
        num=0
        name=""
        UName_Dictionary=dict()
        for i in range(len(mob)):
            if name_form==str(mob[i][0]):
                for j in range(len(pwd)):
                    if pwd_form==pwd[i][0]:
                        num=mob[i][0]
                        validate=True
                        # return render(request,"UserProfile.html")
        
        for i in range(len(uname)):
            if name_form==str(uname[i][0]):
                # return render(request,"UserProfile.html")
                for j in range(len(pwd)):
                    if pwd_form==pwd[i][0]:
                        name=str(uname[i][0])
                        validate=True
                        # return render(request,"UserProfile.html")
        if validate==True:
            user_validated=models.NewUser.objects.get(Phone=name_form)
            user_id=str(user_validated.id)
            user_validated.DB_ID_of_the_requester=user_validated.id
            user_validated.save()
            li=list()
                # return HttpResponse(str(arr)+str(type(arr[0])))
            for i in range(len(uname)):
                li.append(uname[i][0])
            with open("HomePage/static/USERS.js",'w') as JSONobj:
                data=json.dumps(li)
                JSONobj.write("let data ={}".format(data)+"\nexport{data}")
            if num!=0:
                for val in range(len(mob)):
                    if num==mob[val][0]:
                        name=uname[val][0]
                        UName_Dictionary={'name':name,'user_id':user_id}
            
            elif num==0:
                UName_Dictionary={'name':name,'user_id':user_id}
            return render(request,'UserProfile.html',UName_Dictionary)
            
        elif validate==False:
            return HttpResponse("Invalid Login Credentials")


def SearchResult(request):
    dic=dict()
    id_list=list() #it wil hold the IDs of profiles occured in searched results
    if request.method=='POST':
        li=list()
        users=models.NewUser.objects.values_list('Name')
        user_search=request.POST.get('Search')
        user_name=request.POST.get('name')
        id_of_searcher=request.POST.get('User_ID')
        li=list()
        for i in range(len(users)):
            if len(user_search)<=len(users[i][0]):
                for j in range(len(user_search)-1):
                    if j<len(user_search)-1:
                        if user_search[j].lower()==users[i][0][j].lower():
                            if j+1==len(user_search)-1:
                                if user_search[j+1]==users[i][0][j+1]:
                                    li.append(users[i][0])
                                    ph=models.NewUser.objects.values_list('Phone')[i][0]
                                    id=models.NewUser.objects.get(Phone=ph)
                                    id_list.append(id.id)
                                    break

                            elif j+1==len(user_search)-1:
                                if user_search[j+1]!=users[i][0][j+1]:
                                    break
                            else:
                                continue

                
                    elif user_search[j].lower()!=users[i][0][j].lower():
                        match=False
                        for k in range(len(users[i][0])):
                            if k<=len(users[i][0])-1 and j<=len(user_search)-1:
                                if user_search[j].lower()!=users[i][0][k].lower():
                                    if k==len(users[i][0])-1:
                                        break

                                    else:
                                        continue

                                elif user_search[j].lower()==users[i][0][k].lower():
                                    j+=1
                                    continue
                        else:
                            ph=models.NewUser.objects.values_list('Phone')[i][0]
                            id=models.NewUser.objects.get(Phone=ph)
                            id_list.append(id.id)
                            li.append(users[i][0])
                            break
                    
        print("list of users=",li)
        print("their ID=",id_list)
        
        # combined_dic=dict()
        # for i in range(0,len(li)):
        #     combined_dic[str(id_list[i])]=li[i]
        # dic={'id_and_users_list':combined_dic,'searched_by':user_name}
        # dic2={'k2':'two','k3':'three','k4':'four','k5':'five'}
        # dic1={'k1':dic2}
    # return render(request,'search_result.html',{'list_of_users':li,'list_of_ID':id_list,'Profile_Searched_By':user_name})
    # print(combined_dic)
    # return HttpResponse(str(combined_dic))
    # l2=['1','2','3','4','5']
    # l3=['one','two','three','four','five']
    # combined_list=[['1','one'],['2','two'],['3','three'],['4','four'],['5','five']]
    combined_list=[]
    for i in range(len(id_list)):
        a=id_list[i]
        b=li[i]
        i=[]
        i.append(a)
        i.append(b)
        combined_list.append(i)
    return render(request,'search_result.html',{'combined':combined_list,'Profile_Searched_By':user_name,'id_of_searcher':id_of_searcher})

def Visit_Profile(request,i,searched_by,id_of_searcher):
    user=dict()
    total_friends=0
    searcher_id=id_of_searcher
    # requested_user=i
    requested_user=models.NewUser.objects.get(id=i)
    searched_by_user=searched_by
    if request.method=="GET":
        uname=models.NewUser.objects.values_list('Name')
        U_Friends=models.NewUser.objects.values_list('No_of_Friends')
        for data in range(len(uname)):
            if requested_user.Name==uname[data][0]:
                total_friends=requested_user.No_of_Friends

    user={'Profile_Requested':requested_user.Name, 'ID_Of_Profile_Requested':requested_user.id,'Total_Friends':total_friends,'searched_by':searched_by_user,"searcher_id":searcher_id}
    return render(request,'visit_profile.html',user)


def Friend_Request_Sent(request):
    # return HttpResponse("Friend_Request_Sent function ran")
    if request.method=='POST':
        Request_Sent_By=request.POST.get('Request_Sent_By')
        searcher_id=request.POST.get('searcher_id')
        Request_Sent_To=request.POST.get('Request_Sent_To')
        ID_Of_Profile_Requested=request.POST.get('ID_Of_Profile_Requested')

        obj=models.NewUser.objects.get(id=ID_Of_Profile_Requested)
        obj.Friend_Requests+=1
        obj.save()

        Friend_Req_obj=models.Friend_Requests()
        Friend_Req_obj.Phone=obj
        # Friend_Req_obj.Name=Request_Sent_By
        Friend_Req_obj.save()
        return HttpResponse("Friend Request Sent To "+str(obj.Name)+" "+str(obj)+" "+"request sent by "+str(Friend_Req_obj.DB_ID_of_the_requester.Name))




def Handle_Friend_Request(request,i,searched_by):
    if request.method=='POST':
        request_sent_by=request.POST.get('Request_Sent_By')
        request_sent_to=request.POST.get('Request_Sent_To')
        users=models.NewUser.objects.values_list('Name')
        # Friend_Requests=models.NewUser.objects.values_list('Friend_Requests')
        # objects=models.NewUser.objects.get(Phone=8791168119)
        # objects.Friend_Requests=0
        # print(objects)
        # objects.save()
        return HttpResponse("Got values")
        # for name in range(len(users)):
            # if users[name][0]==request_sent_to:

        #         # print(update_friend_request.Friend_Request)
        #         return HttpResponse(update_friend_request)
                
        # return HttpResponse(str(request_sent_by)+" "+str(request_sent_to)+" "+str(i))



def Test(request):
    objects=models.NewUser.objects.values_list('id')
    print(type(objects))
    print(objects[0])
    print(objects[0][0])
    return HttpResponse(objects)