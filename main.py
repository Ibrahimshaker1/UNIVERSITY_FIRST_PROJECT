import tkinter as tk
from tkinter import messagebox
import datetime as dt
import json
import smtplib
import os
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
# smtp
email = "testemailforprogramming892@gmail.com"
password = "oeiamtoxskecviba"
sheet_url = "https://api.sheety.co/3de9a3e3bed011fd366e5e92a6b0475c/logLasFile/sheet1"
username = "ibrahim829"
sheet_password = os.environ.get("ENV_PASS")
basic = HTTPBasicAuth(username, sheet_password)
sheet_headers = {
    "Authorization": "Basic aWJyYWhpbTgyOToxMEAyMEAzMEA="
}
# Data
data = pd.read_csv("data.csv")
data = data.to_dict()
data_depth = data['    DEPTH']
data_RHOB = data['    RHOB']
data_NPHI = data['             NPHI']
data_CALI = data['             CALI']
data_GR = data['             GR']
data_DT = data['               DT']
data_SP = data['               SP']
data_SFLU = data['               SFLU']
data_ILM = data['             ILM']
data_ILD = data['              ILD']
data_depth_list = []
for key in data_depth:
    data_depth_list.append(data_depth[key])
data_RHOB_list = []
for key in data_RHOB:
    data_RHOB_list.append(data_RHOB[key])
data_NPHI_list = []
for key in data_NPHI:
    data_NPHI_list.append(data_NPHI[key])
data_CALI_list = []
for key in data_CALI:
    data_CALI_list.append(data_CALI[key])
data_GR_list = []
for key in data_GR:
    data_GR_list.append(data_GR[key])
data_DT_list = []
for key in data_DT:
    data_DT_list.append(data_DT[key])
data_sp_lsit = []
for key in data_SP:
    data_sp_lsit.append(data_SP[key])
data_SFLU_list = []
for key in data_SFLU:
    data_SFLU_list.append(data_SFLU[key])
data_ILM_list = []
for key in data_ILM:
    data_ILM_list.append(data_ILM[key])
data_ILD_list = []
for key in data_ILD:
    data_ILD_list.append(data_ILD[key])
# make the GUI
window_color = "#006666"
canvas_1_color = "#000000"
window = tk.Tk()
window.title("AAM5 Well Log")
window.config(width=500, height=500, padx=20, pady=20)
window.configure(background=window_color)
# functions
def measurementt():
    depth = Depth_entry.get()
    depth_int = int(depth)
    if depth_int in data_depth_list:
        index = data_depth_list.index(depth_int)
        RHOB = data_RHOB_list[index]
        NPHI = data_NPHI_list[index]
        CARLI = data_CALI_list[index]
        GR = data_GR_list[index]
        DT = data_DT_list[index]
        SP = data_sp_lsit[index]
        SFLU = data_SFLU_list[index]
        ILM = data_ILM_list[index]
        ILD = data_ILD_list[index]
        RHOB_entry.insert(0, RHOB)
        NPHI_entry.insert(0, NPHI)
        CARLI_entry.insert(0, CARLI)
        GR_entry.insert(0, GR)
        DT_entry.insert(0, DT)
        SP_entry.insert(0, SP)
        SFLU_entry.insert(0, SFLU)
        ILM_entry.insert(0, ILM)
        ILD_entry.insert(0, ILD)
    else:
        is_ok = messagebox.showinfo(message="Sorry there is no data at this depth")
        if is_ok:
            Depth_entry.delete(0, len(depth))
def delete_func():
    yes = messagebox.askyesno(message="DO You Want To Delete The Results")
    if yes:
        Depth_entry.delete(0, len(Depth_entry.get()))
        RHOB_entry.delete(0, len(RHOB_entry.get()))
        NPHI_entry.delete(0, len(NPHI_entry.get()))
        CARLI_entry.delete(0, len(CARLI_entry.get()))
        GR_entry.delete(0, len(GR_entry.get()))
        DT_entry.delete(0, len(DT_entry.get()))
        SP_entry.delete(0, len(SP_entry.get()))
        SFLU_entry.delete(0, len(SFLU_entry.get()))
        ILM_entry.delete(0, len(ILM_entry.get()))
        ILD_entry.delete(0, len(ILD_entry.get()))
        pma_entry.delete(0, len(pma_entry.get()))
        pt_entry.delete(0, len(pt_entry.get()))
        tma_entry.delete(0, len(tma_entry.get()))
        tf_entry.delete(0, len(tf_entry.get()))
        denstiy_entry.delete(0, len(denstiy_entry.get()))
        sonic_entry.delete(0, len(sonic_entry.get()))
        effective_entry.delete(0, len(effective_entry.get()))
