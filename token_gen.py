import socketserver
from time import sleep

from dvsc.config import TOKEN, TOKEN_PASSWORD

ABOUT = """
  dP            dP                                                             
  88            88                                                             
d8888P .d8888b. 88  .dP  .d8888b. 88d888b.          .d8888b. .d8888b. 88d888b. 
  88   88'  `88 88888"   88ooood8 88'  `88 88888888 88'  `88 88ooood8 88'  `88 
  88   88.  .88 88  `8b. 88.  ... 88    88          88.  .88 88.  ... 88    88 
  dP   `88888P' dP   `YP `88888P' dP    dP          `8888P88 `88888P' dP    dP 
ooooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~.88~oooooooooooooooooo v1.5.2 (2023)
                                                     d8888P

Cutting-edge software designed to enhance your security by generating robust tokens from passwords.
Our advanced algorithms ensure a seamless and secure transformation of your passwords into unique tokens,
adding an extra layer of protection to your sensitive data.

Stay ahead of the curve with Token-Gen, your trusted companion for generating secure tokens from passwords.
"""
# Cache flush were added to fix weird socket timeouts, black magic - it just works
CACHE_FLUSH_INTERVAL = 0.1
answer = ''


class CommandHandler:
    def handle_command(self, command):
        global answer
        command_segments = command.split(' ')

        if command_segments[0] == "about":
            answer = ABOUT
            sleep(CACHE_FLUSH_INTERVAL)
        elif command_segments[0] == "pass":
            if len(command_segments) != 2:
                answer = "Enter password!"
            else:
                answer = True
                if command_segments[1] == TOKEN_PASSWORD:
                    answer = "goodboy"
                else:
                    answer = "badboy"
                
                sleep(CACHE_FLUSH_INTERVAL)
                if answer == "goodboy":
                    answer = TOKEN
                else:
                    answer = "Wrong password!"
        elif command_segments[0] == "help":
            if len(command_segments) != 2:
                answer = """help <command> - Get help on command
pass <password> - Get token by verifying password
source <eula> - Show server handler source-code, should agree to EULA = true
status - Service status
about - About screen
"""
            else:
                answer = command_segments[1]
                sleep(CACHE_FLUSH_INTERVAL)
                sleep(CACHE_FLUSH_INTERVAL)
                if answer == "pass":
                    answer = "Get token by verifying password"
        elif command_segments[0] == "status":
            sleep(CACHE_FLUSH_INTERVAL)
            answer = "ALIVE"
            sleep(CACHE_FLUSH_INTERVAL)
        elif command_segments[0] == "source":
            if len(command_segments) != 2:
                answer = "EULA was not agreed!"
            else:
                with open(__file__, 'rt') as f:
                    answer = f.read()
        else:
            answer = "Unknown command"
        return answer

class SimpleTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        command_handler = CommandHandler()
        self.wfile.write(ABOUT.encode("utf-8") + b"\nEnter help to get started.\n")

        while True:
            self.wfile.write(b"> ")
            data = self.rfile.readline().decode("utf-8").strip()
            if not data:
                break

            response = command_handler.handle_command(data)
            self.wfile.write(response.encode("utf-8") + b"\n")

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 7438

    server = socketserver.ThreadingTCPServer((HOST, PORT), SimpleTCPHandler)

    try:
        print(f"Server listening on {HOST}:{PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer terminated")
        server.shutdown()
        server.server_close()
