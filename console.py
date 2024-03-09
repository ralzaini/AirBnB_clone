#!/usr/bin/python3

"""
    Module for the console
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Console class for HBNB project
    """
    prompt = "(hbnb)"
    valid_class = ["BaseModel", "User", "State", "Review", "Place", "Amenity",
                   "City"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self, arg):
        """
        Print help message for exit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle End-of-File (EOF) input
        """
        print("")
        return True

    def emptyline(self):
        """
        Empty the last command
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id. Ex: $ create BaseModel
        """
        args = shlex.split(arg)
        class_name = args[0] if args else None
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.valid_class:
            print("** class doesn't exist **")
        else:
            new_inst = eval(class_name)()
            storage.save()
            print(new_inst.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = shlex.split(arg)
        class_name = args[0] if args else None
        instance_id = args[1] if len(args) > 1 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.valid_class:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            objs_dict = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            print(objs_dict.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and,
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = shlex.split(arg)
        class_name = args[0] if args else None
        instance_id = args[1] if len(args) > 1 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.valid_class:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            objs_dict = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objs_dict:
                del objs_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all
        """
        objs_dict = storage.all()
        args = shlex.split(arg)

        if not args:
            instances = objs_dict.values()
        elif args[0] not in self.valid_class:
            print("** class doesn't exist **")
            return
        else:
            instances = []
            for key, value in objs_dict.items():
                if key.split('.')[0] == args[0]:
                    instances.append(value)
            for instance in instances:
                print(str(instance))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding,
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = shlex.split(arg)

        if len(args) < 2:
            print("** class name and/or instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in self.valid_class:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        objs_dict = storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in objs_dict:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name and/or value missing **")
            return

        obj = objs_dict[key]
        attribute_name = args[2]
        attribute_value = args[3]

        try:
            attribute_value = eval(attribute_value)
        except Exception:
            pass

        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
