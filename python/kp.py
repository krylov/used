from argparse import ArgumentParser
import logging
from os.path import exists
from pykeepass import PyKeePass
from pykeepass.pykeepass import create_database


parser = ArgumentParser()
parser.add_argument('-f', '--path',
                    help='Path to database file')
parser.add_argument('-p', '--password',
                    default='',
                    help='Password for database file')
cmd_choices = ['add', 'get', 'replace',
               'remove', 'copy']
parser.add_argument('-c', '--command',
                    choices=cmd_choices,
                    default='get',
                    help='Command')
parser.add_argument('-g', '--group',
                    help='Target group to execute action')
parser.add_argument('-t', '--title',
                    help='Target title to execute action')
parser.add_argument('-u', '--user',
                    action='store_true',
                    help='Target group to execute action')
args = parser.parse_args()


logging.basicConfig(level=logging.DEBUG)
logging.info('Start ...')
if not exists(args.path):
    logging.info(f'No database {args.path}')
    create_database(args.path, password=args.password)
logging.debug(f'Command: {args.command}') 

kp = PyKeePass(args.path, 
               password=args.password)
group = kp.find_groups(name=args.group, first=True)
entry = kp.find_entries(group=group, title=args.title, first=True)
print(entry.password)