def porosity_meauser():
    pma = float(pma_entry.get())
    pt = float(pt_entry.get())
    tma = float(tma_entry.get())
    tf = float(tf_entry.get())
    density_porosity = (pma - float(RHOB_entry.get())) / (pma - pt)
    sonic_porosity = (float(DT_entry.get())-tma)/(tf-tma)
    effective_porosity = (float(NPHI_entry.get())+density_porosity)/2
    denstiy_entry.insert(0, density_porosity)
    sonic_entry.insert(0, sonic_porosity)
    effective_entry.insert(0, effective_porosity)
def save_f():
    date = dt.datetime.now()
    date_list = [date.day, date.month, date.year]
    date_list_str = str(date_list)[1:-1]
    depth = Depth_entry.get()
    NPHI = NPHI_entry.get()
    RHOB = RHOB_entry.get()
    DT = Depth_entry.get()
    SP = SP_entry.get()
    GR = GR_entry.get()
    CARLI = CARLI_entry.get()
    SFLU = SFLU_entry.get()
    ILM = ILM_entry.get()
    ILD = ILD_entry.get()
    denstiy = denstiy_entry.get()
    sonic = sonic_entry.get()
    effective = effective_entry.get()
    new_data = {
        date_list_str: {
            "date of process": date_list_str,
            "Depth": depth,
            "NPHI": NPHI,
            "RHOB": RHOB,
            "DT": DT,
            "SP": SP,
            "GR": GR,
            "CARLI": CARLI,
            "SFLU": SFLU,
            "ILM": ILM,
            "ILD": ILD,
            "density porosity": denstiy,
            "sonic porosity": sonic,
            "effective porosity": effective
        }
    }
    is_ok = messagebox.askyesno(title="Save Data", message="DO you wont to save the data")
    if is_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=16)

        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=16)
def show_data():
    try:
        data_date = show_data_entry.get()
        with open("data.json", "r") as file:
            data = json.load(file)
            data_dic = data[data_date]
            messagebox.showinfo(
                title=f"data of the well at Date:{data_date}",
                message=f"""the Data of the well\nDate of process:{data_dic['date of process']}\nDepth:{data_dic['Depth']}\nNPHI:{data_dic['NPHI']}\nRHOB:{data_dic['RHOB']}\nDT:{data_dic['DT']}
                            \nSP:{data_dic['SP']}\nGR:{data_dic['GR']}\nCARLI:{data_dic['CARLI']}\nSFLU:{data_dic['SFLU']}\nILM:{data_dic['ILM']}\nILD:{data_dic['ILD']}
                            \ndensity porosity:{data_dic['density porosity']}\nsonic porosity:{data_dic['sonic porosity']}\neffective porosity:{data_dic['effective porosity']}
                        
                        
                        """
            )
    except FileNotFoundError and KeyError:
        messagebox.showinfo(title="Error", message="There is no data saved yet or no data at this input Date")
def send_email():
    try:
        date_date = show_data_entry.get()
        with open("data.json", "r") as file:
            data = json.load(file)
            data_dic = data[date_date]
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=Email_entry.get(),
                msg=f"""subject:well report\n\nthe Data of the well\nDate of process:{data_dic['date of process']}\nDepth:{data_dic['Depth']}\nNPHI:{data_dic['NPHI']}\nRHOB:{data_dic['RHOB']}\nDT:{data_dic['DT']}
                            \nSP:{data_dic['SP']}\nGR:{data_dic['GR']}\nCARLI:{data_dic['CARLI']}\nSFLU:{data_dic['SFLU']}\nILM:{data_dic['ILM']}\nILD:{data_dic['ILD']}
                            \ndensity porosity:{data_dic['density porosity']}\nsonic porosity:{data_dic['sonic porosity']}\neffective porosity:{data_dic['effective porosity']}
                        
                        
                        """
            )
            connection.close()
    except KeyError:
        with open("data.json", "r") as file:
            date = dt.datetime.now()
            date_list = [date.day, date.month, date.year]
            data_date = str(date_list)[1:-1]
            data = json.load(file)
            data_dic = data[data_date]
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=Email_entry.get(),
                msg=f"""subject:well report\n\nthe Data of the well\nDate of process:{data_dic['date of process']}\nDepth:{data_dic['Depth']}\nNPHI:{data_dic['NPHI']}\nRHOB:{data_dic['RHOB']}\nDT:{data_dic['DT']}
                                   \nSP:{data_dic['SP']}\nGR:{data_dic['GR']}\nCARLI:{data_dic['CARLI']}\nSFLU:{data_dic['SFLU']}\nILM:{data_dic['ILM']}\nILD:{data_dic['ILD']}
                                   \ndensity porosity:{data_dic['density porosity']}\nsonic porosity:{data_dic['sonic porosity']}\neffective porosity:{data_dic['effective porosity']}


                               """
            )
            connection.close()
