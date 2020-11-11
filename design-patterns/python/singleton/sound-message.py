class Speaker:
    class __Speaker:
        def say_text(self, text):
            print("Sound: ", text)
            
    instance = None

    def __init__(self):
        if not Speaker.instance:
            Speaker.instance = Speaker.__Speaker()

    def say_text(self, text):
        self.instance.say_text(text)

def main():
    s = Speaker()
    s.say_text("Hello")

main()
