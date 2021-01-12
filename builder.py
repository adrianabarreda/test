import frame
import common as c


class builder:
    def __init__(self):
        self.frame = frame.baseFrame("nagios_frame")
        (self.frame).set_field_format()
        self.build_frame()

    def return_fields(self):
        return (self.frame).fields

    def set_header(self,new_h):
        (self.frame).set_header(new_h)

    def set_footer(self,new_f):
        (self.frame).set_footer(new_f)

    def add_field(self,new_Field):
        (self.frame).add_field(new_Field.strip("\n"))

    def build_frame(self):
        new_h = input("Please specify the first line of your config object.\n This would be the first line before any dynamic fields.\n If there is none, Leave this blank.\n")
        (self.frame).set_header(new_h)
        new_f = input("Please specify the last line of your config object.\n This would be the line directly after the KEY VALUE section.\n If there is none, Leave this blank.\n")
        (self.frame).set_footer(new_f)


    def print_frame(self,choices):
        print(f"{(self.frame).header}")
        key_enc = (self.frame).get_f_status('encapsulate_key')
        val_enc =  (self.frame).get_f_status('encapsulate_value')
        x=0
        delim =(self.frame).get_f_status('delimiter')
        max_spaces = (self.frame).maxFieldLength
        for field in (self.frame).fields:
            current_choice = choices[x].strip('\n')
            spaces = max_spaces - len(field)
            print(f"    {key_enc}{field}{key_enc}{delim}{' '*spaces}{val_enc}{current_choice}{val_enc}")
            x = x+1
        print(f"{(self.frame).footer}")

    def ask_new_field(self):
        r = input("Please set the KEY of the new field, Do not add quotes or delimiters.\n")
        if self.confirm_new_field(r):
            (self.frame).add_field(r)
            return
        else:
            print("Lets try again!")
            return self.ask_new_field()



    def confirm_new_field(self,r):
        r = input(f"The new field you wish to add is '{r}' Correct?(y/n)\n")
        if r.lower() == "y":
            return True
        elif r.lower() == "n":
            return False
        else:
            return self.confirm_new_field(r)



    def num_of_fields(self,x=0):
        if x < 5:
            r = input("How many fields will you need?\n Fields:")
            try:
                return int(r)
            except ValueError:
                x = x + 1
                return self.num_of_fields(x)
        else:
            c.error_lazy("num_of_fields")


