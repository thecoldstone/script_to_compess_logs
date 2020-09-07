import os
from datetime import datetime

NAME = "LOGS" + str(datetime.timestamp(datetime.now())).replace('.', '')
SCRIPT = "tar -czf /var/log/" + NAME + " /var/log"
COMMAND = "(crontab -l ; echo '* * * * * " + SCRIPT + "')| crontab -"
# os.system()

print(COMMAND)