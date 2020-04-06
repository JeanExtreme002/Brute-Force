from argparse import ArgumentParser
import os


class ArgParser(ArgumentParser):

    def __init__(self, description = None, data_dir = "."):
        
        ArgumentParser.__init__(self, description = description)

        self.add_argument(
            "--command", required = True, 
            help = 'Command to run a program. (ex: "start app {}")'
            )

        self.add_argument(
            "--code", "-c", type = int, default = 0, 
            help = 'Expected exit code. (default: 0)'
            )

        self.add_argument(
            "--charset", "-f", default = os.path.join(data_dir, "charset.txt"),
            help = "File with the characters that will be used to generate password combinations."
            )

        self.add_argument(
            "--range", "-r", default = "A-Za-z0-9",
            help = 'Creates a charset.txt file with a range of characters. (default: "A-Za-z0-9")'
            )

        self.add_argument(
            "--excludes", "-e", default = "\n, ",
            help = 'Ignores some characters in the charset file.'
            )

        self.add_argument(
            "--min", type = int, default = 1,
            help = 'Maximum password length. (default: 1)'
            )

        self.add_argument(
            "--max", type = int, default = 5,
            help = 'Minimum password length. (default: 5)'
            )

        self.add_argument(
            "--show", "-s", default = "true",
            help = "Shows generated passwords. (default: true)"
            )


    def validate_args(self, args, err_callback):

        """
        Valida os argumentos.
        """

        if not args.command or not "{}" in args.command:
            err_callback('Please enter a command using "{}" to indicate the location of the password')

        if not args.charset:
            err_callback("Please enter a valid file name.")


