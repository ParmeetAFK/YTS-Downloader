import re

a_link = '<a class="text--bold palewhite title" href="/movie/fighting">Fighting</a>'



m = re.search('href=(".+?")',a_link)

z = re.search('>(.+?)<',a_link)


for i in (z):
	print(z.group(i))
