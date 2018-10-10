GW Services Code

The current urls will return the content as described in a json file
## **""** => 
returns nothing, a loading page telling you to enter a proper url as an endpoint
##**"media"** => 
returns nothing, a loading page telling you to enter a proper url as an endpoint
##**"media/getAllImages"** => 
grabs ALL images that are being stored in the raw bucket
##**"media/getAllVideos"** => 
grabs ALL videos that are being stored in the raw bucket
##**"media/getAllUserImages/{{user_id_of_who_you_want_to_grab}}"** => 
grabs ALL images that are being stored in the raw bucket as well as the edited bucket
##**"media/getAllUserVideos/{{user_id_of_who_you_want_to_grab}}"** => 
grabs ALL videos that are being stored in the raw bucket as well as the edited bucket
##**"media/getAllEvents"** => 
grabs ALL events from mysql database
##**"media/getSpecificEvent/{{event_id_of_which_event_you_want_to_grab}}"** => 
grabs a specific event from the mySQL database with all of the details about the event as well as all of the content that is associated with that event
## **"media/getAllImagesUserEvent/{{user_id_of_who_you_want_to_grab}}/{{event_id_of_which_event_you_want_to_grab}}"** => 
grabs all images for a specific user at a specific event
##**"media/getAllVideosUserEvent/{{user_id_of_who_you_want_to_grab}}/{{event_id_of_which_event_you_want_to_grab}}"** => 
grabs all videos for a specific user at a specific event
##**"media/updateDatabase"** => 
Initializing/updating the database. Only to be used once at the very beginning of launching the website to transfer all of the existing files that are stored in the s3 database but not yet tracked in the sql database specific to the api that we are using. Once the api is able to continually update the sql database every time an image is uploaded this function will never have to be run again