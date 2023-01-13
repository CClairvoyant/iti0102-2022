"""API task."""

from __future__ import print_function

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient.discovery
import googleapiclient.errors
from time import perf_counter


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    # If modifying these scopes, delete the file token.json.
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = None
    list_of_links = []
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id,
                                    range="A:A").execute()
        values = result.get('values')

        if not values:
            return []

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            list_of_links.append("".join(row))
        return list_of_links

    except HttpError as err:
        print(err)


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    video_links = []

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=link.split("=")[-1],
        maxResults=50
    )
    response = request.execute()

    for i in range(len(response["items"])):
        video_links.append("https://www.youtube.com/watch?v=" + response["items"][i]["contentDetails"]["videoId"])

    while "nextPageToken" in response:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=link.split("=")[-1],
            maxResults=50,
            pageToken=response["nextPageToken"]
        )
        response = request.execute()
        for i in range(len(response["items"])):
            video_links.append("https://www.youtube.com/watch?v=" + response["items"][i]["contentDetails"]["videoId"])

    return video_links


if __name__ == '__main__':
    with open("developer_key.txt", "r") as file:
        developer_key = file.read()
    start = perf_counter()
    video_links = get_links_from_playlist(
        "https://www.youtube.com/watch?v=7MysgX9vv48&list=PL3tRBEVW0hiBSFOFhTC5wt75P2BES0rAo", developer_key)
    end = perf_counter()
    print(video_links)

    print(f"Fetching {len(video_links)} video links took {end - start} seconds.")

    # print(get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json'))
