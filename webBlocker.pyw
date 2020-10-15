import time
from datetime import datetime as dt
from datetime import date
import calendar

# write here the path to your hosts file
host_temp = r'C:\Users\Mczaja\webBlocker\hosts'
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
# there is a list of pages which you would like to block
website_list = ['www.facebook.pl', 'facebook.pl', 'facebook.com', 'www.facebook.com',
                'www.wp.pl', 'wp.pl', 'www.onet.pl', 'onet.pl', 'instagram.com',
                'www.youtube.pl', 'youtube.pl', 'www.youtube.com', 'youtube.com']
# During these days, the web blocker will block pages
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

my_date = date.today()

while True:
    if calendar.day_name[my_date.weekday()] in working_days:
        if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < \
                dt(dt.now().year, dt.now().month, dt.now().day, 14):
            print('Working hours........')
            # opening a file and writing the banned sites
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + '\n')
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                # pointer at top of text
                file.seek(0)
                # deleting the banned sites
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print('Not working hours.......')
        #time.sleep(5)
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            # pointer at top of text
            file.seek(0)
            # deleting the banned sites
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Not working days.......')
    time.sleep(5)