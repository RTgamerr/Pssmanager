import pyfiglet
from fernet import Fernet
import cmd


class cmd2(cmd.Cmd):
  logo1 = pyfiglet.figlet_format("PssManager")
  print(logo1)
  print(""" 
  --------------------------------------------
  - USE "save" <email> <password>             -
  - USE "list"                               -
  - USE "checken"                            -
  --------------------------------------------
  """)


  key = Fernet.generate_key()
  key2 = Fernet(key)



  def  do_save(self, username, password):
   self.username = {}
   self.password = {}

   try:
    with open('psx2z.txt', 'wb') as file0:
        contents = file0.write(username, password)
        key2.encrypt(contents)
   except:
    print('[-] an error has occured')
  

  def do_list():
    try:
     with open('psx2z.txt', 'wb') as file1:
       contents = file1.read(100)
       content0 = key2.decrypt(contents)

       return content0()
    except:
      print('[-] an error has occured')
  def do_help():
    print(''' 
    save - this command saves your cridentials in this format 'save <email> <password>'
    list - this command list all your cridentials
    checken - Idk. When making this command I forgot what it was for once re-vistiting this project again
    ''')
  
if __name__ == '__main__':
 cmd2.cmdloop()


