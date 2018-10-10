from django.shortcuts import render, HttpResponse
import bcrypt, sys, os, base64, datetime, hashlib, hmac 
import boto3, csv, json
from django.db import models
from .models import User, Device, Event, Media
client = boto3.client('s3') #low-level functional API
resource = boto3.resource('s3') #high-level object-oriented API
v1_raw_bucket = resource.Bucket('pi-1')
v1_edited_bucket = resource.Bucket('pi-2')
v2_raw_bucket = resource.Bucket('pi-4')
v2_edited_bucket = resource.Bucket('pi-5') 

# Initializing the database 
# Only to be used once at the very beginning of launching the website to transfer all of the 
# existing files that are stored in the s3 database but not yet tracked in the sql database specific
# to the api that we are using
# Once the api is able to continually update the sql database every time an image is uploaded 
# this function will never have to be run again
def updateDatabase(request):
    thisUsersContentRaw = v2_raw_bucket.objects.filter()
    thisUsersContentEdited = v2_edited_bucket.objects.filter()
    if (User.objects.filter(id = 1)):
        print("user 1 exists")
    else:
        User.objects.create(
            first_name = "glimpse",
            last_name = "project",
            email = "drose@glimpsewearables.com",
            phone = "5094818244",
            password = "password",
            created_at = datetime.time,
            updated_at = datetime.time
        )
    if(Device.objects.filter(id = 1)):
        print("device 1 exists")
    else:
        Device.objects.create(
            device_number = 1,
            serial_number = "1a2b3c4d5e6f7g",
            UserId = User.objects.get(id=1)
        )
    if(Event.objects.filter(id = 1)):
        print("Event 1 exists")
    else:
        Event.objects.create(
            name = "glimpsewearables concert",
            lat = 47.6062,
            long = 122.3321,
            address = "4637 21st Ave NE",
        )
    # This function is the most important for updating the database, checking to see if all of the images
    # that are in the s3 database are accounted for in the sql database
    for data in thisUsersContentRaw:
        if Media.objects.filter(url_link = data.key):
            print(data.key + "data.key already exists")
        else:
            # If else statement that helps decide whether or not this media type is a image or video
            Media.objects.create(
                media_type = "image",
                url_link = data.key,
                DeviceId = Device.objects.last(),
                UserId = User.objects.last(),
                event = Event.objects.last(),
                raw_or_edited = "raw"
            )
            print("adding new edited media with " + data.key + " as a the url_link")
    # This function is the most important for updating the database, checking to see if all of the images
    # that are in the s3 database are accounted for in the sql database
    for data in thisUsersContentEdited:
        if Media.objects.filter(url_link = data.key):
            print(data.key + "data.key already exists")
        else:
            # If else statement that helps decide whether or not this media type is a image or video
            # Reuse this function for adding image to database every time a new image is uploaded to the s3 database
            Media.objects.create(
                media_type = "image",
                url_link = data.key,
                DeviceId = Device.objects.last(),
                UserId = User.objects.last(),
                event = Event.objects.last(),
                raw_or_edited = "edited"
            )
            print("adding new edited media with " + data.key + " as a the url_link")
    return HttpResponse(thisUsersContentRaw)



# All of the endpoints for pushing information from the api call
# functions divider
# functions divider
# functions divider
def createEvent():
    print("creating a new event")
def updateEvent():
    print("updating an existing event")
def createSingleMedia():
    print("creating a single media object")
def updateSingleMedia():
    print("updating attributes of a single event")




# All of functions for creating users and managing user information

# functions divider
# functions divider
# functions divider

# def createUser(request):
#     if request.method=="POST":
#         errors = User.objects.basic_validator(request.POST)
#         if len(errors):
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/registerLoginPage', errors)
#         else:
#             imgCount = 0
#             vidCount = 0
#             device_number = request.POST['deviceNumber']
#             bucket_select = "user" + device_number
#             bucket_images = bucket_select + "/images"
#             bucket_videos = bucket_select + "/videos"
#             throw_images = bucket_images + "/"
#             throw_videos = bucket_videos + "/"
#             this_users_images = test_bucket.objects.filter(Prefix=bucket_images)
#             this_users_videos = test_bucket.objects.filter(Prefix=bucket_videos)
#             newEmail = request.POST['usersEmail']
#             print(newEmail.lower())
#             User.objects.create(full_name=request.POST['usersName'], email_address=newEmail.lower(), phone_number=request.POST['usersPhone'], number_pics = imgCount, number_vids = vidCount, device_key_name=request.POST['deviceNumber'])
#             last_user = User.objects.last()
#             request.session['user_id'] = last_user.id
#             Device.objects.create(device_owner = User.objects.get(device_key_name = device_number), device_key_name = "SerialNumber", number_pics = imgCount, number_vids = vidCount)
#             user_with_id = User.objects.get(id=request.session['user_id'])
#             return redirect('/userPage')
#     return redirect('/')



# All of functions for creating events and managing event information

# functions divider
# functions divider
# functions divider

