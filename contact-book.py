import tkinter as tk


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("390x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.contacts = {}

        self.create_ui()
        self.show_home()

    # ---------------- UI ----------------

    def create_ui(self):

        # Top bar
        self.top_bar = tk.Frame(
            self.root,
            bg="#202124",
            height=70
        )
        self.top_bar.pack(fill="x")
        self.top_bar.pack_propagate(False)

        self.title = tk.Label(
            self.top_bar,
            text="Contact Book",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#202124"
        )
        self.title.pack(side="left", padx=22)

        # Main content
        self.content = tk.Frame(
            self.root,
            bg="#f5f5f5"
        )
        self.content.pack(
            fill="both",
            expand=True
        )

        # Bottom navigation
        self.nav = tk.Frame(
            self.root,
            bg="white",
            height=70
        )
        self.nav.pack(fill="x")
        self.nav.pack_propagate(False)

        self.home_btn = tk.Button(
            self.nav,
            text="⌂\nHome",
            font=("Arial", 9),
            bg="white",
            fg="#202124",
            relief="flat",
            command=self.show_home
        )
        self.home_btn.pack(
            side="left",
            expand=True,
            fill="both"
        )

        self.add_btn = tk.Button(
            self.nav,
            text="+\nAdd",
            font=("Arial", 9),
            bg="white",
            fg="#202124",
            relief="flat",
            command=self.show_add
        )
        self.add_btn.pack(
            side="left",
            expand=True,
            fill="both"
        )

        self.search_btn = tk.Button(
            self.nav,
            text="⌕\nSearch",
            font=("Arial", 9),
            bg="white",
            fg="#202124",
            relief="flat",
            command=self.show_search
        )
        self.search_btn.pack(
            side="left",
            expand=True,
            fill="both"
        )

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ---------------- HOME ----------------

    def show_home(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Your Contacts",
            font=("Arial", 22, "bold"),
            bg="#f5f5f5",
            fg="#202124"
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 5)
        )

        tk.Label(
            self.content,
            text=f"{len(self.contacts)} saved contact(s)",
            font=("Arial", 10),
            bg="#f5f5f5",
            fg="#777777"
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        if not self.contacts:

            tk.Label(
                self.content,
                text="No contacts yet",
                font=("Arial", 15),
                bg="#f5f5f5",
                fg="#777777"
            ).pack(pady=100)

            tk.Button(
                self.content,
                text="+  Add your first contact",
                font=("Arial", 11, "bold"),
                bg="#202124",
                fg="white",
                relief="flat",
                padx=15,
                pady=10,
                command=self.show_add
            ).pack()

            return

        # Contact list
        list_frame = tk.Frame(
            self.content,
            bg="#f5f5f5"
        )
        list_frame.pack(
            fill="both",
            expand=True,
            padx=20
        )

        for name, details in self.contacts.items():

            card = tk.Frame(
                list_frame,
                bg="white",
                height=75
            )
            card.pack(
                fill="x",
                pady=6
            )

            initial = name[0].upper()

            avatar = tk.Label(
                card,
                text=initial,
                font=("Arial", 16, "bold"),
                width=3,
                height=2,
                bg="#e8eaed",
                fg="#202124"
            )
            avatar.pack(
                side="left",
                padx=10,
                pady=8
            )

            info = tk.Frame(
                card,
                bg="white"
            )
            info.pack(
                side="left",
                fill="both",
                expand=True,
                pady=10
            )

            tk.Label(
                info,
                text=name,
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#202124"
            ).pack(anchor="w")

            tk.Label(
                info,
                text=details["phone"],
                font=("Arial", 9),
                bg="white",
                fg="#777777"
            ).pack(anchor="w")

            tk.Button(
                card,
                text="⋮",
                font=("Arial", 16),
                bg="white",
                fg="#555555",
                relief="flat",
                command=lambda n=name: self.show_options(n)
            ).pack(
                side="right",
                padx=10
            )

    # ---------------- ADD CONTACT ----------------

    def show_add(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="New Contact",
            font=("Arial", 22, "bold"),
            bg="#f5f5f5",
            fg="#202124"
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 30)
        )

        self.name_entry = self.create_entry(
            "Name"
        )

        self.phone_entry = self.create_entry(
            "Phone Number"
        )

        self.email_entry = self.create_entry(
            "Email"
        )

        tk.Button(
            self.content,
            text="Save Contact",
            font=("Arial", 11, "bold"),
            bg="#202124",
            fg="white",
            relief="flat",
            padx=20,
            pady=12,
            command=self.save_contact
        ).pack(
            pady=30
        )

    def create_entry(self, label_text):

        frame = tk.Frame(
            self.content,
            bg="#f5f5f5"
        )
        frame.pack(
            fill="x",
            padx=25,
            pady=8
        )

        tk.Label(
            frame,
            text=label_text,
            font=("Arial", 9),
            bg="#f5f5f5",
            fg="#666666"
        ).pack(anchor="w")

        entry = tk.Entry(
            frame,
            font=("Arial", 12),
            bg="white",
            fg="#202124",
            relief="flat"
        )
        entry.pack(
            fill="x",
            ipady=10,
            pady=4
        )

        return entry

    def save_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone:

            self.show_message(
                "Please enter a name and phone number."
            )
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email
        }

        self.show_home()

    # ---------------- SEARCH ----------------

    def show_search(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Search",
            font=("Arial", 22, "bold"),
            bg="#f5f5f5",
            fg="#202124"
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        search_entry = tk.Entry(
            self.content,
            font=("Arial", 13),
            bg="white",
            relief="flat"
        )
        search_entry.pack(
            fill="x",
            padx=25,
            ipady=12
        )

        results = tk.Frame(
            self.content,
            bg="#f5f5f5"
        )
        results.pack(
            fill="both",
            expand=True,
            pady=20
        )

        def search():

            for widget in results.winfo_children():
                widget.destroy()

            query = search_entry.get().lower()

            found = False

            for name, details in self.contacts.items():

                if (
                    query in name.lower()
                    or query in details["phone"]
                ):

                    found = True

                    card = tk.Frame(
                        results,
                        bg="white"
                    )
                    card.pack(
                        fill="x",
                        padx=25,
                        pady=5
                    )

                    tk.Label(
                        card,
                        text=name,
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg="#202124"
                    ).pack(
                        anchor="w",
                        padx=15,
                        pady=(10, 0)
                    )

                    tk.Label(
                        card,
                        text=details["phone"],
                        font=("Arial", 10),
                        bg="white",
                        fg="#777777"
                    ).pack(
                        anchor="w",
                        padx=15,
                        pady=(0, 10)
                    )

            if not found:

                tk.Label(
                    results,
                    text="No contacts found.",
                    font=("Arial", 11),
                    bg="#f5f5f5",
                    fg="#777777"
                ).pack(pady=50)

        tk.Button(
            self.content,
            text="Search",
            font=("Arial", 10, "bold"),
            bg="#202124",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            command=search
        ).pack(pady=10)

    # ---------------- OPTIONS ----------------

    def show_options(self, name):

        popup = tk.Toplevel(self.root)
        popup.title(name)
        popup.geometry("300x250")
        popup.resizable(False, False)
        popup.configure(bg="white")

        tk.Label(
            popup,
            text=name,
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#202124"
        ).pack(pady=20)

        tk.Button(
            popup,
            text="Edit Contact",
            width=20,
            command=lambda: [
                popup.destroy(),
                self.edit_contact(name)
            ]
        ).pack(pady=5)

        tk.Button(
            popup,
            text="Delete Contact",
            width=20,
            command=lambda: [
                popup.destroy(),
                self.delete_contact(name)
            ]
        ).pack(pady=5)

        tk.Button(
            popup,
            text="Close",
            width=20,
            command=popup.destroy
        ).pack(pady=5)

    # ---------------- EDIT ----------------

    def edit_contact(self, name):

        self.clear_content()

        details = self.contacts[name]

        tk.Label(
            self.content,
            text="Edit Contact",
            font=("Arial", 22, "bold"),
            bg="#f5f5f5",
            fg="#202124"
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 30)
        )

        self.name_entry = self.create_entry("Name")
        self.name_entry.insert(0, name)

        self.phone_entry = self.create_entry("Phone Number")
        self.phone_entry.insert(0, details["phone"])

        self.email_entry = self.create_entry("Email")
        self.email_entry.insert(0, details["email"])

        tk.Button(
            self.content,
            text="Update Contact",
            font=("Arial", 11, "bold"),
            bg="#202124",
            fg="white",
            relief="flat",
            padx=20,
            pady=12,
            command=lambda: self.update_contact(name)
        ).pack(pady=30)

    def update_contact(self, old_name):

        new_name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not new_name or not phone:

            self.show_message(
                "Name and phone number are required."
            )
            return

        del self.contacts[old_name]

        self.contacts[new_name] = {
            "phone": phone,
            "email": email
        }

        self.show_home()

    # ---------------- DELETE ----------------

    def delete_contact(self, name):

        del self.contacts[name]

        self.show_home()

    # ---------------- MESSAGE ----------------

    def show_message(self, message):

        popup = tk.Toplevel(self.root)
        popup.title("Contact Book")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.configure(bg="white")

        tk.Label(
            popup,
            text=message,
            font=("Arial", 11),
            bg="white",
            fg="#202124",
            wraplength=250
        ).pack(
            pady=30
        )

        tk.Button(
            popup,
            text="OK",
            width=10,
            command=popup.destroy
        ).pack()


# ---------------- RUN PROGRAM ----------------

root = tk.Tk()

app = ContactBook(root)

root.mainloop()