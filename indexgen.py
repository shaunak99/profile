import json
import pdfkit

jsonfile = open('resume.json')
resume = json.load(jsonfile)


def header(destfile):
    outfile.write('<div>')
    outfile.write('<div style="float:left;">')
    outfile.write('<p><span class="logospan"><img alt="" src="images/image2.jpg" class="logoimage" title=""></span></p>')
    outfile.write('</div>')
    outfile.write('<div class="basics">')
    outfile.write('<p class="c28"><span class="c24">' + resume["basics"]["name"].upper() + '</span></p>')
    outfile.write('<p class="c62"><span class="c1">Course : '  + resume["basics"]["course"] + '</span></p>')
    outfile.write('<p class="c62"><span class="c1">Institute : '  + resume["basics"]["institute"] + '</span></p>')
    outfile.write('<p class="c13"><span class="c1">Email : ' + resume["basics"]["email"] + '</span></p>')
    outfile.write('<p class="c13"><span class="c1">Mobile : ' + resume["basics"]["mobile"] + '</span></p>')
    if destfile == "pdf":
        outfile.write('<p class="c13"><span class="c1">Webpage : </span><a href="https://' + resume["basics"]["webpage"] + '">https://' + resume["basics"]["webpage"] + '</a></p>')
        outfile.write('<p class="c49"><span class="c1">CGPA : ' + resume["basics"]["cgpa"] + '</span></p>')
    outfile.write('</div>')
    outfile.write('<div style="float:right;">')
    outfile.write('<p><span class="dpspan"><img alt="" src="images/image1.png" class="dpimage" title=""></span></p>')
    outfile.write('</div>')
    outfile.write('</div>')
    outfile.write('<div style="clear:both"></div>')


def menubar():
    outfile.write('<ul class="horizontal"><li class="active">Home</li><li><a href="projects.html">Projects</a></li><li><a href="shaunak.pdf">CV</a></li></ul>')