# def createEvent(request):
#     if isLoggedIn() == "false":
#         return redirect("")
#     if request.method == "POST":
#         errors = Event.objects.basic_validator(request.POST)
#         print(errors)
#         if len(errors):
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/godMode', errors)
#         else:
#             Event.objects.create(name=request.POST['eventName'], venue_name=request.POST['venueName'], address=request.POST['address'], start_date=request.POST['startDate'], end_date=request.POST['endDate'])
#     return redirect("/godMode")


# All of functions for logging in users and keeping track of their information

# functions divider
# functions divider
# functions divider
# def login(request):
#     if request.method == "POST":
#         errors = User.objects.login_validator(request.POST)
#         if len(errors):
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/registerLoginPage', errors)
#         checkEmail = request.POST['emailsLogin']
#         passEmail = checkEmail.lower()
#         if User.objects.filter(email_address=passEmail):
#             user = User.objects.get(email_address=passEmail)
#             if user.device_key_name == request.POST['deviceNumber']:
#                 request.session['user_id'] = user.id
#                 return redirect('/userPage')
#     return redirect('/')




# All of the endpoints for retrieving information from the api call
# functions divider
# functions divider
# functions divider
def index(request): # this is the standard endpoint that will not return anything
    response = "here is the standard page that will be seen when the user enters the blank url"
    return HttpResponse(response)
def mediaHome(request):
    response = "here is the home page from the media application portion of the api"
    return HttpResponse(response)
def getAllImages(request): # grabs ALL images that are being stored in the raw bucket
    response = "Getting all images"
    context = {}
    all_images = Media.objects.filter(media_type = "image")
    context["all_images"] = all_images
    newContext = json.dumps(context)
    return HttpResponse(newContext)

def getAllVideos(request): # grabs ALL videos that are being stored in the raw bucket
    response = "Getting all videos"
    context = {}
    all_videos = Media.objects.filter(media_type = "video")
    context["all_videos"] = all_videos
    newContext = json.dumps(context)
    return HttpResponse(newContext)

def getAllUserImages(request, user_id): # grabs ALL images connected to the specific user that are being stored in the raw bucket
    context = {}
    if User.objects.filter(id = user_id):
        response = "Getting all images specific to user " + user_id + "..!! "
        raw_images = Media.objects.filter(UserId = User.objects.get(id=user_id), media_type = "image", raw_or_edited = "raw")
        edited_images = Media.objects.filter(UserId = User.objects.get(id=user_id), media_type = "image", raw_or_edited = "edited")
        context["raw_images"] = raw_images
        context["edited_images"] = edited_images
        
    else:
        context["error"] = "You entered a user that does not exist"
    newContext = json.dumps(context)
    return HttpResponse(newContext)

def getAllUserVideos(request, user_id): # grabs ALL videos connected to the specific user that are being stored in the raw bucket
    context = {}
    if User.objects.filter(id = user_id):
        response = "Getting all videos specific to a user..."
        videos_raw = getUserContentFromDataBase(user_id, "video", "raw")
        videos_edited = getUserContentFromDataBase(user_id, "video", "edited")
        context["videos_raw"] = videos_raw
        context["images_raw"] = images_raw
    else:
        context["error"] = "You entered a user that does not exist"
    context.json()
    return HttpResponse(context)

def getAllEvents(request): # grabs ALL events from mysql database
    response = "Getting all events that have been created"
    context = {}
    all_events = Event.objects.all()
    all_images = Media.objects.filter(media_type = "image")
    all_videos = Media.objects.filter(media_type = "video")
    context["all_events"] = all_events
    context["all_images"] = all_images
    context["all_videos"] = all_videos
    context.json()
    return HttpResponse(context)

def getSpecificEvent(request, event_id): # grabs a specific event from the mySQL database
    context = {}
    if Event.objects.filter(id = event_id):
        response = "Getting a single specific event with a event id of"
        context = {}
        this_event = Event.objects.get(id = event_id)
        this_event_content = Media.objects.filter(event = Event.objects.get(id=event_id))
        context["this_event"] = this_event
        context["this_event_content"] = this_event_content
    else:
        context["error"] = "You entered a event that does not exist"
    context.json()
    return HttpResponse(context)

def getAllImagesUserEvent(request, user_id, event_id): # grabs all images for a specific user at a specific event
    context = {}
    if Event.objects.filter(id = event_id) and User.objects.filter(id = user_id):
        response = "Getting all images for a single user at a specific event with a event id of" + event_id
        user_event_content = Media.objects.filter(event = Event.objects.get(id=event_id), UserId = User.objects.get(id=user_id), media_type="image")
        context["user_event_content"] = user_event_content
    else:
        context["error"] = "You entered a user or event that does not exist"
    context.json()
    return HttpResponse(context)

def getAllVideosUserEvent(request, user_id, event_id): # grabs all videos for a specific user at a specific event
    context = {}
    if Event.objects.filter(id = event_id) and User.objects.filter(id = user_id):
        response = "Getting all videos for a single user at a specific event with a event id of" + event_id
        user_event_content = Media.objects.filter(event = Event.objects.get(id=event_id), UserId = User.objects.get(id=user_id), media_type="video")
        context["user_event_content"] = user_event_content
    else:
        context["error"] = "You entered a user or event that does not exist"
    context.json()
    return HttpResponse(context)
