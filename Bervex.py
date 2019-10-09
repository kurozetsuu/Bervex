from tkinter import * 
from PIL import Image,ImageTk
import requests 
from tkinter import ttk 
from tkinter import filedialog
from tkinter import messagebox 
from threading import Thread


window = Tk()
window.title('Bervex')
window.iconbitmap(r'Extensions/icon.ico')
window.geometry('400x380')
window.configure(background="black")
photo = Image.open("Extensions/image.png").resize((175,175),Image.ANTIALIAS)
image = ImageTk.PhotoImage(photo)
picture = Label(image=image, bg="black")
picture.pack()
window.resizable=(False, False)


image1 = Image.open("Extensions/facebook.png")
image1 = image1.resize((22,22),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image1)
picture2 = Label(image=photo2, bg="#555e6f")

text = Label(window, text='Bervex', bg='black', fg='#f6fef9', font=('Papyrus',25,))
text.pack()

text1 = Label(window, text='Username :  ', bg='black', fg='white', font=('Courier',14,'bold'))
text1.place(x=30,y=250)

entry = Entry(window, width=20, bg='white', state='normal', font=('Courier',12))
entry.place(x=155,y=254)

def grab():
	window.config(cursor="wait")

	acc = entry.get()

	rfacebook = requests.get("https://www.facebook.com/"+acc)
	rinstagram = requests.get("https://www.instagram.com/"+acc)
	rtwitter = requests.get("https://www.twitter.com/"+acc)
	ryoutube = requests.get("https://www.youtube.com/"+acc)
	rvk = requests.get("https://vk.com/"+acc)
	rlinkedin = requests.get("https://www.linkedin.com/"+acc)
	rblogger = requests.get("https://"+acc+".blogspot.com")
	rwordpress = requests.get("https://"+acc+".wordpress.com")
	rgithub = requests.get("https://www.github.com/"+accfrom tkinter import * 
from PIL import Image,ImageTk
import requests 
from tkinter import ttk 
from tkinter import filedialog
from tkinter import messagebox 
from threading import Thread


window = Tk()
window.title('Bervex')
window.iconbitmap(r'Extensions/icon.ico')
window.geometry('400x380')
window.configure(background="black")
photo = Image.open("Extensions/image.png").resize((175,175),Image.ANTIALIAS)
image = ImageTk.PhotoImage(photo)
picture = Label(image=image, bg="black")
picture.pack()
window.resizable=(False, False)


image1 = Image.open("Extensions/facebook.png")
image1 = image1.resize((22,22),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image1)
picture2 = Label(image=photo2, bg="#555e6f")

text = Label(window, text='Bervex', bg='black', fg='#f6fef9', font=('Papyrus',25,))
text.pack()

text1 = Label(window, text='Username :  ', bg='black', fg='white', font=('Courier',14,'bold'))
text1.place(x=30,y=250)

entry = Entry(window, width=20, bg='white', state='normal', font=('Courier',12))
entry.place(x=155,y=254)

def grab():
	window.config(cursor="wait")

	acc = entry.get()

	rfacebook = requests.get("https://www.facebook.com/"+acc)
	rinstagram = requests.get("https://www.instagram.com/"+acc)
	rtwitter = requests.get("https://www.twitter.com/"+acc)
	ryoutube = requests.get("https://www.youtube.com/"+acc)
	rvk = requests.get("https://vk.com/"+acc)
	rlinkedin = requests.get("https://www.linkedin.com/"+acc)
	rblogger = requests.get("https://"+acc+".blogspot.com")
	rwordpress = requests.get("https://"+acc+".wordpress.com")
	rgithub = requests.get("https://www.github.com/"+acc)
	rpinterest = requests.get("https://www.pinterest.com/"+acc)
	rreddit = requests.get("https://www.reddit.com/user/"+acc)
	rtumblr = requests.get("https://"+acc+".tumblr.com")
	rflickr  = requests.get("https://www.flickr.com/photos/"+acc)
	rsteam   = requests.get("https://steamcommunity.com/id/"+acc)
	rvimeo   = requests.get("https://www.vimeo.com/"+acc)
	rsoundcloud = requests.get("https://www.soundcloud.com/"+acc)
	rdisqus     = requests.get("https://www.disqus.com/"+acc)
	rmedium = requests.get("https://medium.com/@"+acc)
	rdevianart = requests.get("https://"+acc+".deviantart.com")
	raboutme = requests.get("https://about.me/"+acc)
	rimgur = requests.get("https://imgur.com/user/"+acc)
	rflipboard = requests.get("https://www.flipboard.com/@"+acc)
	rslideshare = requests.get("https://www.slideshare.net/"+acc)
	rspotify = requests.get("https://open.spotify.com/user/"+acc)
	rscribd = requests.get("https://www.scribd.com/"+acc)
	rbadoo = requests.get("https://www.badoo.com/en/"+acc)
	rpatreon = requests.get("https://www.patreon.com/"+acc)
	rdailymotion = requests.get("https://www.dailymotion.com/"+acc)
	rcashme = requests.get("https://cash.me/"+acc)
	rbehance = requests.get("https://www.behance.net/"+acc)
	rgoodreads = requests.get("https://www.goodreads.com/"+acc)
	rkeybase = requests.get("https://www.keybase.io/"+acc)
	rkongregate = requests.get("https://kongregate.com/accounts/"+acc)
	rlivejournal = requests.get("https://"+acc+".livejournal.com")
	rangellist = requests.get("https://angel.co/"+acc)
	rlastfm = requests.get("https://last.fm/user/"+acc)
	rdribbble = requests.get("https://dribbble.com/"+acc)
	rcodecademy = requests.get("https://www.codecademy.com/"+acc)
	rgravatar = requests.get("https://en.gravatar.com/"+acc)
	rpastebin = requests.get("https://foursquare.com/"+acc)
	rfoursquare = requests.get("https://foursquare.com/"+acc)
	rroblox = requests.get("https://foursquare.com/"+acc)
	rgumroad = requests.get("https://www.gumroad.com/"+acc)
	rnewgrounds = requests.get("https://"+acc+".newgrounds.com")
	rwattpad = requests.get("https://www.wattpad.com/user/"+acc)
	rcanva = requests.get("https://www.canva.com/"+acc)
	rcreativemarker = requests.get("https://creativemarket.com/"+acc)
	rtrakt = requests.get("https://www.trakt.tv/users/"+acc)
	r500px = requests.get("https://500px.com/"+acc)
	rbuzzfeed = requests.get("https://buzzfeed.com/"+acc)
	rtripadvisor = requests.get("https://tripadvisor.com/members/"+acc)
	rhubpages = requests.get("https://"+acc+".hubpages.com/")
	rhouzz = requests.get("https://houzz.com/user/"+acc)
	rblipfm = requests.get("https://blip.fm/"+acc)
	rhackernews = requests.get("https://news.ycombinator.com/user?id="+acc)
	rcodementor = requests.get("https://www.codementor.io/"+acc)
	rreverbnation = requests.get("https://www.reverbnation.com/"+acc)
	rifttt = requests.get("https://www.ifttt.com/p/"+acc)
	rebay = requests.get("https://www.ebay.com/usr/"+acc)
	rslack = requests.get("https://"+acc+".slack.com")
	rtrip = requests.get("https://www.trip.skyscanner.com/user/"+acc)
	rello = requests.get("https://ello.co/"+acc)
	rtripit = requests.get("https://www.tripit.com/people/"+acc+"#/profile/basic-info")
	retsy = requests.get("https://www.etsy.com/shop/"+acc)
	rbasecamp = requests.get("https://"+acc+".basecamphq.com/login")
	rtracky = requests.get("https://tracky.com/user/"+acc)
	rokcupid = requests.get("https://www.okcupid.com/profile/"+acc)
	rbandcamp = requests.get("https://www.bandcamp.com/"+acc)
	rwikipedia = requests.get("https://www.wikipedia.org/wiki/User:"+acc)
	rcontently = requests.get("https://"+acc+".contently.com")
	rbitbucket = requests.get("https://bitbucket.org/"+acc)
	rfotolog = requests.get("https://fotolog.com/"+acc)
	rdesignspiration = requests.get("https://www.designspiration.net/"+acc)


	file = open(acc+".txt","w")
	file.write(acc+" results !\n")
	file.write("\n")


	if (rfacebook.ok) == True:

		file.write("[+] Facebook        :     "+"https://www.facebook.com/"+acc+"\n")


	if (rinstagram.ok) == True:

		file.write("[+] instagram       :     "+"https://www.instagram.com/"+acc+"\n")


	if (rtwitter.ok) == True:

		file.write("[+] Twitter         :     "+"https://www.twitter.com/"+acc+"\n")


	if (ryoutube.ok) == True:

		file.write("[+] Youtube         :     "+"https://www.youtube.com/"+acc+"\n")


	if (rvk.ok) == True:

		file.write("[+] Vk              :     "+"https://www.vk.com/"+acc+"\n")

	if (rlinkedin.ok) == True:

		file.write("[+] Linkedin        :     "+"https://www.linkedin.com/"+acc+"\n")

	if (rblogger.ok) == True:

		file.write("[+] Blogger         :     "+"https://"+acc+".blogspot.com"+"\n")


	if (rwordpress.ok) == True : 

		file.write("[+] Wordpress       :     "+"https://"+acc+".wordpress.com"+"\n")

	if (rgithub.ok) == True:
 
		file.write("[+] Github          :     "+"https://www.github.com/"+acc+"\n")

	
	if (rpinterest.ok) == True:

		file.write("[+] Pinterest       :     "+"https://www.pinterest.com/"+acc+"\n")


	if (rreddit.ok) == True:

		file.write("[+] Reddit          :     "+"https://www.reddit.com/user/"+acc+"\n")


	if (rtumblr.ok) == True:

		file.write("[+] Tumblr          :     "+"https://"+acc+".tumblr.com"+"\n")

	

	if (rflickr.ok) == True:

		file.write("[+] Flickr          :     "+"https://www.flickr.com/photos/"+acc+"\n")

	

	if (rflickr.ok) == True:

		file.write("[+] Steam           :     "+"https://www.steamcommunity.co/id/"+acc+"\n")


	if (rvimeo.ok) == True:

		file.write("[+] Vimeo           :     "+"https://www.vimeo.com/"+acc+"\n")

	
	if (rsoundcloud.ok) == True:

		file.write("[+] Soundcloud      :     "+"https://www.soundcloud.com/"+acc+"\n")


	if (rdisqus.ok) == True:

		file.write("[+] Disqus          :     "+"https://www.disqus.com/"+acc+"\n")

	if (rmedium.ok) == True:

		file.write("[+] Medium          :     "+"https://www.medium.com/@"+acc+"\n")

	if (rdevianart.ok) == True:

		file.write("[+] DevianART       :     "+"https://"+acc+".devianart.com/"+"\n")

	
	if (raboutme.ok) == True:

		file.write("[+] About.me        :     "+"https://about.me/"+acc+"\n")


	if (rimgur.ok) == True:

		file.write("[+] Imgur           :     "+"https://www.imgur.me/user/"+acc+"\n")


	if (rflipboard.ok) == True:

		file.write("[+] Flipboard       :     "+"https://www.flipboard.com/@"+acc+"\n")

	

	if (rslideshare.ok) == True:

		file.write("[+] Slideshare      :     "+"https://www.slideshare.net/"+acc+"\n")



	if (rspotify.ok) == True:

		file.write("[+] Spotify         :     "+"https://open.spotify.com/user/"+acc+"\n")

	

	if (rscribd.ok) == True:

		file.write("[+] Scribd          :     "+"https://www.scribd.com/"+acc+"\n")

	
	if (rbadoo.ok) == True:

		file.write("[+] Badoo           :     "+"https://www.badoo.com/en/"+acc+"\n")

	

	if (rpatreon.ok) == True:

		file.write("[+] Patreon         :     "+"https://www.patreon.com/"+acc+"\n")

	

	if (rdailymotion.ok) == True:

		file.write("[+] Dailymotion     :     "+"https://www.dailymotion.com/"+acc+"\n")

	

	if (rcashme.ok) == True:

		file.write("[+] CashMe          :     "+"https://www.cash.me/"+acc+"\n")


	if (rbehance.ok) == True:

		file.write("[+] Behance         :     "+"https://www.behance.com/"+acc+"\n")


	if (rgoodreads.ok) == True:

		file.write("[+] GoodReads       :     "+"https://www.goodreads.com/"+acc+"\n")

	
	if (rkeybase.ok) == True:

		file.write("[+] Keybase         :     "+"https://www.keybase.io/"+acc+"\n")


	if (rkongregate.ok) == True:

		file.write("[+] Kongregate      :     "+"https://kongregate.com/accounts/"+acc+"\n")

	

	if (rlivejournal.ok) == True:

		file.write("[+] LiveJournal     :     "+"https://"+acc+".livejournal.com"+"\n")



	if (rangellist.ok) == True:

		file.write("[+] AngelList       :     "+"https://angel.co/"+acc+"\n")



	if (rlastfm.ok) == True:

		file.write("[+] Last.fm         :     "+"https://last.fm/user/"+acc+"\n")

	

	if (rdribbble.ok) == True:

		file.write("[+] Dribble         :     "+"https://dribbble.com/"+acc+"\n")

	
	if (rcodecademy.ok) == True:

		file.write("[+] Codecademy      :     "+"https://www.codecademy.com/"+acc+"\n")

	

	if (rgravatar.ok) == True:

		file.write("[+] Gravatar        :     "+"https://en.gravatar.com/"+acc+"\n")

	

	if (rpastebin.ok) == True:

		file.write("[+] Pastebin        :     "+"https://pastebin.com/u/"+acc+"\n")
 
	
	if (rfoursquare.ok) == True:

		file.write("[+] Foursquare      :     "+"https://foursquare.com/"+acc+"\n")

	

	if (rroblox.ok) == True:

		file.write("[+] Roblox          :     "+"https://foursquare.com/"+acc+"\n")



	if (rgumroad.ok) == True:

		file.write("[+] Gumroad         :     "+"https://www.gumroad.com/"+acc+"\n")

	

	if (rnewgrounds.ok) == True:

		file.write("[+] Newgrounds      :     "+"https://"+acc+".newgrounds.com"+"\n")

	
	if (rwattpad.ok) == True:

		file.write("[+] Wattpad         :     "+"https://www.wattpad.com/user/"+acc+"\n")

	
	if (rcanva.ok) == True:

		file.write("[+] Canva           :     "+"https://www.canva.com/"+acc+"\n")



	if (rcreativemarker.ok) == True:

		file.write("[+] CreativeMarket  :     "+"https://creativemarket.com/"+acc+"\n")

	

	if (rtrakt.ok) == True:

		file.write("[+] Trakt           :     "+"https://www.trakt.tv/users/"+acc+"\n")

	
	if (r500px.ok) == True:

		file.write("[+] 500px           :     "+"https://500px.com/"+acc+"\n")

	
	if (rbuzzfeed.ok) == True:

		file.write("[+] Buzzfeed        :     "+"https://buzzfeed.com/"+acc+"\n")

	
	if (rtripadvisor.ok) == True:

		file.write("[+] TripAdvisor     :     "+"https://tripadvisor.com/members/"+acc+"\n")


	if (rhubpages.ok) == True:

		file.write("[+] HubPages        :     "+"https://"+acc+".hubpages.com/"+"\n")

	

	if (rhouzz.ok) == True:

		file.write("[+] Houzz           :     "+"https://houzz.com/user/"+acc+"\n")

	
	if (rblipfm.ok) == True:

		file.write("[+] Blip.fm         :     "+"https://blip.fm/"+acc+"\n")

	

	if (rhackernews.ok) == True:

		file.write("[+] HackerNews      :     "+"https://news.ycombinator.com/user?id="+acc+"\n")

	
	if (rcodementor.ok) == True:

		file.write("[+] Codementor      :     "+"https://www.codementor.io/"+acc+"\n")


	if (rreverbnation.ok) == True:

		file.write("[+] ReverbNation    :     "+"https://www.reverbnation.com/"+acc+"\n")

	

	if (rifttt.ok) == True:

		file.write("[+] IFTTTT          :     "+"https://www.ifttt.com/p/"+acc+"\n")


	if (rebay.ok) == True:

		file.write("[+] Ebay            :     "+"https://www.ebay.com/usr/"+acc+"\n")

	
	if (rslack.ok) == True:

		file.write("[+] Slack           :     "+"https://"+acc+".slack.com"+"\n")

	

	if (rtrip.ok) == True:

		file.write("[+] Trip            :     "+"https://www.trip.skyscanner.com/user/"+acc+"\n")

	

	if (rello.ok) == True:

		file.write("[+] Ello            :     "+"https://ello.co/"+acc+"\n")

	

	if (rtripit.ok) == True:

		file.write("[+] Tripit          :     "+"https://www.tripit.com/people/"+acc+"#/profile/basic-info"+"\n")

	

	if (retsy.ok) == True:
 
		file.write("[+] Etsy            :     "+"https://www.etsy.com/shop/"+acc+"\n")

	

	if (rbasecamp.ok) == True:
 
		file.write("[+] Basecamp        :     "+"https://"+acc+".basecamphq.com/login"+"\n")


	if (rtracky.ok) == True:
 
		file.write("[+] Tracky          :     "+"https://tracky.com/user/"+acc+"\n")


	if (rokcupid.ok) == True:
 
		file.write("[+] OkCupid         :     "+"https://www.okcupid.com/profile/"+acc+"\n")



	if (rbandcamp.ok) == True:
 
		file.write("[+] Bandcamp        :     "+"https://www.bandcamp.com/"+acc+"\n")

	

	if (rwikipedia.ok) == True:
 
		file.write("[+] Wikipedia       :     "+"https://www.wikipedia.org/wiki/User:"+acc+"\n")

	

	if (rcontently.ok) == True:
 
		file.write("[+] Contently       :     "+"https://"+acc+".contently.com"+"\n")

	

	if (rbitbucket.ok) == True:
 
		file.write("[+] BitBucket       :     "+"https://bitbucket.org/"+acc+"\n")

	

	if (rfotolog.ok) == True:
 
		file.write("[+] Fotolog         :     "+"https://fotolog.com/"+acc+"\n")

	

	if (rdesignspiration.ok) == True:
 
		file.write("[+] Designspiration :     "+"https://www.designspiration.net/"+acc+"\n")

	window.config(cursor='arrow')

	messagebox.showinfo("Info","Results has been successfully saved as "+entry.get()+'.txt')

def rgrab():
	Thread(target=grab).start()

button = Button(window, text='Grab', bg='black', fg='white', font=("Courier",14,"bold"), activebackground='black',relief=GROOVE, activeforeground='white', command=rgrab)
button.place(x=172,y=310)



window.mainloop()



def fonc2():
	Thread(target=fonc).start()
	rpinterest = requests.get("https://www.pinterest.com/"+acc)
	rreddit = requests.get("https://www.reddit.com/user/"+acc)
	rtumblr = requests.get("https://"+acc+".tumblr.com")
	rflickr  = requests.get("https://www.flickr.com/photos/"+acc)
	rsteam   = requests.get("https://steamcommunity.com/id/"+acc)
	rvimeo   = requests.get("https://www.vimeo.com/"+acc)
	rsoundcloud = requests.get("https://www.soundcloud.com/"+acc)
	rdisqus     = requests.get("https://www.disqus.com/"+acc)
	rmedium = requests.get("https://medium.com/@"+acc)
	rdevianart = requests.get("https://"+acc+".deviantart.com")
	raboutme = requests.get("https://about.me/"+acc)
	rimgur = requests.get("https://imgur.com/user/"+acc)
	rflipboard = requests.get("https://www.flipboard.com/@"+acc)
	rslideshare = requests.get("https://www.slideshare.net/"+acc)
	rspotify = requests.get("https://open.spotify.com/user/"+acc)
	rscribd = requests.get("https://www.scribd.com/"+acc)
	rbadoo = requests.get("https://www.badoo.com/en/"+acc)
	rpatreon = requests.get("https://www.patreon.com/"+acc)
	rdailymotion = requests.get("https://www.dailymotion.com/"+acc)
	rcashme = requests.get("https://cash.me/"+acc)
	rbehance = requests.get("https://www.behance.net/"+acc)
	rgoodreads = requests.get("https://www.goodreads.com/"+acc)
	rkeybase = requests.get("https://www.keybase.io/"+acc)
	rkongregate = requests.get("https://kongregate.com/accounts/"+acc)
	rlivejournal = requests.get("https://"+acc+".livejournal.com")
	rangellist = requests.get("https://angel.co/"+acc)
	rlastfm = requests.get("https://last.fm/user/"+acc)
	rdribbble = requests.get("https://dribbble.com/"+acc)
	rcodecademy = requests.get("https://www.codecademy.com/"+acc)
	rgravatar = requests.get("https://en.gravatar.com/"+acc)
	rpastebin = requests.get("https://foursquare.com/"+acc)
	rfoursquare = requests.get("https://foursquare.com/"+acc)
	rroblox = requests.get("https://foursquare.com/"+acc)
	rgumroad = requests.get("https://www.gumroad.com/"+acc)
	rnewgrounds = requests.get("https://"+acc+".newgrounds.com")
	rwattpad = requests.get("https://www.wattpad.com/user/"+acc)
	rcanva = requests.get("https://www.canva.com/"+acc)
	rcreativemarker = requests.get("https://creativemarket.com/"+acc)
	rtrakt = requests.get("https://www.trakt.tv/users/"+acc)
	r500px = requests.get("https://500px.com/"+acc)
	rbuzzfeed = requests.get("https://buzzfeed.com/"+acc)
	rtripadvisor = requests.get("https://tripadvisor.com/members/"+acc)
	rhubpages = requests.get("https://"+acc+".hubpages.com/")
	rhouzz = requests.get("https://houzz.com/user/"+acc)
	rblipfm = requests.get("https://blip.fm/"+acc)
	rhackernews = requests.get("https://news.ycombinator.com/user?id="+acc)
	rcodementor = requests.get("https://www.codementor.io/"+acc)
	rreverbnation = requests.get("https://www.reverbnation.com/"+acc)
	rifttt = requests.get("https://www.ifttt.com/p/"+acc)
	rebay = requests.get("https://www.ebay.com/usr/"+acc)
	rslack = requests.get("https://"+acc+".slack.com")
	rtrip = requests.get("https://www.trip.skyscanner.com/user/"+acc)
	rello = requests.get("https://ello.co/"+acc)
	rtripit = requests.get("https://www.tripit.com/people/"+acc+"#/profile/basic-info")
	retsy = requests.get("https://www.etsy.com/shop/"+acc)
	rbasecamp = requests.get("https://"+acc+".basecamphq.com/login")
	rtracky = requests.get("https://tracky.com/user/"+acc)
	rokcupid = requests.get("https://www.okcupid.com/profile/"+acc)
	rbandcamp = requests.get("https://www.bandcamp.com/"+acc)
	rwikipedia = requests.get("https://www.wikipedia.org/wiki/User:"+acc)
	rcontently = requests.get("https://"+acc+".contently.com")
	rbitbucket = requests.get("https://bitbucket.org/"+acc)
	rfotolog = requests.get("https://fotolog.com/"+acc)
	rdesignspiration = requests.get("https://www.designspiration.net/"+acc)


	file = open(acc+".txt","w")
	file.write(acc+" results !\n")
	file.write("\n")


	if (rfacebook.ok) == True:

		file.write("[+] Facebook        : Found     !   "+"https://www.facebook.com/"+acc+"\n")


	if (rinstagram.ok) == True:

		file.write("[+] instagram       : Found     !   "+"https://www.instagram.com/"+acc+"\n")


	if (rtwitter.ok) == True:

		file.write("[+] Twitter         : Found     !   "+"https://www.twitter.com/"+acc+"\n")


	if (ryoutube.ok) == True:

		file.write("[+] Youtube         : Found     !   "+"https://www.youtube.com/"+acc+"\n")


	if (rvk.ok) == True:

		file.write("[+] Vk              : Found     !   "+"https://www.vk.com/"+acc+"\n")

	if (rlinkedin.ok) == True:

		file.write("[+] Linkedin        : Found     !   "+"https://www.linkedin.com/"+acc+"\n")

	if (rblogger.ok) == True:

		file.write("[+] Blogger         : Found     !   "+"https://"+acc+".blogspot.com"+"\n")


	if (rwordpress.ok) == True : 

		file.write("[+] Wordpress       : Found     !   "+"https://"+acc+".wordpress.com"+"\n")

	if (rgithub.ok) == True:
 
		file.write("[+] Github          : Found     !   "+"https://www.github.com/"+acc+"\n")

	
	if (rpinterest.ok) == True:

		file.write("[+] Pinterest       : Found     !   "+"https://www.pinterest.com/"+acc+"\n")


	if (rreddit.ok) == True:

		file.write("[+] Reddit          : Found     !   "+"https://www.reddit.com/user/"+acc+"\n")


	if (rtumblr.ok) == True:

		file.write("[+] Tumblr          : Found     !   "+"https://"+acc+".tumblr.com"+"\n")

	

	if (rflickr.ok) == True:

		file.write("[+] Flickr          : Found     !   "+"https://www.flickr.com/photos/"+acc+"\n")

	

	if (rflickr.ok) == True:

		file.write("[+] Steam           : Found     !   "+"https://www.steamcommunity.co/id/"+acc+"\n")


	if (rvimeo.ok) == True:

		file.write("[+] Vimeo           : Found     !   "+"https://www.vimeo.com/"+acc+"\n")

	
	if (rsoundcloud.ok) == True:

		file.write("[+] Soundcloud      : Found     !   "+"https://www.soundcloud.com/"+acc+"\n")


	if (rdisqus.ok) == True:

		file.write("[+] Disqus          : Found     !   "+"https://www.disqus.com/"+acc+"\n")

	if (rmedium.ok) == True:

		file.write("[+] Medium          : Found     !   "+"https://www.medium.com/@"+acc+"\n")

	if (rdevianart.ok) == True:

		file.write("[+] DevianART       : Found     !   "+"https://"+acc+".devianart.com/"+"\n")

	
	if (raboutme.ok) == True:

		file.write("[+] About.me        : Found     !   "+"https://about.me/"+acc+"\n")


	if (rimgur.ok) == True:

		file.write("[+] Imgur           : Found     !   "+"https://www.imgur.me/user/"+acc+"\n")


	if (rflipboard.ok) == True:

		file.write("[+] Flipboard       : Found     !   "+"https://www.flipboard.com/@"+acc+"\n")

	

	if (rslideshare.ok) == True:

		file.write("[+] Slideshare      : Found     !   "+"https://www.slideshare.net/"+acc+"\n")



	if (rspotify.ok) == True:

		file.write("[+] Spotify         : Found     !   "+"https://open.spotify.com/user/"+acc+"\n")

	

	if (rscribd.ok) == True:

		file.write("[+] Scribd          : Found     !   "+"https://www.scribd.com/"+acc+"\n")

	
	if (rbadoo.ok) == True:

		file.write("[+] Badoo           : Found     !   "+"https://www.badoo.com/en/"+acc+"\n")

	

	if (rpatreon.ok) == True:

		file.write("[+] Patreon         : Found     !   "+"https://www.patreon.com/"+acc+"\n")

	

	if (rdailymotion.ok) == True:

		file.write("[+] Dailymotion     : Found     !   "+"https://www.dailymotion.com/"+acc+"\n")

	

	if (rcashme.ok) == True:

		file.write("[+] CashMe          : Found     !   "+"https://www.cash.me/"+acc+"\n")


	if (rbehance.ok) == True:

		file.write("[+] Behance         : Found     !   "+"https://www.behance.com/"+acc+"\n")


	if (rgoodreads.ok) == True:

		file.write("[+] GoodReads       : Found     !   "+"https://www.goodreads.com/"+acc+"\n")

	
	if (rkeybase.ok) == True:

		file.write("[+] Keybase         : Found     !   "+"https://www.keybase.io/"+acc+"\n")


	if (rkongregate.ok) == True:

		file.write("[+] Kongregate      : Found     !   "+"https://kongregate.com/accounts/"+acc+"\n")

	

	if (rlivejournal.ok) == True:

		file.write("[+] LiveJournal     : Found     !   "+"https://"+acc+".livejournal.com"+"\n")



	if (rangellist.ok) == True:

		file.write("[+] AngelList       : Found     !   "+"https://angel.co/"+acc+"\n")



	if (rlastfm.ok) == True:

		file.write("[+] Last.fm         : Found     !   "+"https://last.fm/user/"+acc+"\n")

	

	if (rdribbble.ok) == True:

		file.write("[+] Dribble         : Found     !   "+"https://dribbble.com/"+acc+"\n")

	
	if (rcodecademy.ok) == True:

		file.write("[+] Codecademy      : Found     !   "+"https://www.codecademy.com/"+acc+"\n")

	

	if (rgravatar.ok) == True:

		file.write("[+] Gravatar        : Found     !   "+"https://en.gravatar.com/"+acc+"\n")

	

	if (rpastebin.ok) == True:

		file.write("[+] Pastebin        : Found     !   "+"https://pastebin.com/u/"+acc+"\n")
 
	
	if (rfoursquare.ok) == True:

		file.write("[+] Foursquare      : Found     !   "+"https://foursquare.com/"+acc+"\n")

	

	if (rroblox.ok) == True:

		file.write("[+] Roblox          : Found     !   "+"https://foursquare.com/"+acc+"\n")



	if (rgumroad.ok) == True:

		file.write("[+] Gumroad         : Found     !   "+"https://www.gumroad.com/"+acc+"\n")

	

	if (rnewgrounds.ok) == True:

		file.write("[+] Newgrounds      : Found     !   "+"https://"+acc+".newgrounds.com"+"\n")

	
	if (rwattpad.ok) == True:

		file.write("[+] Wattpad         : Found     !   "+"https://www.wattpad.com/user/"+acc+"\n")

	
	if (rcanva.ok) == True:

		file.write("[+] Canva           : Found     !   "+"https://www.canva.com/"+acc+"\n")



	if (rcreativemarker.ok) == True:

		file.write("[+] CreativeMarket  : Found     !   "+"https://creativemarket.com/"+acc+"\n")

	

	if (rtrakt.ok) == True:

		file.write("[+] Trakt           : Found     !   "+"https://www.trakt.tv/users/"+acc+"\n")

	
	if (r500px.ok) == True:

		file.write("[+] 500px           : Found     !   "+"https://500px.com/"+acc+"\n")

	
	if (rbuzzfeed.ok) == True:

		file.write("[+] Buzzfeed        : Found     !   "+"https://buzzfeed.com/"+acc+"\n")

	
	if (rtripadvisor.ok) == True:

		file.write("[+] TripAdvisor     : Found     !   "+"https://tripadvisor.com/members/"+acc+"\n")


	if (rhubpages.ok) == True:

		file.write("[+] HubPages        : Found     !   "+"https://"+acc+".hubpages.com/"+"\n")

	

	if (rhouzz.ok) == True:

		file.write("[+] Houzz           : Found     !   "+"https://houzz.com/user/"+acc+"\n")

	
	if (rblipfm.ok) == True:

		file.write("[+] Blip.fm         : Found     !   "+"https://blip.fm/"+acc+"\n")

	

	if (rhackernews.ok) == True:

		file.write("[+] HackerNews      : Found     !   "+"https://news.ycombinator.com/user?id="+acc+"\n")

	
	if (rcodementor.ok) == True:

		file.write("[+] Codementor      : Found     !   "+"https://www.codementor.io/"+acc+"\n")


	if (rreverbnation.ok) == True:

		file.write("[+] ReverbNation    : Found     !   "+"https://www.reverbnation.com/"+acc+"\n")

	

	if (rifttt.ok) == True:

		file.write("[+] IFTTTT          : Found     !   "+"https://www.ifttt.com/p/"+acc+"\n")


	if (rebay.ok) == True:

		file.write("[+] Ebay            : Found     !   "+"https://www.ebay.com/usr/"+acc+"\n")

	
	if (rslack.ok) == True:

		file.write("[+] Slack           : Found     !   "+"https://"+acc+".slack.com"+"\n")

	

	if (rtrip.ok) == True:

		file.write("[+] Trip            : Found     !   "+"https://www.trip.skyscanner.com/user/"+acc+"\n")

	

	if (rello.ok) == True:

		file.write("[+] Ello            : Found     !   "+"https://ello.co/"+acc+"\n")

	

	if (rtripit.ok) == True:

		file.write("[+] Tripit          : Found     !   "+"https://www.tripit.com/people/"+acc+"#/profile/basic-info"+"\n")

	

	if (retsy.ok) == True:
 
		file.write("[+] Etsy            : Found     !   "+"https://www.etsy.com/shop/"+acc+"\n")

	

	if (rbasecamp.ok) == True:
 
		file.write("[+] Basecamp        : Found     !   "+"https://"+acc+".basecamphq.com/login"+"\n")


	if (rtracky.ok) == True:
 
		file.write("[+] Tracky          : Found     !   "+"https://tracky.com/user/"+acc+"\n")


	if (rokcupid.ok) == True:
 
		file.write("[+] OkCupid         : Found     !   "+"https://www.okcupid.com/profile/"+acc+"\n")



	if (rbandcamp.ok) == True:
 
		file.write("[+] Bandcamp        : Found     !   "+"https://www.bandcamp.com/"+acc+"\n")

	

	if (rwikipedia.ok) == True:
 
		file.write("[+] Wikipedia       : Found     !   "+"https://www.wikipedia.org/wiki/User:"+acc+"\n")

	

	if (rcontently.ok) == True:
 
		file.write("[+] Contently       : Found     !   "+"https://"+acc+".contently.com"+"\n")

	

	if (rbitbucket.ok) == True:
 
		file.write("[+] BitBucket       : Found     !   "+"https://bitbucket.org/"+acc+"\n")

	

	if (rfotolog.ok) == True:
 
		file.write("[+] Fotolog         : Found     !   "+"https://fotolog.com/"+acc+"\n")

	

	if (rdesignspiration.ok) == True:
 
		file.write("[+] Designspiration : Found     !   "+"https://www.designspiration.net/"+acc+"\n")

	window.config(cursor='arrow')

	messagebox.showinfo("Info","Results has been successfully saved as "+entry.get()+'.txt')

def rgrab():
	Thread(target=grab).start()

button = Button(window, text='Grab', bg='black', fg='white', font=("Courier",14,"bold"), activebackground='black',relief=GROOVE, activeforeground='white', command=rgrab)
button.place(x=172,y=310)



window.mainloop()



def fonc2():
	Thread(target=fonc).start()
