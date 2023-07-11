import os
from plexapi.server import PlexServer

PLEX_ENV_FILE = "plex-env.txt"

# Load environment variables from file
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

# Create a PlexServer instance
plex = PlexServer(plex_url, plex_token)

# List all playlists
print("Playlists:")
for playlist in plex.playlists():
    print(f"ID: {playlist.ratingKey}\tTitle: {playlist.title}")
