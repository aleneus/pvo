class BuildingHtmlView:
    def numbers(self, ns, purpose):
        f = open('numbers.html', 'w')
        f.write("""
        <html>
        <head> <title> </title> </head>
        <body>
        <h1> Rooms for {0} </h1>
        <table border=3>""".format(purpose))
        for n in ns:
            f.write('<tr><td>{0}</td></tr>\n'.format(n))
        f.write("""
        </table>
        </body>
        </html>""")
        f.close()
