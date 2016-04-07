import requests
import json
import random

TOKEN = $FACEBOOK_ACCESS_TOKEN
#	^ put your facebook access token here
reply = ['Thank you very much :D']

def get_birthday_feed():
  init_url = 'https://graph.facebook.com/me/feed?access_token=' + TOKEN
  
  flag = True
  while(flag):
    result = json.loads((requests.get(init_url)).text)
    #print result
    for i in range(0, len(result['data'])):
      print result['data'][i]['from']['name'] + " : " + result['data'][i]['message']
      print "(R)eply, (n)ext or (e)xit?"
      user_response = str(raw_input())
      if user_response == 'R' or user_response == 'r':
        # comment
        comment = reply[random.randint(0, len(reply)-1)]
        print "Replying With : " + comment
        r = requests.post("https://graph.facebook.com/" + result['data'][i]['id'].split("_")[1] + "/comments?access_token=" + TOKEN + "&message=" + comment)
        #like
        r = requests.post("https://graph.facebook.com/" + result['data'][i]['id'].split("_")[1] + "/likes?access_token=" + TOKEN)
        print r
        # send a post
      elif user_response == 'n' or user_response == "N":
        print "Skipping this guy"
      elif user_response == "e" or user_response == "E":
        print "Exiting"
        flag = False
        break
      else:
        print "No valid input"
      
    # get next set of data
    init_url = result['paging']['next']

# execute main
if __name__ == '__main__':
  get_birthday_feed()

