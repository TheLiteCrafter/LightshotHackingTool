import webbrowser
from configparser import ConfigParser
import sys
import random
import string

config = ConfigParser()
config.read("config.ini")

try:
    browser_path = str(config["Settings"]["browser_path"] + " %s")
    browser_mode = str(config["Settings"]["def_browser_mode"])
    mode = str(config["Settings"]["def_mode"])
    times = int(config["Settings"]["def_links"])

except Exception as e:
    print("Config File Is Corrupted or does no Exist! This Programm will Exit!")
    sys.exit("Config File Is Corrupted or does no Exist!")

def get_url():
    RANDOM_GEN = str(str(random.choice(
        string.ascii_letters)).lower() + 
        str(random.choice(string.ascii_letters)).lower() + 
        str(random.randint(0, 9)) + str(random.randint(0, 9)) + 
        str(random.randint(0, 9)) + str(random.randint(0, 9))
        )
    URL = "https://prnt.sc/" + RANDOM_GEN

    return(URL)

while 1:

    command = input("Please Enter a Command: ")
    command = str(command).lower()

    if command == "help":
        print("List of avilable commands:")
        print("help - Shows a List of all avilable commands")
        print("start - Starts the process")
        print("exit - Exists the programm")
        print("mode direct/written - Changes the Output-Mode")
        print("links (int) - how many links should be generated/opened")
        print("browser_mode normal/private - in wich mode the browser should start")

    elif command == "exit":
        sys.exit()

    elif command == "mode direct":
        mode = "direct"
        print("Success! Mode is now: " + mode)

    elif command == "mode written":
        mode = "written"
        print("Success! Mode is now: " + mode)

    elif "links" in command:
        times = int(command.replace("links ", ""))
        print("Success! links is now: " + str(times))

    elif command == "browser_mode normal":
        browser_mode = "normal"
        print("Success! browser_mode is now: " + browser_mode)

    elif command == "browser_mode private":
        browser_mode = "private"
        print("Success! browser_mode is now: " + browser_mode)

    elif command == "start":

        count = 1

        if mode == "direct":
            while count <= times:

                if browser_mode == "private":
                    webbrowser.get(browser_path + " --incognito").open(get_url())

                else:
                    webbrowser.get(browser_path).open(get_url())
                
                count = count+1

        else:
            f = open("output.txt", "w")

            while count <= times:
                f.write(get_url() + "\n")
                count = count+1

            f.close()

    else:
        print("Invalid Command! Type help for a list of commands!")