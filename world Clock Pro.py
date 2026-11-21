
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from zoneinfo import ZoneInfo

# ==========================================
# WORLD CLOCK PRO - PREMIUM DESKTOP PROJECT
# ==========================================

class WorldClockPro:

    def __init__(self, root):
        self.root = root
        self.root.title("World Clock Pro | Global Dashboard")
        self.root.geometry("1100x750")
        self.root.minsize(850, 600)
        self.root.configure(bg="#101827")

        self.is_24_hour = True

        self.timezones = {
            "India 🇮🇳": "Asia/Kolkata",
            "New York 🇺🇸": "America/New_York",
            "London 🇬🇧": "Europe/London",
            "Dubai 🇦🇪": "Asia/Dubai",
            "Tokyo 🇯🇵": "Asia/Tokyo",
            "South Korea 🇰🇷": "Asia/Seoul",
            "Singapore 🇸🇬": "Asia/Singapore",
            "Moscow 🇷🇺": "Europe/Moscow",
            "Sydney 🇦🇺": "Australia/Sydney",
            "Germany 🇩🇪": "Europe/Berlin",
            "Toronto 🇨🇦": "America/Toronto",
            "Paris 🇫🇷": "Europe/Paris"
        }

        self.selected_cities = [
            "India 🇮🇳",
            "New York 🇺🇸",
            "London 🇬🇧",
            "Dubai 🇦🇪",
            "Tokyo 🇯🇵",
            "Singapore 🇸🇬"
        ]

        self.clock_labels = {}

        self.setup_ui()
        self.update_clock()

    # HEADER

    def setup_ui(self):

        header = tk.Frame(
            self.root,
            bg="#172438",
            height=135
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🌍 WORLD CLOCK PRO",
            font=("Arial", 28, "bold"),
            fg="#ffffff",
            bg="#172438"
        ).pack(pady=(20, 5))

        tk.Label(
            header,
            text="GLOBAL TIME ZONE MANAGEMENT SYSTEM",
            font=("Arial", 10, "bold"),
            fg="#36d6c2",
            bg="#172438"
        ).pack()

        self.local_time = tk.Label(
            header,
            text="",
            font=("Arial", 12),
            fg="#ffffff",
            bg="#172438"
        )
        self.local_time.pack(pady=12)

        # CONTROL PANEL

        control = tk.Frame(
            self.root,
            bg="#101827"
        )
        control.pack(fill="x", padx=25, pady=20)

        tk.Label(
            control,
            text="ADD NEW CITY",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#101827"
        ).pack(side="left")

        self.city_box = ttk.Combobox(
            control,
            values=list(self.timezones.keys()),
            state="readonly",
            width=22
        )
        self.city_box.pack(side="left", padx=12)
        self.city_box.set("Select City")

        tk.Button(
            control,
            text="+ ADD CITY",
            command=self.add_city,
            bg="#167dce",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=9,
            cursor="hand2"
        ).pack(side="left")

        tk.Button(
            control,
            text="12 / 24 HOUR",
            command=self.toggle_format,
            bg="#263750",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=9,
            cursor="hand2"
        ).pack(side="right")

        # CLOCK CARDS

        self.clock_frame = tk.Frame(
            self.root,
            bg="#101827"
        )
        self.clock_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # FOOTER

        footer = tk.Frame(
            self.root,
            bg="#172438",
            height=45
        )
        footer.pack(fill="x", side="bottom")

        tk.Label(
            footer,
            text="WORLD CLOCK PRO  |  DEVELOPED WITH PYTHON",
            font=("Arial", 9, "bold"),
            fg="#8fa8c9",
            bg="#172438"
        ).pack(pady=13)

        self.refresh_cards()

    # CREATE CITY CARDS

    def refresh_cards(self):

        for widget in self.clock_frame.winfo_children():
            widget.destroy()

        self.clock_labels = {}

        for index, city in enumerate(self.selected_cities):

            row = index // 3
            col = index % 3

            card = tk.Frame(
                self.clock_frame,
                bg="#1c2a40",
                highlightbackground="#30445f",
                highlightthickness=1
            )

            card.grid(
                row=row,
                column=col,
                padx=10,
                pady=12,
                sticky="nsew"
            )

            self.clock_frame.grid_columnconfigure(
                col, weight=1
            )

            self.clock_frame.grid_rowconfigure(
                row, weight=1
            )

            tk.Label(
                card,
                text="🌐 " + city,
                font=("Arial", 14, "bold"),
                fg="white",
                bg="#1c2a40"
            ).pack(pady=(20, 10))

            time_label = tk.Label(
                card,
                text="00:00:00",
                font=("Arial", 25, "bold"),
                fg="#36d6c2",
                bg="#1c2a40"
            )
            time_label.pack(pady=10)

            date_label = tk.Label(
                card,
                text="Loading...",
                font=("Arial", 10),
                fg="#a9bad0",
                bg="#1c2a40"
            )
            date_label.pack(pady=5)

            tk.Label(
                card,
                text=self.timezones[city],
                font=("Arial", 9),
                fg="#8298b5",
                bg="#1c2a40"
            ).pack(pady=5)

            tk.Button(
                card,
                text="REMOVE CITY",
                command=lambda c=city: self.remove_city(c),
                bg="#a33348",
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                cursor="hand2",
                padx=10,
                pady=6
            ).pack(pady=(10, 18))

            self.clock_labels[city] = (
                time_label,
                date_label
            )

    # ADD CITY

    def add_city(self):

        city = self.city_box.get()

        if city not in self.timezones:
            messagebox.showwarning(
                "Warning",
                "Please select a city first."
            )
            return

        if city in self.selected_cities:
            messagebox.showinfo(
                "Already Added",
                "This city is already added."
            )
            return

        self.selected_cities.append(city)
        self.refresh_cards()

    # REMOVE CITY

    def remove_city(self, city):

        if city in self.selected_cities:
            self.selected_cities.remove(city)

        self.refresh_cards()

    # CHANGE TIME FORMAT

    def toggle_format(self):

        self.is_24_hour = not self.is_24_hour
        self.update_clock()

    # LIVE CLOCK ENGINE

    def update_clock(self):

        local_now = datetime.now().astimezone()

        self.local_time.config(
            text="YOUR LOCAL TIME: " +
            local_now.strftime("%d %B %Y | %I:%M:%S %p")
        )

        for city in self.selected_cities:

            try:
                current = datetime.now(
                    ZoneInfo(self.timezones[city])
                )

                if self.is_24_hour:
                    time_text = current.strftime("%H:%M:%S")
                else:
                    time_text = current.strftime("%I:%M:%S %p")

                date_text = current.strftime("%A, %d %B %Y")

                time_label, date_label = self.clock_labels[city]

                time_label.config(text=time_text)
                date_label.config(text=date_text)

            except Exception as error:
                self.clock_labels[city][0].config(
                    text="Time unavailable"
                )

        self.root.after(1000, self.update_clock)


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = WorldClockPro(root)

    root.mainloop()
