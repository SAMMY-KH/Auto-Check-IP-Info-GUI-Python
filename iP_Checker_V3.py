from tkinter import *
import requests

root = Tk()
root.title("Tools Checking Ip By SammyKH")
root.geometry("350x200")
root.iconbitmap("Logo/IP Logo.ico")
root.resizable(False, False)
root.configure(bg='Grey')



def info():
    root.update()
    labelpopme.destroy()
    Output_results.delete(1.0, END)

    try:
        ip1= "https://icanhazip.com/"
        response1 = requests.get(ip1).text
        print(response1)
        labelpopip.config(text="Your IP : "+str(response1))
        ip = Output_results.get("1.0", "end-1c")
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            "[-] Live IP": response.get("query"),
            "[-] Live Country": response.get("country"),
            "[-] Live Region": response.get("regionName"),
            "[-] Live City": response.get("city"),
            "[-] Live Zip-code": response.get("zip"),
            "[-] Live Latitude": response.get("lat"),
            "[-] Live Longitude": response.get("lon"),
            "[-] Live Timezone": response.get("timezone"),
            "[-] Live Provider": response.get("isp"),
            "[-] Live Organization": response.get("org")
        }
        for k, e in data.items():
            print(f"[bold cyan]{k}: [bold yellow]{e}")
            show_info = (f"{k}: {e}")
            Output_results.insert(END,show_info+str("\n"))
            
        print("")
    except Exception as e:
        print(f"[bold red]An '{e}' error occurred")
myfram1 = Frame(root)
myscrollbar1 = Scrollbar(myfram1, orient=VERTICAL)
Output_results = Text(myfram1, height = 7,width = 46,fg="Black",bg = "light grey" ,font='none 10 bold italic',yscrollcommand=myscrollbar1.set)
myscrollbar1.config(command=Output_results.yview)
myscrollbar1.pack(side=RIGHT, fill=Y)
myfram1.place(x = 3,y = 40)
Output_results.pack(pady=1)

CHIP1_BTN = Button(root, height = 1,width = 10,bg='Green',fg='Light Green',text ="Show IP info",command=info)
CHIP1_BTN.place(x = 135,y = 160)

labelpopme = Label(root,fg='Blue',bg='Grey', text = 'Tools By SAMMY KH Donate Me By ABA-003 398 932 KHOM SAMNANG',font='none 7 bold italic')                    
labelpopme.place(x = 8,y =19)

labelpoppro = Label(root,fg='Gold',bg='Grey', text = '  Tools By',font='none 15 bold italic')                    
labelpoppro.place(x = 8,y =160)
labelpoppro1 = Label(root,fg='RED',bg='Grey', text = 'SAMMY_KH',font='none 15 bold italic')                    
labelpoppro1.place(x = 225,y =160)

labelpopip=Label(root, text="",bg="Grey",fg="black",font='none 10 bold italic', justify=RIGHT)
labelpopip.place(x = 105,y =1)
root.mainloop()  