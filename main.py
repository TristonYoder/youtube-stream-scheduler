import os
import google.oauth2.credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define your stream details
stream_title = "Your Stream Title"
stream_description = "Your Stream Description"
playlist_id = "YOUR_PLAYLIST_ID"  # Replace with your playlist ID
stream_key = "YOUR_STREAM_KEY"  # Replace with your stream key

# Set the scheduled start time as a variable (in ISO 8601 format)
scheduled_start_time = "2024-01-21T12:00:00Z"

# Set your API key or service account credentials file path here
API_KEY = "YOUR_API_KEY"
SERVICE_ACCOUNT_FILE = "your-service-account-file.json"  # Replace with the path to your service account JSON file
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Initialize the YouTube API client
credentials = None

if SERVICE_ACCOUNT_FILE:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
else:
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_file(
        "your-oauth2-credentials.json", SCOPES
    )

youtube = build("youtube", "v3", credentials=credentials)

# Create a live broadcast
live_broadcast = youtube.liveBroadcasts().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": stream_title,
            "description": stream_description,
            "scheduledStartTime": scheduled_start_time,
        },
        "status": {
            "privacyStatus": "unlisted",  # You can change this to "private" or "public"
        },
    },
).execute()

# Create a live stream
live_stream = youtube.liveStreams().insert(
    part="snippet",
    body={
        "snippet": {
            "title": stream_title,
            "description": stream_description,
        },
    },
).execute()

# Bind the live broadcast and stream
youtube.liveBroadcasts().bind(
    part="id,contentDetails",
    id=live_broadcast["id"],
    streamId=live_stream["id"],
).execute()

# Add the live broadcast to the playlist
youtube.playlistItems().insert(
    part="snippet",
    body={
        "snippet": {
            "playlistId": playlist_id,
            "position": 0,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": live_broadcast["id"],
            },
        },
    },
).execute()

print("Stream" + stream_title + " Created Successfully!")
