import os
import json
import subprocess
import argparse
import sys
import pyfiglet
from rich import print
from typing import DefaultDict

title = pyfiglet.figlet_format('Muxing Script', font='slant')
print(f'[red]{title}[/red]')
print("by Miji-Desu")

mkvmerge = './mkvmerge'

video = input("\nEnter Video Filename : ")
audio = input("\nEnter Audio Filename : ")
output = input("\nSpecify Output Filename : ")

print("Merging .....")
subprocess.run([mkvmerge, '--ui-language' ,'en_US', '--output', output +'.mkv', '--language', '0:eng', '--track-name', '0:Pipe-HD', '--default-track', '0:yes', '--compression', '0:none', video, '--language', '0:eng', '--track-name', '0:Pipe-HD', '--default-track', '0:yes', '--compression' ,'0:none', audio])
print("\nAll Done .....")
