import glob

link_files = glob.glob('output/02-*.txt')
print('Files Found: {}'.format(link_files))

f = open('output/all_article_links.txt', 'w')
for lf in link_files:
    links = open(lf, 'r')
    f.write(links.read())
    links.close()
f.close()
