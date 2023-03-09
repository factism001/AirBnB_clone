#!/usr/bin/python3
"""AirBnB console"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import models

classes = {'BaseModel': BaseModel, 'User': User,
           'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Console main class"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the programm
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the programm
        """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):
        """Create a new instance - Usage: create <Classname>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            if args in classes:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

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

    def do_all(self, args):
        """Print all instances of a class - Usage: all <classname>\n"""
        objects = models.storage.all()
        objList = []
        if args == "":
            for key in objects:
                objList.append(str(objects[key]))
            print(objList)
        else:
            try:
                line = args.split()
                eval(line[0])
                for elem in objects:
                    aux = objects[elem].to_dict()
                    if aux['__class__'] == line[0]:
                        objList.append(str(objects[elem]))
                print(objList)
            except KeyError:
                print("** class doesn't exist **")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
