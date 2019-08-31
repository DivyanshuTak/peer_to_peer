import sys
import os


list = [10,5,5,5,50]

dummy=0
for dummy in len(list):
    print("bitch")


while True:
    pass
try:
    print("parent ID ::",(os.getpid()))
except OSError:
    print("coudnt process the request")

try:
    pid = os.fork()
except :
    print("coudnt create child process")
    exit()

if pid == 0:
    print("in the child process")
    exit()

print("we have created a child",pid)
finished = os.waitpid(0, 0)
print(finished)


