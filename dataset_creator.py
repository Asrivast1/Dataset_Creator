# Downloading images from google search for datasets using python script - Web Scraping Hack
from google_images_download import google_images_download #The package we are going to use to download the pictures from Google
def dataset(keys, count):
	response = google_images_download.googleimagesdownload() #Using the function from within the package to download the images
	arguments = {"keywords":keys, "limit":count,'print_urls':True}  # Specifying the parameters, keywords means the thing whose pics we intend to download and count refers to the number
	paths = response.download(arguments)
	print(paths)
keys = input("Enter the name of the image that you want to create dataset of:")
count = int(input("Enter the number of images you require (whole number only)"))
dataset(keys, count)

