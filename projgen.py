import json

outfile = open('projects.html','w')
jsonfile = open('resume.json')
resume = json.load(jsonfile)


def menubar():
    outfile.write('<ul class="horizontal"><li><a href="index.html">Home</a></li><li class="active">Projects</li><li><a href="shaunak.pdf">CV</a></li></ul>')


def show_cards():
    outfile.write('<div class="main"><h1>Projects and Algorithms</h1><ul class="cards">')
    for proj in resume["projcards"]:
        if proj['display'] == 1:
            outfile.write('<li class="cards_item"><div class="card">')
            outfile.write('<div class="card_image"><img src="' + proj["image"] + '"></div>')
            outfile.write('<div class="card_content"><h2 class="card_title">' + proj["title"] + '</h2>')
            outfile.write('<button onclick="location.href=' + "'" + proj["link"] + "'" + '" class="btn card_btn">Read More</button>')
            outfile.write('</div></div></li>')
    outfile.write('</ul></div>')


def main():
    outfile.write("<!DOCTYPE html>")
    outfile.write("<html>")

    outfile.write("<head>")
    outfile.write('<meta content="text/html; charset=UTF-8" http-equiv="content-type">')
    outfile.write('<link rel="stylesheet" href="resume.css">')
    outfile.write('<link rel="stylesheet" href="projects.css">')
    outfile.write("</head>")

    outfile.write("<body>")
    outfile.write('<div style="width:100%;">')

    menubar()
    show_cards()

    outfile.write('</div>')
    outfile.write("</body>")
    outfile.write("</html>")


main()