def education():
    outfile.write('<table class="c2">')
    outfile.write('<tbody>')
    outfile.write('<tr><td class="c22" colspan="5" rowspan="1"><p class="c21"><span class="c5">ACADEMIC DETAILS</span></p></td></tr>')
    outfile.write('<tr class="c0">')
    outfile.write('<td class="c23" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>COURSE </b></span></p></td>')
    outfile.write('<td class="c16" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>INSTITUTE/COLLEGE </b></span></p></td>')
    outfile.write('<td class="c20" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>BOARD/UNIVERSITY </b></span></p></td>')
    outfile.write('<td class="c15" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>SCORE </b></span></p></td>')
    outfile.write('<td class="c55" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>YEAR </b></span></p></td>')
    outfile.write('</tr>')
    for rec in resume["education"]:
        outfile.write('<tr class="c0">')
        outfile.write('<td class="c23" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + rec["course"] + '</span></p></td>')
        outfile.write('<td class="c16" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + rec["institute"] + '</span></p></td>')
        outfile.write('<td class="c20" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + rec["board"] + '</span></p></td>')
        outfile.write('<td class="c15" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + rec["score"] + '</span></p></td>')
        outfile.write('<td class="c55" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + rec["year"] + '</span></p></td>')
        outfile.write('</tr>')
    outfile.write('</tr>')
    outfile.write('<tbody>')
    outfile.write('</table>')


def skills():
    outfile.write('<table class="c2">')
    outfile.write('<tbody>')
    for skill in resume["skills"]:
        outfile.write('<tr><td class="c53" colspan="1" rowspan="1">')
        outfile.write('<p class="c79"><span class="c1"><b>' + skill["category"] + '</b></span></p>')
        outfile.write('</td>')
        outfile.write('<td class="c30" colspan="1" rowspan="1">')
        outfile.write('<p class="c43"><span class="c1">' + skill["details"] + '</span></p>')
        outfile.write('</td></tr>')
    outfile.write('<tbody>')
    outfile.write('</table>')


def table_start(caption):
    outfile.write('<table class="c2">')
    outfile.write('<tbody>')
    if len(caption) > 0:
        outfile.write('<tr><td class="c22" colspan="1" rowspan="1"><p class="c21"><span class="c5">' + caption.upper() + '</span></p></td></tr>')
    outfile.write('<tr>')
    outfile.write('<td class="c22" colspan="1" rowspan="1">')


def table_end():
    outfile.write('</td>')
    outfile.write('</tr>')
    outfile.write('<tbody>')
    outfile.write('</table>')


def internship():
    table_start("summer internship / work experience")
    for internship in resume["internships"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + internship["role"] + ', ' + internship["company"] + '</b></span>')
        outfile.write('<span class="c1" style="float:right;"><b>' + internship["startDate"] + ' - ' + internship["endDate"] + '</b></span><br />')
        outfile.write('<span class="c1">' + internship["summary"] + '</span></p>')
    table_end()

def projects():
    table_start("projects")
    for project in resume["projects"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + project["title"] + ' - ' + project["domain"] + '</b></span>')
        outfile.write('<span class="c1" style="float:right;"><b>' + project["startDate"] + ' - ' + project["endDate"] + '</b></span><br />')
        outfile.write('<span class="c1">' + project["summary"] + '</span></p>')
    table_end()


def responsibilities():
    table_start("position of responsibilities")
    for resp in resume["responsibilities"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + resp["role"] + '</b></span>')
        outfile.write('<span class="c1" style="float:right;"><b>' + resp["startDate"] + ' - ' + resp["endDate"] + '</b></span><br />')
        outfile.write('<span class="c1">' + resp["summary"] + '</span></p>')
    table_end()


def extracurricular():
    table_start("extra curricular activities")
    for activity in resume["extracurricular"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + activity["activity"] + '</b></span>')
        outfile.write('<span class="c1">' + activity["summary"] + '</span></p>')
    table_end()


def awards():
    table_start("awards and recognitions")
    for award in resume["awards"]:
        outfile.write('<p class="c66"><span class="c1">' + award["summary"] + '</span></p>')
    table_end()


def certifications():
    outfile.write('<table class="c2">')
    outfile.write('<tbody>')
    outfile.write('<tr><td class="c22" colspan="3" rowspan="1"><p class="c21"><span class="c5">  CERTIFICATIONS </span></p></td></tr>')

    outfile.write('<tr class="c0"><td class="c37" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>CERTIFICATION </b></span></p></td>')
    outfile.write('<td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>CERTIFYING AUTHORITY </b></span></p></td>')
    outfile.write('<td class="c27" colspan="1" rowspan="1"><p class="c25"><span class="c1"><b>DESCRIPTION </b></span></p></td></tr>')
    for cert in resume["certifications"]:
        outfile.write('<tr class="c0"><td class="c37" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + cert["certificate"] + '</span></p></td>')
        outfile.write('<td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + cert["certifier"] + '</span></p></td>')
        outfile.write('<td class="c27" colspan="1" rowspan="1"><p class="c25"><span class="c1">' + cert["summary"] + '</span></p></td></tr>')
    outfile.write('<tbody>')
    outfile.write('</table>')


def competitions():
    table_start("competitions")
    for comp in resume["competitions"]:
        outfile.write('<p class="c66"><span class="c1">' + comp["summary"] + '</span></p>')
    table_end()


def scholarships():
    table_start("scholoarships")
    for sch in resume["scholarships"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + sch["name"] + '</b></span>')
        outfile.write('<span class="c1" style="float:right;"><b>' + sch["date"] + '</b></span><br />')
        outfile.write('<span class="c1">' + sch["summary"] + '</span></p>')
    table_end()


def languages():
    table_start("languages known")
    for lang in resume["languages"]:
        outfile.write('<p class="c66"><span class="c1"><b>' + lang["language"] + '</b>: ' + lang['fluency'] + '</span></p>')
    table_end()

def gen(destfile):
    global outfile

    outfile = open('index.html','w')
    outfile.write("<!DOCTYPE html>")
    outfile.write("<html>")

    outfile.write("<head>")
    outfile.write('<meta content="text/html; charset=UTF-8" http-equiv="content-type">')
    outfile.write('<link rel="stylesheet" href="resume.css">')
    outfile.write("</head>")

    outfile.write("<body>")
    outfile.write('<div style="width:100%;">')

    if destfile == "html":
        menubar()
    header(destfile)
    if destfile == "pdf":
        education()
    skills()
    internship()
    projects()
    responsibilities()
    extracurricular()
    awards()
    certifications()
    competitions()
    scholarships()
    languages()

    outfile.write('</div>')
    outfile.write("</body>")
    outfile.write("</html>")
    outfile.close()

    if destfile == "pdf":
        options = {
            "margin-left": "0.5in",
            "margin-right": "0.5in",
            "margin-top": "0.5in",
            "margin-bottom": "0.5in"
        }
        pdfkit.from_file('index.html', 'shaunak.pdf', options=options)


def main():
    gen("pdf") #call this before html generation to keep the menubar in html
    gen("html")


main()
