import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("free").cek_pw()
   except Exception as e:
       exit(str(e))
