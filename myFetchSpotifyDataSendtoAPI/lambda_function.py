import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('lambda')
    
    print(event)  #log events

    # Dictionary with country names and corresponding top50 chart playlist IDs.
    playlists_dict = {
    'Global': '37i9dQZEVXbMDoHDwVN2tF',  # Global
    'Argentina': '37i9dQZEVXbMMy2roB9myp',  # Argentina
    'Australia': '37i9dQZEVXbJPcfkRz0wJ0',  # Australia
    'Austria': '37i9dQZEVXbKNHh6NIXu36',  # Austria
    'Belgium': '37i9dQZEVXbJNSeeHswcKB',  # Belgium
    'Bolivia': '37i9dQZEVXbJqfMFK4d691',  # Bolivia
    'Brazil': '37i9dQZEVXbMXbN3EUUhlg',  # Brazil
    'Bulgaria': '37i9dQZEVXbNfM2w2mq1B8',  # Bulgaria
    'Canada': '37i9dQZEVXbKj23U1GF4IR',  # Canada
    'Chile': '37i9dQZEVXbL0GavIqMTeb',  # Chile
    'Colombia': '37i9dQZEVXbOa2lmxNORXQ',  # Columbia
    'Costa Rica': '37i9dQZEVXbMZAjGMynsQX',  # Costa Rica
    'Czech Republic': '37i9dQZEVXbIP3c3fqVrJY',  # Czech Republic
    'Denmark': '37i9dQZEVXbL3J0k32lWnN',  # Denmark
    'Dominican Republic': '37i9dQZEVXbKAbrMR8uuf7',  # Dominican Republic
    'Ecuador': '37i9dQZEVXbJlM6nvL1nD1',  # Ecuador
    'El Salvador': '37i9dQZEVXbLxoIml4MYkT',  # El Salvador
    'Estonia': '37i9dQZEVXbLesry2Qw2xS',  # Estonia
    'Finland': '37i9dQZEVXbMxcczTSoGwZ',  # Finland
    'France': '37i9dQZEVXbIPWwFssbupI',  # France
    'Germany': '37i9dQZEVXbJiZcmkrIHGU',  # Germany
    'Greece': '37i9dQZEVXbJqdarpmTJDL',  # Greece
    'Guatemala': '37i9dQZEVXbLy5tBFyQvd4',  # Guatemala
    'Honduras': '37i9dQZEVXbJp9wcIM9Eo5',  # Honduras
    'Hong Kong': '37i9dQZEVXbLwpL8TjsxOG',  # Hong Kong
    'Hungary': '37i9dQZEVXbNHwMxAkvmF8',  # Hungary
    'Iceland': '37i9dQZEVXbKMzVsSGQ49S',  # Iceland
    'India': '37i9dQZEVXbLZ52XmnySJg',  # India
    'Indonesia': '37i9dQZEVXbObFQZ3JLcXt',  # Indonesia
    'Ireland': '37i9dQZEVXbKM896FDX8L1',  # Ireland
    'Israel': '37i9dQZEVXbJ6IpvItkve3',  # Israel
    'Italy': '37i9dQZEVXbIQnj7RRhdSX',  # Italy
    'Japan': '37i9dQZEVXbKXQ4mDTEBXq',  # Japan
    'Latvia': '37i9dQZEVXbJWuzDrTxbKS',  # Latvia
    'Lithuania': '37i9dQZEVXbMx56Rdq5lwc',  # Lithuania
    'Luxembourg': '37i9dQZEVXbKGcyg6TFGx6',  # Luxembourg
    'Malaysia': '37i9dQZEVXbJlfUljuZExa',  # Malaysia
    'Mexico': '37i9dQZEVXbO3qyFxbkOE1',  # Mexico
    'Netherlands': '37i9dQZEVXbKCF6dqVpDkS',  # Netherlands
    'New Zealand': '37i9dQZEVXbM8SIrkERIYl',  # New Zealand
    'Nicaragua': '37i9dQZEVXbISk8kxnzfCq',  # Nicaragua
    'Norway': '37i9dQZEVXbJvfa0Yxg7E7',  # Norway
    'Panama': '37i9dQZEVXbKypXHVwk1f0',  # Panama
    'Paraguay': '37i9dQZEVXbNOUPGj7tW6T',  # Paraguay
    'Peru': '37i9dQZEVXbJfdy5b0KP7W',  # Peru
    'Philippines': '37i9dQZEVXbNBz9cRCSFkY',  # Philippines
    'Poland': '37i9dQZEVXbN6itCcaL3Tt',  # Poland
    'Portugal': '37i9dQZEVXbKyJS56d1pgi',  # Portugal
    'Romania': '37i9dQZEVXbNZbJ6TZelCq',  # Romania
    'Singapore': '37i9dQZEVXbK4gjvS1FjPY',  # Singapore
    'Slovakia': '37i9dQZEVXbKIVTPX9a2Sb',  # Slovakia
    'South Africa': '37i9dQZEVXbMH2jvi6jvjk',  # South Africa
    'Spain': '37i9dQZEVXbNFJfN1Vw8d9',  # Spain
    'Sweden': '37i9dQZEVXbLoATJ81JYXz',  # Sweden
    'Switzerland': '37i9dQZEVXbJiyhoAPEfMK',  # Switzerland
    'Taiwan': '37i9dQZEVXbMnZEatlMSiu',  # Taiwan
    'Thailand': '37i9dQZEVXbMnz8KIWsvf9',  # Thailand
    'Turkey': '37i9dQZEVXbIVYVBNw9D5K',  # Turkey
    'United Kingdom': '37i9dQZEVXbLnolsZ8PSNw',  # United Kingdom
    'United States': '37i9dQZEVXbLRQDuF5jeBp',  # United States
    'Uruguay': '37i9dQZEVXbMJJi3wgRbAy',  # Uruguay
    'Vietnam': '37i9dQZEVXbLdGSmz6xilI',  # Vietnam
    }
    
    if event["op"] == "init":  #first lambda invocation
        print("init")
        for country, playlist_id in playlists_dict.items():  #loop over countries
            response = client.invoke(  ##invoke itself and parse country and playlistID as a payload
                FunctionName='myFetchSpotifyDataSendtoAPI',
                InvocationType='Event',
                ClientContext='',
                Payload=json.dumps({
                                    "op": "fetch_country", 
                                    "params": {
                                        "country": country,
                                        "playlist_id": playlist_id
                                    }}).encode(),
                Qualifier='$LATEST'
                )
            print(response)
    elif event["op"] == "fetch_country":  
        print("fetch_country")
        #call function that make SpotifyAPI calls and send data to API Gateway
        get_spotify_data(event["params"]["country"], event["params"]["playlist_id"])  
    else:
        print("Invalid op: ", event["op"])
            
