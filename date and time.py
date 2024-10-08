#creator :Sreehari pramod
#date :8-10-2024

from datetime import datetime
current=datetime.now()
print(current)
print(current.strftime("%Y-%m-%d %H:%M:%S"))
print(current.strftime("%m/%d/%Y"))
print(current.strftime("%A,%B %d,%Y"))
print(current.strftime("%A,%b %d,%Y %H:%M:%S %p"))
print(current.strftime("%a-%b-%d %H:%M:%S %z %Y"))
print(current.strftime("%a-%b-%d %H:%M:%S %z %Y"))
print(current.isoformat())
print(current.strftime("%d"))
print(current.strftime("%H:%M:%S"))
print(current.strftime("%m"))
print(current.strftime("%y"))

