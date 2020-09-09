import urllib.request as Ureq
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import os
url_search="test_url.html"
# import tqdm
from tqdm.auto import tqdm
class TqdmUp(tqdm):
	def update_to(self,b=1,bsize=1,tsize=None):
		if tsize is not None:
			self.total=tsize
		self.update(b*bsize-self.n)



def one_downloadable_item(single_path):
	print(single_path)
	print("Excutinh")
	item_name=single_path.split("/")[-1]
	with TqdmUp(unit="B",unit_scale=True,unit_divisor=1024,miniters=1,desc=item_name) as t:
		# print("hello")
		path_to_join="D:/movies"
		full_file_name=os.path.join(path_to_join,item_name)
		Ureq.urlretrieve(single_path,filename=full_file_name,reporthook=t.update_to,data=None)
		t.total=t.n

def download_many_items(url_path):
	for item in url_path:
		try:
			one_dowloadable_item(item)
		except Exception as err:
			return (str(err))

	return "successfully completed"

# custom code
def  web_scraping_dowload(page_source):
	

	
	try:
		

		myUrl=page_source
		uClient=urlopen(myUrl)
	# uClient=uReq(myUrl)
		page=uClient.read()
		uClient.close()
		page_soup=soup(page,"html.parser")
		# get body
		body_content=page_soup.body
		links=body_content.findAll("a")
		# get valis href

		for index,link in enumerate(links):
			# print(link["href"])
			format_type=link["href"].split(".")[-1]
			if format_type=="mkv":
				if index>=4:
					
					print("hello-1")
					link_address=link["href"]
					full_address=f"http://dl2.mojdl.com/upload/Tv-Series/Better%20Call%20Saul/S04/720p/{link_address}"
					one_downloadable_item(full_address)


			







		
	except Exception as e:
		return f"an error occurred {str(e)}"

	# get a links

	


web_scraping_dowload("http://dl2.mojdl.com/upload/Tv-Series/Better%20Call%20Saul/S04/720p/")




