import os
from datetime import datetime

# Global variables
NAME = "LOGS" + str(datetime.timestamp(datetime.now())).replace('.', '')
SCRIPT = "tar -czf /var/log/" + NAME + " /var/log"


def init_cmd(**kwargs):
    '''

    :param kwargs: contains all needed parameters to execute program
    :return: initialized command
    '''

    time = '* * * * * '
    script = 'echo "Hello World!" '


    for k, v in kwargs.items():

        if k == 'time':
            time = v

        if k == 'script':
            script = v

    return "(crontab -l ; echo '" + time + script + "') | crontab -"


if __name__ == "__main__":
    os.system(init_cmd(time='0 0 1 */1 * ', script=SCRIPT))
