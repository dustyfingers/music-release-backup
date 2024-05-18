will try in python first then switch to js if I can't get it working quick enough.

this is made to be scheduled as a task with the windows task scheduler :) so you can make the program that is started 'python' or the absolute path to your python installation, and then pass this file's absolute path as the only argument

you will need a token.json file for the google cloud integration in the root directory of this project.

to run this project you will need:

1. a google cloud project with the google drive api enabled
2. a token.json with the proper creds from google for oauth
3. a scheduled task set up on your windows computer that dictates that the program that is started is 'python' or the absolute path to your python installation, and then this file's absolute path as the only argument
4. files to back up to google cloud. I hardcoded my personal release backup folder's absolute path but this should be able to work with any directory. check the BACKUP_FILEPATH constant in main.py
