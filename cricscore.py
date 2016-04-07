import urllib2, json, time 
# Score set to empty initially.
score = ''

# Run forever
while True:
    # Fetch the url for the specific match.
    response = urllib2.urlopen('http://cricscore-api.appspot.com/csa?id=951347')
    #									^change these id with match you want to monitor
    #To get Id List visit http://cricscore-api.appspot.com/csa 
    # Get the score details from the response json.
    # TODO: Improve the feature to select the match automatically from console itself.
    data = json.load(response)
    new_score = data[0]['de']

    # If score changes, print to console.
    if(new_score != score):
        print new_score
        score = new_score

    # Request API after 2 seconds.
    time.sleep(2)