def cloud_save():
    date = dt.datetime.now().date().strftime("%d/%m/%y")
    depth = Depth_entry.get()
    NPHI = NPHI_entry.get()
    RHOB = RHOB_entry.get()
    DT = Depth_entry.get()
    SP = SP_entry.get()
    GR = GR_entry.get()
    CARLI = CARLI_entry.get()
    SFLU = SFLU_entry.get()
    ILM = ILM_entry.get()
    ILD = ILD_entry.get()
    sheet_input = {
        "sheet1": {
            "date": date,
            "depth": depth,
            "nphi": NPHI,
            "rhob": RHOB,
            "dt": DT,
            "sp": SP,
            "gr": GR,
            "carli": CARLI,
            "sflu": SFLU,
            "ilm": ILM,
            "ild": ILD,
        }
    }
    response = requests.post(url=sheet_url, json=sheet_input, auth=basic, headers=sheet_headers)
    print(response.text)
# logo
logo = tk.PhotoImage(file="logo_2.png")
button_image = tk.PhotoImage(file="bu.png")
delete_button_image = tk.PhotoImage(file="delete_image.png")
porosity_measure_image = tk.PhotoImage(file="porosity_measure_image.png")
save_button_image = tk.PhotoImage(file="save_button_image.png")
show_button_image = tk.PhotoImage(file="show_button_image.png")
send_button_image = tk.PhotoImage(file="send_button_image.png")
cloud_button_image = tk.PhotoImage(file="cloud_save_image.png")
canvas_logo_1 = tk.Canvas(width=64, height=64)
canvas_logo_1.config(background=window_color, highlightthickness=0)
text_1 = canvas_logo_1.create_text(
    30,
    30,
    text="U.O.T",
    font=("Calibri", 20, "bold"),
    fill="white"
    )
canvas_logo_1.grid(column=0, row=0)
canvas_logo_2 = tk.Canvas(width=64, height=64, highlightthickness=0, background=window_color)
canvas_logo_2.create_image(32, 32, image=logo)
canvas_logo_2.grid(column=8, row=0)

