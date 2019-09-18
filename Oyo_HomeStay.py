import requests
import bs4
import csv
url="https://www.oyorooms.com/oyo-homes-in-bangalore/"
for i in range(1,4):
	new_url=url+"?page="+str(i)
	data=requests.get(new_url)
	soup=bs4.BeautifulSoup(data.text,"html.parser")
	for div in soup.find_all('div',class_='hotelCardListing__descriptionWrapper'):
		try:
			Rating=div.find('span',class_="is-fontBold hotelRating__rating hotelRating__rating--verygood hotelRating__rating--clickable").text
		except Exception: 
			Rating="No Rating"
		try:
			Amenities=div.find('div',class_="amenityWrapper").text
		except Exception:
			Amenities="No Amenities"
		try:
		    Price=div.find('span',class_="listingPrice__finalPrice").text.encode("ascii","ignore").decode("utf-8")
		except Exception: 
		   	Price="Sold"
		venue={
		"Venue_Name":div.find('h3',class_="listingHotelDescription__hotelName d-textEllipsis").text,
		"venue_address":div.find('div',class_="d-body-lg d-textEllipsis listingHotelDescription__hotelAddress").text,
		"Rating":Rating,
		"Amenities":Amenities,
		"Price":Price
		}
		print(venue)