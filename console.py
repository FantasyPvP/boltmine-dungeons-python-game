class Console():
    def __init__(self):
        return

    def output_(self, message, messageType, colour):
        if messageType == "error":
            print(f"\u001b[31merror:\n╰─> {message}\u001b[0m")

        elif messageType == "status":
            print(f"\u001b[33mstatus:\n╰─> {message}\u001b[0m")

        elif messageType == "colour":
            string = self.format_(message, colour)
            print(string)
        else:
            print("output type doesnt exist")
        return

    def input_(self, message, messageType, colour):
        string = self.format_(message, colour)
        msgIn = input(string)
        return(msgIn)

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