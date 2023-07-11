import os
from plexapi.server import PlexServer
from plexapi.exceptions import NotFound

# Load environment variables from file
PLEX_ENV_FILE = "plex-env.txt"
plex_env = {}
with open(PLEX_ENV_FILE, "r") as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            plex_env[key.strip()] = value.strip()

# Get Plex server details from environment variables
plex_url = f"http://{plex_env['PlexIp']}:{plex_env['PlexPort']}"
plex_token = plex_env['PlexToken']

# Prompt the user to enter the playlist ID and target user
playlist_id = input("Enter the playlist ID: ")
target_user = input("Enter the target user: ")

try:
    # Create a PlexServer instance
    plex = PlexServer(plex_url, plex_token)

    # Retrieve the target user by username
    target_user_obj = plex.myPlexAccount().user(target_user)
    if not target_user_obj:
        raise ValueError("Target user not found.")

    # Retrieve the source playlist by rating key (ID)
    playlist = plex.fetchItem(int(playlist_id))
    if not playlist or playlist.type != "playlist":
        raise ValueError("Invalid playlist ID.")

    # Switch to the target user
    plex = plex.switchUser(target_user_obj.username or target_user_obj.title)

    # Delete the old playlist if it exists
    try:
        target_user_playlist = plex.fetchItem(int(playlist_id))
        target_user_playlist.delete()
    except NotFound:
        pass

    # Create a new playlist for the target user
    new_playlist = plex.createPlaylist(playlist.title, items=playlist.items())
    if not new_playlist:
        raise ValueError("Failed to create the new playlist.")

    print(
        f"Playlist '{playlist.title}' copied successfully to user '{target_user_obj.username or target_user_obj.title}'.")
except ValueError as e:
    print(str(e))
except Exception as e:
    print("Failed to copy the playlist.")
    print(str(e))
