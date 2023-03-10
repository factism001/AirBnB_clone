#!/usr/bin/python3
"""
    Main Console program
"""
import cmd
import models
import re
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

classes = {'BaseModel': BaseModel, 'User': User,
           'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbnb) "

    @classmethod
    def fetch_command(cls, command):
        commands = {"all": cls.do_all, "show": cls.do_show,
                    "destroy": cls.do_destroy, "update": cls.do_update,
                    "count": cls.do_count}
        if command in commands:
            return commands[command]
        else:
            return None

    def do_EOF(self, arg):
        """Quit the program"""
        return True

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def emptyline(self):
        """Ignore empty inputs"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a Model"""
        if arg:
            try:
                args = arg.split()
                template = models.dummy_classes[args[0]]
                new_instance = template()
                try:
                    for pair in args[1:]:
                        pair_split = pair.split("=")
                        if (hasattr(new_instance, pair_split[0])):
                            value = pair_split[1]
                            flag = 0
                            if (value.startswith('"')):
                                value = value.strip('"')
                                value = value.replace("\\", "")
                                value = value.replace("_", " ")
                            elif ("." in value):
                                try:
                                    value = float(value)
                                except ValueError:
                                    flag = 1
                            else:
                                try:
                                    value = int(value)
                                except ValueError:
                                    flag = 1
                            if (not flag):
                                setattr(new_instance, pair_split[0], value)
                        else:
                            continue
                    new_instance.save()
                    print(new_instance.id)
                except ValueError:
                    new_instance.rollback()
            except ValueError:
                print("** class doesn't exist **")
                models.storage.rollback()
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Show the representation of an instance - Usage show <Classname>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            line = args.split()
            if line[0] in classes:
                if len(line) < 2:
                    print("""** instance id missing **""")
                else:
                    objects = models.storage.all()
                    key = str(line[0]) + "." + str(line[1])
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """Delete the instance of a given class -
        Usage: destroy <classname> <id>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            line = args.split()
            if line[0] in classes:
                if len(line) < 2:
                    print("""** instance id missing **""")
                else:
                    objects = models.storage.all()
                    key = str(line[0]) + "." + str(line[1])
                    if key in objects:
                        del(objects[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """string representation of all instances"""
        result = []
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                current_inst = models.dummy_classes[arg[0]]
                for i, o in models.storage.all(current_inst).items():
                    if i.split('.')[0] == arg[0]:
                        result.append(str(o))
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models.storage.all().items():
                result.append(str(obj))
        if result:
            print(result)

    def do_update(self, args):
        """Update or set att in an instance -
        Usage: update <classname> <id> <att_name> <att_value>\n"""
        line = shlex.split(args)
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(line[0]))
            except KeyError:
                print("** class doesn't exist **")
                return
            if len(line) == 1:
                print("** instance id missing **")
            else:
                objects = models.storage.all()
                key = str(line[0]) + "." + str(line[1])
                if key not in objects:
                    print("** no instance found **")
                else:
                    if len(line) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line) == 3:
                            print("** value missing **")
                        else:
                            setattr(objects[key], line[2], line[3])
                            models.storage.save()

    def do_count(self, arg):
        """
        count number of instances
        """
        count = 0
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                for instance, obj in models.storage.all().items():
                    if instance.split('.')[0] == arg[0]:
                        count += 1
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models.storage.all().items():
                count += 1
        print(count)

    def default(self, line):
        """
        handle invalid commands and
        special commands like <class name>.<command>()
        """
        match = re.fullmatch(r"[A-Za-z]+\.[A-Za-z]+\(.*?\)", line)
        if match:
            splited = line.split('.')
            if splited[0] in models.dummy_classes:
                parsed = splited[1].split("(")
                parsed[1] = parsed[1].strip(")")
                args = parsed[1].split(",")
                args = [arg.strip() for arg in args]
                if len(args) >= 3:
                    temp = args[2]
                    args = [arg.strip('"') for arg in args[:2]]
                    args.append(temp)
                else:
                    args = [arg.strip('"') for arg in args]
                command = self.fetch_command(parsed[0])
                if command:
                    reconstructed_args = [arg for arg in args]
                    reconstructed_args.insert(0, splited[0])
                    reconstructed_command = " ".join(reconstructed_args)
                    command(self, reconstructed_command)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
