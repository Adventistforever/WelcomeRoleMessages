# CustomDMRoleMessages
 A Discord bot that sends custom messages to members when a monitored role has been granted.
 This bot was requested by a Redditor and fulfilled to their requirements.


 ### Discord Bot Token and Server Invitation

1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Appplication a name and *Create*
5. Add image for Discord icon
6. Go to Bot tab and click *Add Bot*
7. Enable **SERVER MEMBERS INTENT**
8. Add a bot image
9. Copy the token and paste it into the config.json located in the /app
10. Navigate to OAuth2 Tab > URL Generator
11. Check **BOT** under the SCOPES section
12. In the BOT PERMISSIONS section, check the following:
    - Read Messages/View Channels
    - Send Messages
    - Use External Emojis

13. Copy the GENERATED URL link and paste it into your browser or in a discord message. Click the link to invite the bot



### Getting Started

#### Prequisites

1. Install Python 3.9+
2. install dependancies - `pip install -r requirements.txt`


### Configuring the bot

1. Open config.json in your favorite editor (located in /app)
2. Paste the token you copied above (step 9) into the config.json
3. Add *ONE** target channel or member ID for messages to be sent when a DM cannot be sent to the member (privacy settings) - default `null`
3. Add your comma seperated list of IDs for the roles you wish to monitor
4. Open the /app/data directory and view the sample file included as it contains specific instructions
5. Add your custom messages with the correct naming convetion
6. Bot is now ready to run - `python main.py`


### Config Examples

**No target member/channel for DM error message, 1 monitored role**

```json
{
    "bot_token": "some-bot-token",
    "error_send_target" : null,
    "roles": [4687987654987]
}
```

**Target member/channel for DM error message, 2 monitored roles

```json
{
    "bot_token": "some-bot-token",
    "error_send_target" : 9879654698798,
    "roles": [4687987654987,5649879654]
}
```