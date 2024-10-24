import PySimpleGUI as sg
sg.theme("DarkGreen5")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM    : 2210010376")],
                           [sg.Text("Nama   : Rahmi Hidayah")],
                           [sg.Text("Kelas  : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul : Pemrograman Visual 3")],
                           ],
                           size=(510,200),
                           font=("Times", 18))
window()
window.close()