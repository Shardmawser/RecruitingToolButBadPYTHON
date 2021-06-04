import pynput
from pynput import mouse
from pynput.keyboard import Key, Listener
import pyautogui
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA("Hotkey")

pag = pyautogui

def on_press(key):
        k = str(key)
        
        if k == 'Key.f1':
                pag.write('Is it ok if I ask you a question first?')
        if k == 'Key.f2':
                pag.write("What is your favorite anime?")
        if k == 'Key.f3':
                pag.write('Ok, please follow this link to our discord server: discord.gg/hentai.')
        if k == 'Key.f4':
                pag.write("Once you're there, hit the blue heart in the clan entrance and answer the bot's questions")
        if k == 'Key.f5':
                pag.write("Under 'Who is the Recruiter that you spoke to?' write 'Shardmawser' and under 'Which clan do you plan to be joining?' type in 'Waifu'")
        if k == 'Key.f6':
                pag.write("Feel free to message me once you've finished your application or you encounter any problems.")
        
def on_release(key):
        if key == Key.esc:
                return

with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()



            

