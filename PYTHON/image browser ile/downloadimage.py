import urllib.request
#downloading image from the internet
try:
    #url = "file:///E://Urja//Urja_LJ_Docs//LJKU_MCA-Sem-2//Material//Network Programming//camel.jpg"
    url = "https://media.istockphoto.com/photos/desert-camel-with-two-jumps-waking-in-the-sand-picture-id154902311"
    #url= "https://media.istockphoto.com/photos/tiger-portrait-picture-id949472768?s=612x612"
    download = urllib.request.urlretrieve(url,"camel.jpg")
    print("Image downloaded successfully")
except Exception as ex:
    print(ex)   

