#!/usr/bin/python3
"""Module for the command line interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interpreter methods
    """
    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """Used to create a new instance of the BaseModel and save it to a
            Json file.
        """
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_EOF(self, line):
        """When ctrl+D EOF is called trigger exit on program
        """
        print("")
        return True

    def do_show(self, line):
        """Outputs the string representation of an instance based on class
            name and id.
        """
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(inputs[0], inputs[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Function that deletes an instance based on the class name and id
        """
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(inputs[0], inputs[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Function to print string representation of all instances
        """
        objs = storage.all()

        inputs = shlex.split(line)

        if len(inputs) == 0:
            for key, val in objs.items():
                print(str(val))
        elif inputs[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, val in objs.items():
                if key.split('.')[0] == inputs[0]:
                    print(str(val))

    def do_update(self, line):
        """Function used to update an instance based on the class name and id.
            Use: update <class name> <id> <attribute name> "<attribute value>"
        """
        inputs = shlex.split(line)

        if len(inputs) == 0:
            print("** class name missing **")
        elif inputs[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(inputs[0], inputs[1])
            if key not in objs:
                print("** no instance found **")
            elif len(inputs) < 3:
                print("** attribute name missing **")
            elif len(inputs) < 4:
                print("** value missing **")
            else:
                obj = objs[key]

                attribute_name = inputs[2]
                attribute_value = inputs[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass

                setattr(obj, attribute_name, attribute_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
