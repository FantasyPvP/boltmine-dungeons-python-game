class Console():
    def __init__(self):
        return

    def input_(self, message, colour):
        message = message + "\n╰─> "
        string = self.format_(message, colour)
        msgIn = input(string)
        return(msgIn)

    def output_(self, message, colour):
        string = self.format_(message, colour)
        print("\n" + string)
        return(True)

    def status_(self, message, messageType):
        if messageType == "status":
            print(f"\n\u001b[33mStatus:\n╰─> {message}\u001b[0m")
        elif messageType == "warning":
            print(f"\n\u001b[33mWarning:\n╰─> {message}\u001b[0m")
        else:
            print("status doesnt exist")

    def error_(self, message, errorType):
        if errorType == "normal":
            print(f"\n\u001b[31mError:\n╰─> {message}\u001b[0m")
        elif errorType == "critical":
            print(f"\n\u001b[31;1mCritical Error:\n╰─> {message}\u001b[0m")


    def format_(self, message, colour):
        if colour == "black":
            string = f"\u001b[30m{message}\u001b[0m"
        elif colour == "red":
            string = f"\u001b[31m{message}\u001b[0m"
        elif colour == "green":
            pstring = f"\u001b[32m{message}\u001b[0m"
        elif colour == "yellow":
            string = f"\u001b[33m{message}\u001b[0m"
        elif colour == "blue":
            string = f"\u001b[34m{message}\u001b[0m"
        elif colour == "magenta":
            string = f"\u001b[35m{message}\u001b[0m"
        elif colour == "cyan":
            string = f"\u001b[36m{message}\u001b[0m"
        elif colour == "white":
            string = f"\u001b[37m{message}\u001b[0m"
        elif colour == "black-bold":
            string = f"\u001b[30;1m{message}\u001b[0m"
        elif colour == "red-bold":
            string = f"\u001b[31;1m{message}\u001b[0m"
        elif colour == "green-bold":
            string = f"\u001b[32;1m{message}\u001b[0m"
        elif colour == "yellow-bold":
            string = f"\u001b[33;1m{message}\u001b[0m"
        elif colour == "blue-bold":
            string = f"\u001b[34;1m{message}\u001b[0m"
        elif colour == "magenta-bold":
            string = f"\u001b[35;1m{message}\u001b[0m"
        elif colour == "cyan-bold":
            string = f"\u001b[36;1m{message}\u001b[0m"
        elif colour == "white-bold":
            string = f"\u001b[37;1m{message}\u001b[0m"
        else:
            string = "invalid colour"
        return(string)