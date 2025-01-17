from urllib.request import urlretrieve

# read the relative path to CVPR2019OAR
file = open('cvpr2020oar.html', 'r')
html = file.read()

html = html[html.find('G-TAD: Sub-Graph Localization for Temporal Action Detection')+1:]

# go through the html file until it
# no longer contains the string '.pdf'
while html.find('.pdf') != -1:
	# find the first .pdf file
	paper = html[:html.find('.pdf')+4]
	paper = paper[paper.rfind('"')+1:]
	print(paper)

	# download the pdf into the content folder
	urlretrieve(paper, 'content/' + paper[paper.rfind('/')+1:])

	# update the html so it no longer contains that pdf
	html = html[html.find('.pdf')+1:]
