class Logger:
    def __init__(self, path):
        # This opens (or creates) a file in "append" mode
        self.file = open(path, "a")
    
    def log(self, message, level="info"):
        self.file.write(f"[{level.upper()}] {message}\n")
        # Optional: Print to console too so you can see it immediately
        print(f"Logged to file: [{level.upper()}] {message}")

    def __del__(self):
        self.file.close()

# --- CODE TO GENERATE OUTPUT ---

# 1. Initialize the logger with a filename
my_logger = Logger("my_logs.txt")

# 2. Log some messages
my_logger.log("System started")
my_logger.log("Low disk space", level="warning")
my_logger.log("Failed to connect", level="error")

# 3. Check your folder! 
# A file named 'my_logs.txt' will appear with your text inside.