# label
Depth = tk.Label()
Depth.config(pady=10, text="Depth:", font=("Calibri", 13, "bold"), bg=window_color, highlightthickness=0)
Depth.grid(column=0, row=1)
Porosity_label = tk.Label(pady=10, text="Porosity Log:", font=("Calibri", 15, "bold"), background=window_color, highlightthickness=0)
Porosity_label.grid(column=0, row=2, columnspan=2)
NPHI_label = tk.Label(pady=10, text="NPHI:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
NPHI_label.grid(column=0, row=3)
RHOB_label = tk.Label(pady=10, text="RHOB:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
RHOB_label.grid(column=0, row=4)
DT_label = tk.Label(pady=10, text="DT:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
DT_label.grid(column=0, row=5)
lithology_label = tk.Label(padx=90, text="Lithology Log:", font=("Calibri", 15, "bold"), background=window_color, highlightthickness=0)
lithology_label.grid(column=4, row=2, columnspan=2)
SP_label = tk.Label(text="SP:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
SP_label.grid(column=3, row=3, columnspan=2, sticky="E")
GR_label = tk.Label(text="GR:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
GR_label.grid(column=3, row=4, columnspan=2, sticky="E")
CARLI_label = tk.Label(text="CARLI:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
CARLI_label.grid(column=3, row=5, columnspan=2, sticky="E")
resistivity_label = tk.Label(text="Resistivity:", font=("Calibri", 15, "bold"), background=window_color, highlightthickness=0)
resistivity_label.grid(column=7, row=2, columnspan=2)
SFLU_label = tk.Label(text="SFLU:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
SFLU_label.grid(column=6, row=3, columnspan=2, sticky="E")
ILM_label = tk.Label(text="ILM:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
ILM_label.grid(column=6, row=4, columnspan=2, sticky="E")
ILD_label = tk.Label(text="ILD:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
ILD_label.grid(column=6, row=5, columnspan=2, sticky="E")
porosity_label = tk.Label(text="Measurement:", font=("Calibri", 15, "bold"), background=window_color, highlightthickness=0)
porosity_label.grid(column=4, row=6, columnspan=2)
constant_label = tk.Label(text="Constants:", font=("Calibri", 15, "bold"), background=window_color, highlightthickness=0)
constant_label.grid(column=0, row=7, columnspan=2)
pma_label = tk.Label(pady=10, text="ρma:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
pma_label.grid(column=0, row=8)
pf_label = tk.Label(pady=10, text="ρt:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
pf_label.grid(column=0, row=9)
tma_label = tk.Label(pady=10, text="Δtma:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
tma_label.grid(column=0, row=10)
tf_label = tk.Label(pady=10, text="Δtf:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
tf_label.grid(column=0, row=11)
denstiy_label = tk.Label(text="ΦD:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
denstiy_label.grid(column=4, row=8, sticky="E")
sonic_label = tk.Label(text="ΦS:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
sonic_label.grid(column=4, row=9, sticky="E")
effective_label = tk.Label(text="ΦE:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
effective_label.grid(column=4, row=10, sticky="E")
Email_label = tk.Label(text="Email:", font=("Calibri", 13, "bold"), background=window_color, highlightthickness=0)
Email_label.grid(column=0, row=12)
# Entry
Depth_entry = tk.Entry()
Depth_entry.focus()
Depth_entry.config(bg=window_color, width=10, highlightthickness=0)
Depth_entry.grid(column=1, row=1, sticky="W")
NPHI_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
NPHI_entry.grid(column=1, row=3)
RHOB_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
RHOB_entry.grid(column=1, row=4)
DT_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
DT_entry.grid(column=1, row=5)
SP_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
SP_entry.grid(column=5, row=3, sticky="w")
GR_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
GR_entry.grid(column=5, row=4, sticky="w")
CARLI_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
CARLI_entry.grid(column=5, row=5, sticky="w")
SFLU_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
SFLU_entry.grid(column=8, row=3, sticky="W")
ILM_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
ILM_entry.grid(column=8, row=4, sticky="W")
ILD_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
ILD_entry.grid(column=8, row=5, sticky="W")
pma_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
pma_entry.grid(column=1, row=8)
pt_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
pt_entry.grid(column=1, row=9)
tma_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
tma_entry.grid(column=1, row=10)
tf_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
tf_entry.grid(column=1, row=11)
denstiy_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
denstiy_entry.grid(column=5, row=8, sticky="W")
sonic_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
sonic_entry.grid(column=5, row=9, sticky="W")
effective_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
effective_entry.grid(column=5, row=10, sticky="W")
show_data_entry = tk.Entry(background=window_color, width=15, highlightthickness=0)
show_data_entry.insert(0, string="dd, mm, yy")
show_data_entry.grid(column=7, row=8, sticky="W", columnspan=2)
Email_entry = tk.Entry(background=window_color, width=40, highlightthickness=0)
Email_entry.grid(column=1, row=12, columnspan=5, sticky="W")
# button
measure_button = tk.Button(image=button_image, background=window_color, highlightthickness=0, command=measurementt)
measure_button.grid(column=4, row=1, sticky="W")
delete_button = tk.Button(image=delete_button_image, background=window_color, highlightthickness=0, command=delete_func)
delete_button.grid(column=8, row=1)
porosity_measure_button = tk.Button(image=porosity_measure_image, background=window_color, highlightthickness=0, command=porosity_meauser)
porosity_measure_button.grid(column=5, row=11, sticky="W")
save_button = tk.Button(image=save_button_image, background=window_color, highlightthickness=0, command=save_f)
save_button.grid(column=6, row=1)
show_data = tk.Button(image=show_button_image, background=window_color, highlightthickness=0, command=show_data)
show_data.grid(column=6, row=8)
send_button = tk.Button(image=send_button_image, background=window_color, highlightthickness=0, command=send_email)
send_button.grid(column=6, row=9)
cloud_button = tk.Button(image=cloud_button_image, background=window_color, highlightthickness=0, command=cloud_save)
cloud_button.grid(row=1, column=5)

window.mainloop()
