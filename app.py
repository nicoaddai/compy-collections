import os
# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ["SLACK_BOT_TOKEN"]
)

# Add functionality here
#user ids
    #maxen: U038JV06ZMZ
    #ryan:U029XD01PNF
    #daniela: U03E7JSK3LG
    #solomon: U032SNVUAF8
#channel ids
    #test: C03DB6U9U8Y
    #hw1: C019J946UPJ




@app.event("message")
def auto_reply(event, say):
    try:
        if 'files' in event:
            if event['channel'] == "C019J946UPJ" and ('.pdf' in event['files'][0]['name'] or '.google' in event['text'] or re.compile(r'<(.+)\|\(google\)>') in event['text']) and (event['user'] != 'U038JV06ZMZ' and event['user'] != 'U03612ME0BY' and event['user'] != 'U029XD01PNF' and event['user'] != 'U038JV0HD19' and event['user'] != 'U03E7JSK3LG' and event['user'] != 'U032SNVUAF8'): #if statement clarifying channel to watch for & to not reply to replies
                say(text = "An IL scientist will connect with you shortly. Before we do, take this opportunity to double check your key behavior. Is it uncomfortably specific? See the examples in this document to help you refine your thinking. https://docs.google.com/document/d/1EVoyhVnX_jTzNbWBrN8C9Bz8-A7xHO8wN5dM6o-Oves/edit#",
                thread_ts = event['ts'])
                #print(event)
        else:
            if event['channel'] == "C019J946UPJ" and ('.google' in event['text'] or re.compile(r'<(.+)\|\(google\)>') in event['text']) and (event['user'] != 'U038JV06ZMZ' and event['user'] != 'U03612ME0BY' and event['user'] != 'U029XD01PNF' and event['user'] != 'U038JV0HD19' and event['user'] != 'U03E7JSK3LG' and event['user'] != 'U032SNVUAF8'): #if statement clarifying channel to watch for & to not reply to replies
                say(text = "An IL scientist will connect with you shortly. Before we do, take this opportunity to double check your key behavior. Is it uncomfortably specific? See the examples in this document to help you refine your thinking. https://docs.google.com/document/d/1EVoyhVnX_jTzNbWBrN8C9Bz8-A7xHO8wN5dM6o-Oves/edit#",
                thread_ts = event['ts'])
                #print(event)
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
