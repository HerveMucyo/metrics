import random
from tkinter import Tk, Label, Entry, Text

class MiniTerminal:
  def __init__(self, master):
    self.master = master
    master.title("Mini Terminal")

    # Current directory label
    self.current_dir_label = Label(master, text="user@machine:~$ ")
    self.current_dir_label.pack(side="left")

    # User input field
    self.user_input = Entry(master, width=50)
    self.user_input.bind("<Return>", self.handle_command)
    self.user_input.pack(side="left", fill="x", expand=True)

    # Output text widget
    self.output_text = Text(master, height=10, state="disabled")
    self.output_text.pack(fill="both", expand=True)

    # Packet loss rate label
    self.packet_loss_label = Label(master, text="Packet Loss: N/A")
    self.packet_loss_label.pack(side="right")

    # Update packet loss rate periodically (simulated)
    self.master.after(1000, self.update_packet_loss)  # Update every second

  def handle_command(self, event):
    # Get user input and simulate processing
    command = self.user_input.get()
    output = f"Executing command: {command}\n"

    # Update output text and clear user input
    self.output_text.config(state="normal")
    self.output_text.insert("end", output)
    self.output_text.see("end")
    self.output_text.config(state="disabled")
    self.user_input.delete(0, "end")

  def update_packet_loss(self):
    # Simulate packet loss (replace with actual measurement)
    packet_loss = random.randint(0, 10)  # Random value between 0% and 10%

    # Update packet loss label
    self.packet_loss_label.config(text=f"Packet Loss: {packet_loss}%")

    # Schedule next update
    self.master.after(1000, self.update_packet_loss)

# Create the main window and run the application
root = Tk()
app = MiniTerminal(root)
root.mainloop()
