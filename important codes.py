'''
import pdfkit
string="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>yash</title>
</head>
<body>
<h1>Hi HOW ARE YOU ALL</h1>
<h2>I am yash what is your name</h2>
</body>
</html>
"""
pdfkit.from_string(string, 'out.pdf')


'''
""" --hidden-import "babel.numbers" """