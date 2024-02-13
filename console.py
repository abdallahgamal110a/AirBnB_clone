#!/usr/bin/python3
import cmd



class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        return True

    def do_help(self, arg):
        return super().do_help(arg)

    def do_prompt(self, line):
        self.prompt = line

    def do_create (self, *arg):
        args = arg.split()
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
