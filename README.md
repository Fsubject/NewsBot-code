# NewsBot - A utility Python Discord bot
## How to setup
1. Clone the repository
2. Install the following modules: *discord.py*, *asyncpg*, *newsdataapi*
3. Modify the *settings.py* file with your own settings
4. Create a *.env* file with the following content (change the values):  
    ```
    DISCORD_API_KEY=YOUR_DISCORD_API_KEY
    NEWS_API_KEY=YOUR_NEWSDATA.IO_API_KEY
    
    DATABASE_USERNAME=YOUR_DATABASE_USERNAME
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    DATABASE_NAME=YOUR_DATABASE_NAME
    DATABASE_HOST=YOUR_DATABASE_HOST
    
    TIMEZONE=YOUR_TIMEZONE
    ```
5. Run the bot using the command: `python3 main.py`  

*Feel free to modify the code because some settings aren't in the settings.py file*

## Contribute
I am *open* to contributions as long as you don't just break everything.

## Credits
* Discord: __fsubject__
* Twitter: <a href="https://twitter.com/Fsubj_ect">__@ffsubject__</a>
* Made *__entirely__* by __Fsubject__