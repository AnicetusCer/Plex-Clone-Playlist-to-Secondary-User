# Plex Playlist Sync Scripts

These scripts allow you to sync Plex playlists to shared users using the Plex API. The scripts are written in Python and utilize the `plexapi` library.

## Prerequisites

- Python 3.x installed on your system.
- The `plexapi` library installed. You can install it by running `pip install plexapi`.
- Optional guidance, I use community PyCharm (other IDE's exist), setup a new venv to install the pip plexapi package into.

## Getting Started

1. Clone or download the repository to your local machine.

2. Configure the Plex server details in the `plex-env.txt` file. This file should contain the following environment variables:

   - `PlexIp`: The IP address or hostname of your Plex server.
   - `PlexPort`: The port number of your Plex server (default is `32400`).
   - `PlexToken`: The authentication token for your Plex server.
     - PlexToken this is the api access token for you plex server, there is, nowadays, no simple way to retrive this, the easiest way to get it is to...
       - Log into plex.tv in your browser 
       - Go to a media library and select anything, a film, a track, a tv episode ect.
       - Open the ... menu and elect 'more' > 'get info'
       - This opens the 'Media Info' window, in here select 'View XML' this will open a new xml webpage
       - A the end of the web pages address bar you will find the X-Plex-Token
       - Here is the official page on the subject "https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/"

3. Run the `plex-playlists-list.py` script to list all the available playlists in your Plex server. This script reads the Plex server details from the `plex-env.txt` file.

# Plex Playlist Sync Scripts

These scripts allow you to sync Plex playlists to shared users using the Plex API. The scripts are written in Python and utilize the `plexapi` library.

## Prerequisites

- Python 3.x installed on your system.
- The `plexapi` library installed. You can install it by running `pip install plexapi`.

## Getting Started

1. Clone or download the repository to your local machine.

2. Configure the Plex server details in the `plex-env.txt` file. This file should contain the following environment variables:

   - `PlexIp`: The IP address or hostname of your Plex server.
   - `PlexPort`: The port number of your Plex server (default is `32400`).
   - `PlexToken`: The authentication token for your Plex server.

3. Run the `plex-playlists-list.py` script to list all the available playlists in your Plex server. This script reads the Plex server details from the `plex-env.txt` file.

### python plex-playlists-list.py
This will display a list of playlists along with their IDs. Make note of the desired playlist ID for syncing.

4. Run the `plex-playlist-sync-to-user.py` script to sync a playlist to a target user. This script also reads the Plex server details from the `plex-env.txt` file.

### python plex-playlist-sync-to-user.py
Follow the prompts to enter the playlist ID and the target user. The script will attempt to copy the playlist to the specified user.

## Troubleshooting

- If you encounter any errors or issues, make sure that your Plex server is accessible and the provided server details (IP, port, token) are correct. Also, ensure that the target user exists and the playlist ID is valid.
- Refer to the [plexapi documentation](https://python-plexapi.readthedocs.io/) for more information on using the library and troubleshooting common issues.

