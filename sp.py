import tkinter as tk  # Import Tkinter for GUI
from speedtest import Speedtest  # Import Speedtest for speed measurement

# Function to perform the speed test and update labels
def update_speed():
    speed_test = Speedtest()
    download = speed_test.download()  # Get download speed in bytes/second
    upload = speed_test.upload()  # Get upload speed in bytes/second

    # Convert speeds to Mbps and round to two decimal places
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    # Update the labels with the results
    download_label.config(text=f"Download Speed: {download_speed} Mbps", bg="blue")
    upload_label.config(text=f"Upload Speed: {upload_speed} Mbps")

# Create the main window
root = tk.Tk()
root.title("Internet Speed Test By Ahsan")
root.geometry("500x500")
root.config(bg="#CCEDFF")

# Create a button to trigger the speed test
button = tk.Button(root, text="Check Speed", background="#25265E", font=("Arial", 15, "bold"), command=update_speed)
button.pack(pady=20)  # Add some padding around the button

# Create labels to display the results
download_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
download_label.pack()

upload_label = tk.Label(root, text="")
upload_label.pack()

# Start the main event loop
root.mainloop()
