import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledText

class UptimeBot(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill="both", expand=True, side=TOP)
        ttk.Style().configure("TButton", font="TkFixedFont 15")

        button_frame = ttk.Frame(self, style="dark")
        button_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        initiate_btn = ttk.Button(button_frame, style="success", text="Start")
        initiate_btn.pack(fill="both", side=LEFT)

        settings_btn = ttk.Button(button_frame, style="info", text="Settings")
        settings_btn.pack(fill="both",side=LEFT)

        logo_label = ttk.Label(button_frame, text="UptimeBot", style="inverse-dark")
        logo_label.configure(font=("Arial", 16, "bold"))
        logo_label.pack(fill="x", side=RIGHT, padx=30)

        url_frame = ttk.Frame(self)
        url_frame.grid(row= 1, column= 0, sticky="nsew")

        url_label = ttk.Label(url_frame, text="Site URL", style="inverse-primary")
        url_label.configure(font=("Arial", 16, "bold"))
        url_label.pack(fill="both", expand=True, side=TOP)

        url_entry = ttk.Entry(url_frame)
        url_entry.pack(fill="both", expand=True, padx=30, pady=30)

        url_actions = ttk.Frame(url_frame)
        url_actions.pack(fill="both", expand=True)

        url_submit = ttk.Button(url_actions, text="Submit", style="success")
        url_submit.pack(side=LEFT, padx=30, pady=10)

        summary_frame = ttk.Frame(self)
        summary_frame.grid(row=2, column=0, sticky="nsew")

        summary_label = ttk.Label(summary_frame, text="Summary", style="inverse-primary")
        summary_label.configure(font=("Arial", 16, "bold"))
        summary_label.pack(fill="both", expand=True, side=TOP)

        summary_meter = ttk.Meter(summary_frame, bootstyle="info", textright="%", subtext="Uptime", amountused=100, interactive=False)
        summary_meter.pack(fill="both", expand=True, side=TOP, pady=30, padx=30)

        history_frame = ttk.Frame(self)
        history_frame.grid(row=1, column=1, rowspan=2, sticky="nsew")

        history_info = ttk.Frame(history_frame, style="primary")
        history_info.pack(fill="both", expand=True, side=TOP)

        history_label = ttk.Label(history_info, text="History", style="inverse-primary")
        history_label.configure(font=("Arial", 16, "bold"))
        history_label.pack(side=LEFT)

        history_downlaod = ttk.Button(history_info, text="Download", style="info")
        history_downlaod.pack(side=RIGHT, fill="both")

        coldata = [
            {"text": "Timestamp", "stretch": True},
            {"text": "URL", "stretch": True},
            {"text": "Response Code", "stretch": True},
            {"text": "Response Time (ms)", "stretch": True},
        ]

        rowdata = [
            ('10/2/23 09:00:00','google.com', '200 (OK)', 700),
            ('10/2/23 09:00:30', 'google.com', '200 (OK)', 1200),
            ('10/2/23 09:01:00', 'google.com', '200 (OK)', 800),
        ]

        history_table = Tableview(
            master=history_frame,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            bootstyle=PRIMARY,
        )

        history_table.pack(fill="both", expand=True, side=TOP)

        history_log = ttk.Label(history_frame, text="Log", style="inverse-primary")
        history_log.configure(font=("Arial", 16, "bold"))
        history_log.pack(fill="both", expand=True)

        history_log = ScrolledText(history_frame, padding=5, height=10, autohide=True)
        history_log.pack(fill="both", expand=True)
        history_log.insert(END, "10/2/23 09:00:00 \t\t Response from google.com: 200 (OK)\n")
        history_log.insert(END, "10/2/23 09:00:30 \t\t Response from google.com: 200 (OK)\n")
        history_log.insert(END, "10/2/23 09:01:00 \t\t Response from google.com: 200 (OK)")

        self.columnconfigure(index=0, weight=3)
        self.columnconfigure(index=1, weight=7)

        self.rowconfigure(index=0, weight=2)
        self.rowconfigure(index=1, weight=4)
        self.rowconfigure(index=2, weight=4)


if __name__ == "__main__":
    app = ttk.Window("UptimeBot", themename="sandstone")
    UptimeBot(app)
    app.mainloop()
