# bscNewChainTokenScanner
This scanner will track all the new bsc chain tokens from the time bscList.py is run for holders. When acheived certain thresholds they will post to a telegram channel. 

The database of the token IDS are held in a pickle file.

pip3 install telegram-send

pip3 install beautifulsoup4

Run bscList.py to start tracking new BSC chain tokens.
Run holderScap.py to track the amount of holders and post the to telegram.

SETTING UP TELEGRAM

Go to @BotFather on telegram and setup an Bot with the easy to follow instructions.

Alternatively please use in the cli

telegram-send --configure

remove the conf = "user1.conf" from the telegram-send() portion of the code
