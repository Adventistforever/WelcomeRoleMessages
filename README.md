# CustomDMRoleMessages
 A Discord bot that sends custom messages to members when a monitored role has been granted.
 This bot was requested by a Redditor and fulfilled to their requirements.

## HEROKU SPECIFIC INSTRUCTIONS


### Discord Bot Token and Server Invitation

1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Appplication a name and *Create*
5. Add image for Discord icon
6. Go to Bot tab and click *Add Bot*
7. Enable **SERVER MEMBERS INTENT**
8. Add a bot image
9. Copy the token and
10. Navigate to OAuth2 Tab > URL Generator
11. Check **BOT** under the SCOPES section
12. In the BOT PERMISSIONS section, check the following:
    - Read Messages/View Channels
    - Send Messages
    - Use External Emojis

13. Copy the GENERATED URL link and paste it into your browser or in a discord message. Click the link to invite the bot


### Getting Started
**Github**
1. Login to github
2. Fork this heroku branch of the repo
3. Configure the messages and json file right in github if you wish
4. Make the repo private to prevent public access to your files, messages, IDs, etc.

**Heroku**
1. Login to Heroku - https://id.heroku.com/login
2. Create a new app - give it a name
3. Settings > Config vars - Reveal Config Vars
4. Replace KEY with bot_token and VALUE with your bot token from above (step 9)
5. Add and head back to Deploy
6. Deployment Method - Connnect with Github
7. Add the forked repo to your Heroku account
8. Select the Heroku branch to deploy
9. Deploy the branch
10. Navigate to Resources tab - Dynos
11. Click Edit icon - enable the worker
12. Save
13. Top right corner - More - View Logs
14. Should see the bot load and print the message line that the bot is online and ready.



### Configuring the bot

1. Open config.py in your favorite editor (located in /app)
2. Put your token in the .env-sample and rename to .env
3. Add your IDs for the various variables, notes included in config.py
4. Open the /app/data/(dm/channel) directories and view the sample file included as it contains specific instructions

5. Add your custom messages with the correct naming convetion
6. Bot is now ready to run - `python main.py`


### Specific instructions for custom messages

**Directory layout**

* /app/data/dm


  - sample-01234567890123.txt
  - Active Member-936910278942154782.txt
  - Test Role-947168472985661490.txt
  * /channel
    message.txt


```
This is a sample message - You may use this file for reference. Make each role's custom messages are stored in this same /data directory with the corect filename

The file name must be `role_name-role-id.txt` - as the name of this file illustrates. (without backticks)

**Quick reference**:
The markdown syntax supported by Discord applies to this txt content as well since it's rendered by discord before being sent to the channel.
Embed body text may include links (similar to Reddit)

Italics - * *  | This is a *sample* sentence ("sample" would be italicized)
Bold -  ** **  | This is a **sample** sentence ("sample" would be bold)
Strikethrough - ~~ ~~ | This is a ~~sample~~ sentence ("sample" would have a strike through it's middle)
Links - [The disply link text](https://some-link-to-somewhere.com) | [The display link text] would appear as a clickable link directed to https://some-link-to-somewhere.com


**Emojis**:

Native supported emojies can be added by using the :emoji_name: syntax | :thumbsup: would show the thumbsup emoji
Custom guild emojies can also be used with the <:emoji_name:emoji_id> syntax | Find it easily by sending the emoji to a channel, but placing a \ in front of the icon before sending.
Custom guild animated emojies can also be used with the <a:emoji_name:emoji_id> syntax | Find it easily using the same method for custom guild emojies

```


### Specific instructions for custom Channel messages

**Directory layout**
* /app/data/channel/message.txt (this name must remain message.txt, but you can edit the contents)

```
This is a sample message - You may use this file for reference. This file is only used to send a custom message to the configured channel when any of the configured roles in config.py are added to a member.  The contents of this file are sent as a normal, non-rich Discord message and will only be able to utilize Discord's supported markdown.

DO NOT CHANGE THE NAME OF THIS FILE

**Quick reference**:
The markdown syntax supported by Discord applies to this txt content as well since it's rendered by discord before being sent to the channel.
Embed body text may include links (similar to Reddit)

Italics - * *  | This is a *sample* sentence ("sample" would be italicized)
Bold -  ** **  | This is a **sample** sentence ("sample" would be bold)
Strikethrough - ~~ ~~ | This is a ~~sample~~ sentence ("sample" would have a strike through it's middle)



**Emojis**:

Native supported emojies can be added by using the :emoji_name: syntax | :thumbsup: would show the thumbsup emoji
Custom guild emojies can also be used with the <:emoji_name:emoji_id> syntax | Find it easily by sending the emoji to a channel, but placing a \ in front of the icon before sending.  The resulting message can be copy/pasted into this txt file
Custom guild animated emojies can also be used with the <a:emoji_name:emoji_id> syntax | Find it easily using the same method for custom guild emojies


**mentioning members or roles**
{member} will mention the member that was given the role.  Use this anywhere in the body of this message to mention that member.
{role} will mention the role that the member was given.  Use this anywhere in the body of this message to mention the role

```