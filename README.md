# Internet-speed-Tester

**Description:**

This Python program creates a simple graphical interface to measure your internet download and upload speeds using the Speedtest library. It is built with Tkinter, a standard Python library for creating GUI applications.

**Installation:**

1. **Install required libraries:**
   ```bash
   pip install tk speedtest-cli
   ```
2. **Click the "Check Speed" button:** This will initiate the speed test.
3. **View results:** The download and upload speeds will be displayed in Mbps below the button.

**Code Structure:**

- **Imports:**
   - `tkinter` for creating the GUI elements.
   - `speedtest` for performing the speed test.
- **`update_speed` function:**
   - Conducts the speed test using Speedtest.
   - Calculates and formats the download and upload speeds.
   - Updates the labels with the results.
- **Main window setup:**
   - Creates the main window with the title "Internet Speed Test".
- **Button creation:**
   - Creates a "Check Speed" button that calls the `update_speed` function when clicked.
- **Label creation:**
   - Creates labels to display the download and upload speeds.
- **Event loop:**
   - Starts the Tkinter event loop to keep the window open and responsive.

**Troubleshooting:**

- **ModuleNotFoundError:** Ensure the `speedtest-cli` module is installed using `pip install speedtest-cli`.
- **Typos:** Check for any typos in the code, especially in module names or function calls.

**Additional Notes:**

- The speed test results may vary depending on your internet connection, server selection, and other factors.
- Consider adding features like:
   - Progress bars during the test.
   - History of previous results.
   - Option to select a specific test server.
