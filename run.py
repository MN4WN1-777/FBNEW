import os

if __name__ == "__pycache__":
   try:
       os.system("git pull")
       __import__("xp").cek_pw()
   except Exception as e:
       exit(str(e))
