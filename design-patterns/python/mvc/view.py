from subprocess import call

class BuildingView:
    def table(self, data):
        pass

class BuildingTextView(BuildingView):
    def table(self, data):
        print()
        for row in data:
            for record in row:
                print('{} '.format(record), end='')
            print()
        print()

class BuildingHtmlView(BuildingView):
    def __init__(self, file_name):
        self.ofile = file_name

    def set_output_file(self, file_name):
        self.ofile = file_name
    
    def table(self, data):
        with open(self.ofile, 'w') as f:
            f.write("""
            <html>
            <head>
            <title>
            </title>
            </head>
            <body>
            <table border=3>""")
            for row in data:
                f.write('<tr>')
                for record in row:
                    f.write('<td>{}</td>\n'.format(record))
                f.write('</tr>')
            f.write("""
            </table>
            </body>
            </html>
            """)
        call(["w3m", self.ofile])