if __name__ == "__main__":   
    lambda_handler('', '')
    
def get_spotify_data(country, playlist_id):
    import requests  #to send data to API
    import spotipy  #python library to fetch Spotify data
    from datetime import datetime
    
    # URL of API I have created with AWS API Getway
    URL='https://8ef3kcjkvc.execute-api.us-east-1.amazonaws.com/beta/main'
    
    client_id = "1964d3e09d2640cfa62d7c156acc0cc6"  #removed from this code for security reasons
    client_secret = "56d16e6ba6d845c3b2e2858034f17e20" #removed from this code for secutiry reasons
    
    from spotipy.oauth2 import SpotifyClientCredentials #
    from spotipy import MemoryCacheHandler  
    cache = MemoryCacheHandler()
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret, cache_handler=cache)  #creating Spotify Client Credentials Flow Manager
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  #Creates a Spotify API client
    
    # datetime object containing current date and time
    now = datetime.now()
    weekno = now.isocalendar().week  #pick week number
    year = now.isocalendar().year  #pick year
    
    features_to_pick = ["danceability", "energy", "instrumentalness","tempo", "valence", "mode"]  #audio features to be requested from API

    top50 = sp.playlist_tracks(playlist_id, fields='items.track.id')['items']  #fetching info on top50 playlist
    position = 0  #position within the top50 chart

    for track in top50:  #loop over tracks within a playlist
        position += 1  # this count will go up, indicating position within the top50 chart
        # select features and add them as key-value pair to track's dictionary
        track_dict = {}  # initialize dictionary for track info and audio features
        track_id = track['track']['id']
        track_dict['trackID'] =  track_id  #track_id will be used as primary key for DynamoDB
        track_dict['country'] = country  #country
        track_dict['position'] = position  #position within the chart
        track_dict['year'] = year  #year
        track_dict['weekno'] = weekno  #week number
        track_features=sp.audio_features(track['track']['id'])[0]  #API call to get all audio features
        values_picked=[track_features[k] for k in features_to_pick]  #select features of interest
        for i in range(len(values_picked)):
            track_dict[features_to_pick[i]] = values_picked[i]
            json_string = json.dumps(track_dict)  #convert dicionary to json string
        
        # send data to my API Gateway
        try:
            response = requests.post(URL, data=json_string)
            print(json_string)
            print(response)
        except:
            print("Error occured")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        }
