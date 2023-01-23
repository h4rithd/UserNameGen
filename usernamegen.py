#!/usr/bin/python3
import textwrap
import argparse
from tqdm import tqdm

user_list = []

def listGen(first_name, last_name):
    user_list.append(first_name + last_name)
    user_list.append(last_name + first_name)
    user_list.append(first_name + "." + last_name)
    user_list.append(first_name[0] + "." + last_name)
    user_list.append(first_name + "." + last_name[0])
    user_list.append(last_name[0] + "." + first_name)
    user_list.append(last_name + "." + first_name[0])
    user_list.append(first_name.capitalize() + last_name.capitalize())
    user_list.append(last_name.capitalize() + first_name.capitalize())
    user_list.append(first_name.capitalize() + "." + last_name.capitalize())
    user_list.append(first_name[0].capitalize() + "." + last_name.capitalize())
    user_list.append(first_name.capitalize() + "." + last_name.capitalize()[0])
    user_list.append(last_name.capitalize()[0] + "." + first_name.capitalize())
    user_list.append(last_name.capitalize() + "." + first_name.capitalize()[0])

    for combination in user_list:
        print(combination)


def write2file(userList, outoutfile):
    with open(outoutfile, "w") as out:
        for combination in userList:
            out.write(combination+'\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='usernamegen.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
    -------------------------------------------------------------
    ---------------- | Username Generator |----------------------
    -------------------------------------------------------------
         _____             _____               _____
        |  |  |___ ___ ___|   | |___ _____ ___|   __|___ ___
        |  |  |_ -| -_|  _| | | | .'|     | -_|  |  | -_|   |
        |_____|___|___|_| |_|___|__,|_|_|_|___|_____|___|_|_|   
    				        by h4rith.com
    -------------------------------------------------------------'''),
        usage='python3 %(prog)s -f [usernames.txt] ',
        epilog='------------------ Script from h4rithd.com ------------------'
    )
    parser._action_groups.pop()
    required = parser.add_argument_group('[!] Required arguments')
    optional = parser.add_argument_group('[!] Optional arguments')
    optional.add_argument("-f", "--file", metavar='',
                          help="File that contain FirstName LastName.")
    optional.add_argument("-u", "--username", metavar='',
                          help="Single username as \"FirstName LastName\".")
    required.add_argument("-o", "--output", metavar='',
                          required=True, help="Output file name.")
    args = parser.parse_args()

    if args.file is not None:
        with open(args.file) as f:
            lines = f.readlines()
            for line in tqdm(lines):
                full_name = line.strip().split()
                first_name = full_name[0].lower()
                last_name = full_name[1].lower()
                listGen(first_name, last_name)
    elif args.username is not None:
        full_name = args.username.strip().split()
        first_name = full_name[0].lower()
        last_name = full_name[1].lower()
        listGen(first_name, last_name)
    else:
        print("You should use either a single username like \"FirstName LastName\" as -u or a list of file which include \"FirstName LastName\" as -f parameter. ")

    write2file(user_list, args.output)
