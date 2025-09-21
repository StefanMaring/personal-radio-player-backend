# personal-radio-player-backend
Backend for a small personal local radio player

## API-endpoints

### /getSong:
Gets a random song (.mp3 file) from the audio folder located in the root of the project.

### /recentlyPlayed (POST)
Stores data for a recently played song in a local JSON-file (not in repository)

### /recentlyPlayed (GET)
Retrieves all the available "recently played" data from a local JSON-file (not in repository)

## Local DB
This radio player works with a simple JSON-file that is stored locally in the root of the app (so where main.py is). 
The file needs to be called `recentlyPlayed.json` and must contain `[]` as content in order for it to work.

## Audio storage
This radio player expects `.mp3` files to send to the frontend. These `.mp3` files can be stored in the `audio` folder.
The `audio` folder is not included in the repository. The `audio` folder must be put in the root of the app (so where main.py is).
After creating the folder, you can put as many `.mp3` files in as you want.

## Randomized Song Selection
This API utilizes a small queue data structure implementation in order to make sure the same song doesn't play directly again. 
If a song is selected and it's in the queue, the script will continue to find a song that is not in the queue. 
When the queue has more than 5 songs, a song is removed from the queue. This allows for that particular song to be played again.
