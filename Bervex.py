__author__ = ("AyoubOurass, ZetSu, Flack, ./Ay0ub")

from urllib.request import urlopen
from tkinter import messagebox 
from tkinter import * 
from PIL import Image,ImageTk
import requests 
from tkinter import ttk 
from tkinter import filedialog
from ttkthemes import themed_tk as tk
from threading import Thread
import time




root = tk.ThemedTk() # main window
root.get_themes()
root.set_theme("blue")
root.title('Bervex v2')
root.iconbitmap(r'Extensions/icon.ico')
root.geometry('300x100')
root.configure(background="black")
root.resizable(False, False)
text = Label(root,text='Select your mode', bg='black', fg='white', font=("Courier",15,"bold"))
text.pack(pady=5)




def singleusernamemode(): 


	root.destroy()
	


	window = tk.ThemedTk()
	window.get_themes()
	window.set_theme("blue")
	window.title('Bervex v2  (Single username mode)')
	window.iconbitmap(r'Extensions/icon.ico')
	window.geometry('400x410')
	window.configure(background="black")
	photo = Image.open("Extensions/image.png").resize((175,175),Image.ANTIALIAS)
	image = ImageTk.PhotoImage(photo)
	picture = Label(window,image=image, bg="black")
	picture.pack()
	window.resizable(False, False)


	text = Label(window, text='Bervex', bg='black', fg='#f6fef9', font=('Papyrus',25,))
	text.place(x=145,y=163)

	text1 = Label(window, text='Username :  ', bg='black', fg='white', font=('Courier',15,'bold'))
	text1.place(x=70,y=251)

	def browse():
		window.dir = filedialog.askdirectory()
		return window.dir


	text2 = Label(window, text='Save directory :  ',bg='black', fg='white', font=('Courier',14,'bold'))
	text2.place(x=70,y=290)

	button100 = ttk.Button(window, text='Browse', command=browse)
	button100.place(x=257,y=288)

	entry = ttk.Entry(window, width=20)
	entry.place(x=200,y=255)

	def grab():
		window.config(cursor="wait")

		acc = entry.get()

		if acc == "":
			messagebox.showerror("Error","No username entered")

		else:

			if ' ' in acc:
				acc = acc.replace(" ","")


		

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


			file32 = open(window.dir+"/"+acc+".txt","w")
			file32.write(acc+" results !\n")
			file32.write("\n")


			if (rfacebook.ok) == True:

				file32.write("[+] Facebook        :     "+"https://www.facebook.com/"+acc+"\n")


			if (rinstagram.ok) == True:

				file32.write("[+] instagram       :     "+"https://www.instagram.com/"+acc+"\n")


			if (rtwitter.ok) == True:

				file32.write("[+] Twitter         :     "+"https://www.twitter.com/"+acc+"\n")


			if (ryoutube.ok) == True:

				file32.write("[+] Youtube         :     "+"https://www.youtube.com/"+acc+"\n")


			if (rvk.ok) == True:

				file32.write("[+] Vk              :     "+"https://www.vk.com/"+acc+"\n")

			if (rlinkedin.ok) == True:

				file32.write("[+] Linkedin        :     "+"https://www.linkedin.com/"+acc+"\n")

			if (rblogger.ok) == True:

				file32.write("[+] Blogger         :     "+"https://"+acc+".blogspot.com"+"\n")


			if (rwordpress.ok) == True : 

				file32.write("[+] Wordpress       :     "+"https://"+acc+".wordpress.com"+"\n")

			if (rgithub.ok) == True:
		 
				file32.write("[+] Github          :     "+"https://www.github.com/"+acc+"\n")

			
			if (rpinterest.ok) == True:

				file32.write("[+] Pinterest       :     "+"https://www.pinterest.com/"+acc+"\n")


			if (rreddit.ok) == True:

				file32.write("[+] Reddit          :     "+"https://www.reddit.com/user/"+acc+"\n")


			if (rtumblr.ok) == True:

				file32.write("[+] Tumblr          :     "+"https://"+acc+".tumblr.com"+"\n")

			

			if (rflickr.ok) == True:

				file32.write("[+] Flickr          :     "+"https://www.flickr.com/photos/"+acc+"\n")

			

			if (rflickr.ok) == True:

				file32.write("[+] Steam           :     "+"https://www.steamcommunity.co/id/"+acc+"\n")


			if (rvimeo.ok) == True:

				file32.write("[+] Vimeo           :     "+"https://www.vimeo.com/"+acc+"\n")

			
			if (rsoundcloud.ok) == True:

				file32.write("[+] Soundcloud      :     "+"https://www.soundcloud.com/"+acc+"\n")


			if (rdisqus.ok) == True:

				file32.write("[+] Disqus          :     "+"https://www.disqus.com/"+acc+"\n")

			if (rmedium.ok) == True:

				file32.write("[+] Medium          :     "+"https://www.medium.com/@"+acc+"\n")

			if (rdevianart.ok) == True:

				file32.write("[+] DevianART       :     "+"https://"+acc+".devianart.com/"+"\n")

			
			if (raboutme.ok) == True:

				file32.write("[+] About.me        :     "+"https://about.me/"+acc+"\n")


			if (rimgur.ok) == True:

				file32.write("[+] Imgur           :     "+"https://www.imgur.me/user/"+acc+"\n")


			if (rflipboard.ok) == True:

				file32.write("[+] Flipboard       :     "+"https://www.flipboard.com/@"+acc+"\n")

			

			if (rslideshare.ok) == True:

				file32.write("[+] Slideshare      :     "+"https://www.slideshare.net/"+acc+"\n")



			if (rspotify.ok) == True:

				file32.write("[+] Spotify         :     "+"https://open.spotify.com/user/"+acc+"\n")

			

			if (rscribd.ok) == True:

				file32.write("[+] Scribd          :     "+"https://www.scribd.com/"+acc+"\n")

			
			if (rbadoo.ok) == True:

				file32.write("[+] Badoo           :     "+"https://www.badoo.com/en/"+acc+"\n")

			

			if (rpatreon.ok) == True:

				file32.write("[+] Patreon         :     "+"https://www.patreon.com/"+acc+"\n")

			

			if (rdailymotion.ok) == True:

				file32.write("[+] Dailymotion     :     "+"https://www.dailymotion.com/"+acc+"\n")

			

			if (rcashme.ok) == True:

				file32.write("[+] CashMe          :     "+"https://www.cash.me/"+acc+"\n")


			if (rbehance.ok) == True:

				file32.write("[+] Behance         :     "+"https://www.behance.com/"+acc+"\n")


			if (rgoodreads.ok) == True:

				file32.write("[+] GoodReads       :     "+"https://www.goodreads.com/"+acc+"\n")

			
			if (rkeybase.ok) == True:

				file32.write("[+] Keybase         :     "+"https://www.keybase.io/"+acc+"\n")


			if (rkongregate.ok) == True:

				file32.write("[+] Kongregate      :     "+"https://kongregate.com/accounts/"+acc+"\n")

			

			if (rlivejournal.ok) == True:

				file32.write("[+] LiveJournal     :     "+"https://"+acc+".livejournal.com"+"\n")



			if (rangellist.ok) == True:

				file32.write("[+] AngelList       :     "+"https://angel.co/"+acc+"\n")



			if (rlastfm.ok) == True:

				file32.write("[+] Last.fm         :     "+"https://last.fm/user/"+acc+"\n")

			

			if (rdribbble.ok) == True:

				file32.write("[+] Dribble         :     "+"https://dribbble.com/"+acc+"\n")

			
			if (rcodecademy.ok) == True:

				file32.write("[+] Codecademy      :     "+"https://www.codecademy.com/"+acc+"\n")

			

			if (rgravatar.ok) == True:

				file32.write("[+] Gravatar        :     "+"https://en.gravatar.com/"+acc+"\n")

			

			if (rpastebin.ok) == True:

				file32.write("[+] Pastebin        :     "+"https://pastebin.com/u/"+acc+"\n")
		 
			
			if (rfoursquare.ok) == True:

				file32.write("[+] Foursquare      :     "+"https://foursquare.com/"+acc+"\n")

			

			if (rroblox.ok) == True:

				file32.write("[+] Roblox          :     "+"https://foursquare.com/"+acc+"\n")



			if (rgumroad.ok) == True:

				file32.write("[+] Gumroad         :     "+"https://www.gumroad.com/"+acc+"\n")

			

			if (rnewgrounds.ok) == True:

				file32.write("[+] Newgrounds      :     "+"https://"+acc+".newgrounds.com"+"\n")

			
			if (rwattpad.ok) == True:

				file32.write("[+] Wattpad         :     "+"https://www.wattpad.com/user/"+acc+"\n")

			
			if (rcanva.ok) == True:

				file32.write("[+] Canva           :     "+"https://www.canva.com/"+acc+"\n")



			if (rcreativemarker.ok) == True:

				file32.write("[+] CreativeMarket  :     "+"https://creativemarket.com/"+acc+"\n")

			

			if (rtrakt.ok) == True:

				file32.write("[+] Trakt           :     "+"https://www.trakt.tv/users/"+acc+"\n")

			
			if (r500px.ok) == True:

				file32.write("[+] 500px           :     "+"https://500px.com/"+acc+"\n")

			
			if (rbuzzfeed.ok) == True:

				file32.write("[+] Buzzfeed        :     "+"https://buzzfeed.com/"+acc+"\n")

			
			if (rtripadvisor.ok) == True:

				file32.write("[+] TripAdvisor     :     "+"https://tripadvisor.com/members/"+acc+"\n")


			if (rhubpages.ok) == True:

				file32.write("[+] HubPages        :     "+"https://"+acc+".hubpages.com/"+"\n")

			

			if (rhouzz.ok) == True:

				file32.write("[+] Houzz           :     "+"https://houzz.com/user/"+acc+"\n")

			
			if (rblipfm.ok) == True:

				file32.write("[+] Blip.fm         :     "+"https://blip.fm/"+acc+"\n")

			

			if (rhackernews.ok) == True:

				file32.write("[+] HackerNews      :     "+"https://news.ycombinator.com/user?id="+acc+"\n")

			
			if (rcodementor.ok) == True:

				file32.write("[+] Codementor      :     "+"https://www.codementor.io/"+acc+"\n")


			if (rreverbnation.ok) == True:

				file32.write("[+] ReverbNation    :     "+"https://www.reverbnation.com/"+acc+"\n")

			

			if (rifttt.ok) == True:

				file32.write("[+] IFTTTT          :     "+"https://www.ifttt.com/p/"+acc+"\n")


			if (rebay.ok) == True:

				file32.write("[+] Ebay            :     "+"https://www.ebay.com/usr/"+acc+"\n")

			
			if (rslack.ok) == True:

				file32.write("[+] Slack           :     "+"https://"+acc+".slack.com"+"\n")

			

			if (rtrip.ok) == True:

				file32.write("[+] Trip            :     "+"https://www.trip.skyscanner.com/user/"+acc+"\n")

			

			if (rello.ok) == True:

				file32.write("[+] Ello            :     "+"https://ello.co/"+acc+"\n")

			

			if (rtripit.ok) == True:

				file32.write("[+] Tripit          :     "+"https://www.tripit.com/people/"+acc+"#/profile/basic-info"+"\n")

			

			if (retsy.ok) == True:
		 
				file32.write("[+] Etsy            :     "+"https://www.etsy.com/shop/"+acc+"\n")

			

			if (rbasecamp.ok) == True:
		 
				file32.write("[+] Basecamp        :     "+"https://"+acc+".basecamphq.com/login"+"\n")


			if (rtracky.ok) == True:
		 
				file32.write("[+] Tracky          :     "+"https://tracky.com/user/"+acc+"\n")


			if (rokcupid.ok) == True:
		 
				file32.write("[+] OkCupid         :     "+"https://www.okcupid.com/profile/"+acc+"\n")



			if (rbandcamp.ok) == True:
		 
				file32.write("[+] Bandcamp        :     "+"https://www.bandcamp.com/"+acc+"\n")

			

			if (rwikipedia.ok) == True:
		 
				file32.write("[+] Wikipedia       :     "+"https://www.wikipedia.org/wiki/User:"+acc+"\n")

			

			if (rcontently.ok) == True:
		 
				file32.write("[+] Contently       :     "+"https://"+acc+".contently.com"+"\n")

			

			if (rbitbucket.ok) == True:
		 
				file32.write("[+] BitBucket       :     "+"https://bitbucket.org/"+acc+"\n")

			

			if (rfotolog.ok) == True:
		 
				file32.write("[+] Fotolog         :     "+"https://fotolog.com/"+acc+"\n")

			

			if (rdesignspiration.ok) == True:
		 
				file32.write("[+] Designspiration :     "+"https://www.designspiration.net/"+acc+"\n")

			window.config(cursor='arrow')

			messagebox.showinfo("Info","Results has been successfully saved as "+entry.get()+'.txt')





			
	def rgrab():
		Thread(target=grab).start()

	button = ttk.Button(window, text='Grab', command=rgrab)
	button.place(x=172,y=350)



	window.mainloop()







button1 = ttk.Button(root,text='Single username',command=singleusernamemode)
button1.place(x=25, y=45)









def multiusernamesmode():
	root.destroy()


	window2 = tk.ThemedTk()
	window2.get_themes()
	window2.set_theme("blue")
	window2.title('Bervex v2  (Multi usernames mode)')
	window2.iconbitmap(r'Extensions/icon.ico')
	window2.geometry('400x410')
	window2.configure(background="black")
	photo2 = Image.open("Extensions/image.png").resize((175,175),Image.ANTIALIAS)
	image2 = ImageTk.PhotoImage(photo2)
	picture2 = Label(window2,image=image2, bg="black")
	picture2.pack()
	window2.resizable(False, False)


	text = Label(window2, text='Bervex', bg='black', fg='#f6fef9', font=('Papyrus',25,))
	text.place(x=145,y=163)

	text1 = Label(window2, text='Usernames list :  ', bg='black', fg='white', font=('Courier',15,'bold'))
	text1.place(x=70,y=251)

	def browse3():
		window2.file = filedialog.askopenfilename(title = "Select usernames list",filetype = (("Text Files", "*.txt"),("All Files","*.*")))
		return window2.file

	button3 = ttk.Button(window2, text='Browse',command=browse3)
	button3.place(x=275,y=251)

	def browse2():
		window2.dir = filedialog.askdirectory()
		return window2.dir


	text500 = Label(window2, text='Save directory  ',bg='black', fg='white', font=('Courier',14,'bold'))
	text500.place(x=70,y=290)
	text3 = Label(window2, text=':',bg='black', fg='white', font=('Courier',14,'bold'))
	text3.place(x=251,y=290)


	button10 = ttk.Button(window2, text='Browse', command=browse2)
	button10.place(x=275,y=288)


	def grab2():
		window2.config(cursor="wait")
		dir2 = window2.dir

		acc2 = window2.file
		filename = open(acc2,"r")
		filename = filename.read().splitlines()
		for uname in filename:
			
			rfacebook = requests.get("https://www.facebook.com/"+uname)
			rinstagram = requests.get("https://www.instagram.com/"+uname)
			rtwitter = requests.get("https://www.twitter.com/"+uname)
			ryoutube = requests.get("https://www.youtube.com/"+uname)
			rvk = requests.get("https://vk.com/"+uname)
			rlinkedin = requests.get("https://www.linkedin.com/"+uname)
			rblogger = requests.get("https://"+uname+".blogspot.com")
			rwordpress = requests.get("https://"+uname+".wordpress.com")
			rgithub = requests.get("https://www.github.com/"+uname)
			rpinterest = requests.get("https://www.pinterest.com/"+uname)
			rreddit = requests.get("https://www.reddit.com/user/"+uname)
			rtumblr = requests.get("https://"+uname+".tumblr.com")
			rflickr  = requests.get("https://www.flickr.com/photos/"+uname)
			rsteam   = requests.get("https://steamcommunity.com/id/"+uname)
			rvimeo   = requests.get("https://www.vimeo.com/"+uname)
			rsoundcloud = requests.get("https://www.soundcloud.com/"+uname)
			rdisqus     = requests.get("https://www.disqus.com/"+uname)
			rmedium = requests.get("https://medium.com/@"+uname)
			rdevianart = requests.get("https://"+uname+".deviantart.com")
			raboutme = requests.get("https://about.me/"+uname)
			rimgur = requests.get("https://imgur.com/user/"+uname)
			rflipboard = requests.get("https://www.flipboard.com/@"+uname)
			rslideshare = requests.get("https://www.slideshare.net/"+uname)
			rspotify = requests.get("https://open.spotify.com/user/"+uname)
			rscribd = requests.get("https://www.scribd.com/"+uname)
			rbadoo = requests.get("https://www.badoo.com/en/"+uname)
			rpatreon = requests.get("https://www.patreon.com/"+uname)
			rdailymotion = requests.get("https://www.dailymotion.com/"+uname)
			rcashme = requests.get("https://cash.me/"+uname)
			rbehance = requests.get("https://www.behance.net/"+uname)
			rgoodreads = requests.get("https://www.goodreads.com/"+uname)
			rkeybase = requests.get("https://www.keybase.io/"+uname)
			rkongregate = requests.get("https://kongregate.com/iounts/"+uname)
			rlivejournal = requests.get("https://"+uname+".livejournal.com")
			rangellist = requests.get("https://angel.co/"+uname)
			rlastfm = requests.get("https://last.fm/user/"+uname)
			rdribbble = requests.get("https://dribbble.com/"+uname)
			rcodecademy = requests.get("https://www.codecademy.com/"+uname)
			rgravatar = requests.get("https://en.gravatar.com/"+uname)
			rpastebin = requests.get("https://foursquare.com/"+uname)
			rfoursquare = requests.get("https://foursquare.com/"+uname)
			rroblox = requests.get("https://foursquare.com/"+uname)
			rgumroad = requests.get("https://www.gumroad.com/"+uname)
			rnewgrounds = requests.get("https://"+uname+".newgrounds.com")
			rwattpad = requests.get("https://www.wattpad.com/user/"+uname)
			rcanva = requests.get("https://www.canva.com/"+uname)
			rcreativemarker = requests.get("https://creativemarket.com/"+uname)
			rtrakt = requests.get("https://www.trakt.tv/users/"+uname)
			r500px = requests.get("https://500px.com/"+uname)
			rbuzzfeed = requests.get("https://buzzfeed.com/"+uname)
			rtripadvisor = requests.get("https://tripadvisor.com/members/"+uname)
			rhubpages = requests.get("https://"+uname+".hubpages.com/")
			rhouzz = requests.get("https://houzz.com/user/"+uname)
			rblipfm = requests.get("https://blip.fm/"+uname)
			rhackernews = requests.get("https://news.ycombinator.com/user?id="+uname)
			rcodementor = requests.get("https://www.codementor.io/"+uname)
			rreverbnation = requests.get("https://www.reverbnation.com/"+uname)
			rifttt = requests.get("https://www.ifttt.com/p/"+uname)
			rebay = requests.get("https://www.ebay.com/usr/"+uname)
			rslack = requests.get("https://"+uname+".slack.com")
			rtrip = requests.get("https://www.trip.skyscanner.com/user/"+uname)
			rello = requests.get("https://ello.co/"+uname)
			rtripit = requests.get("https://www.tripit.com/people/"+uname+"#/profile/basic-info")
			retsy = requests.get("https://www.etsy.com/shop/"+uname)
			rbasecamp = requests.get("https://"+uname+".basecamphq.com/login")
			rtracky = requests.get("https://tracky.com/user/"+uname)
			rokcupid = requests.get("https://www.okcupid.com/profile/"+uname)
			rbandcamp = requests.get("https://www.bandcamp.com/"+uname)
			rwikipedia = requests.get("https://www.wikipedia.org/wiki/User:"+uname)
			rcontently = requests.get("https://"+uname+".contently.com")
			rbitbucket = requests.get("https://bitbucket.org/"+uname)
			rfotolog = requests.get("https://fotolog.com/"+uname)
			rdesignspiration = requests.get("https://www.designspiration.net/"+uname) 


			file666 = open(dir2+"/"+uname+".txt","w")
			file666.write(uname+" results !"+"\n")
			file666.write("\n")

		
			

			if (rfacebook.ok) == True:

				file666.write("[+] Facebook        :     "+"https://www.facebook.com/"+uname+"\n")


			if (rinstagram.ok) == True:

				file666.write("[+] instagram       :     "+"https://www.instagram.com/"+uname+"\n")


			if (rtwitter.ok) == True:

				file666.write("[+] Twitter         :     "+"https://www.twitter.com/"+uname+"\n")


			if (ryoutube.ok) == True:

				file666.write("[+] Youtube         :     "+"https://www.youtube.com/"+uname+"\n")


			if (rvk.ok) == True:

				file666.write("[+] Vk              :     "+"https://www.vk.com/"+uname+"\n")

			if (rlinkedin.ok) == True:

				file666.write("[+] Linkedin        :     "+"https://www.linkedin.com/"+uname+"\n")

			if (rblogger.ok) == True:

				file666.write("[+] Blogger         :     "+"https://"+uname+".blogspot.com"+"\n")


			if (rwordpress.ok) == True : 

				file666.write("[+] Wordpress       :     "+"https://"+uname+".wordpress.com"+"\n")

			if (rgithub.ok) == True:
		 
				file666.write("[+] Github          :     "+"https://www.github.com/"+uname+"\n")

			
			if (rpinterest.ok) == True:

				file666.write("[+] Pinterest       :     "+"https://www.pinterest.com/"+uname+"\n")


			if (rreddit.ok) == True:

				file666.write("[+] Reddit          :     "+"https://www.reddit.com/user/"+uname+"\n")


			if (rtumblr.ok) == True:

				file666.write("[+] Tumblr          :     "+"https://"+uname+".tumblr.com"+"\n")

			

			if (rflickr.ok) == True:

				file666.write("[+] Flickr          :     "+"https://www.flickr.com/photos/"+uname+"\n")

			

			if (rflickr.ok) == True:

				file666.write("[+] Steam           :     "+"https://www.steamcommunity.co/id/"+uname+"\n")


			if (rvimeo.ok) == True:

				file666.write("[+] Vimeo           :     "+"https://www.vimeo.com/"+uname+"\n")

			
			if (rsoundcloud.ok) == True:

				file666.write("[+] Soundcloud      :     "+"https://www.soundcloud.com/"+uname+"\n")


			if (rdisqus.ok) == True:

				file666.write("[+] Disqus          :     "+"https://www.disqus.com/"+uname+"\n")

			if (rmedium.ok) == True:

				file666.write("[+] Medium          :     "+"https://www.medium.com/@"+uname+"\n")

			if (rdevianart.ok) == True:

				file666.write("[+] DevianART       :     "+"https://"+uname+".devianart.com/"+"\n")

			
			if (raboutme.ok) == True:

				file666.write("[+] About.me        :     "+"https://about.me/"+uname+"\n")


			if (rimgur.ok) == True:

				file666.write("[+] Imgur           :     "+"https://www.imgur.me/user/"+uname+"\n")


			if (rflipboard.ok) == True:

				file666.write("[+] Flipboard       :     "+"https://www.flipboard.com/@"+uname+"\n")

			

			if (rslideshare.ok) == True:

				file666.write("[+] Slideshare      :     "+"https://www.slideshare.net/"+uname+"\n")



			if (rspotify.ok) == True:

				file666.write("[+] Spotify         :     "+"https://open.spotify.com/user/"+uname+"\n")

			

			if (rscribd.ok) == True:

				file666.write("[+] Scribd          :     "+"https://www.scribd.com/"+uname+"\n")

			
			if (rbadoo.ok) == True:

				file666.write("[+] Badoo           :     "+"https://www.badoo.com/en/"+uname+"\n")

			

			if (rpatreon.ok) == True:

				file666.write("[+] Patreon         :     "+"https://www.patreon.com/"+uname+"\n")

			

			if (rdailymotion.ok) == True:

				file666.write("[+] Dailymotion     :     "+"https://www.dailymotion.com/"+uname+"\n")

			

			if (rcashme.ok) == True:

				file666.write("[+] CashMe          :     "+"https://www.cash.me/"+uname+"\n")


			if (rbehance.ok) == True:

				file666.write("[+] Behance         :     "+"https://www.behance.com/"+uname+"\n")


			if (rgoodreads.ok) == True:

				file666.write("[+] GoodReads       :     "+"https://www.goodreads.com/"+uname+"\n")

			
			if (rkeybase.ok) == True:

				file666.write("[+] Keybase         :     "+"https://www.keybase.io/"+uname+"\n")


			if (rkongregate.ok) == True:

				file666.write("[+] Kongregate      :     "+"https://kongregate.com/iounts/"+uname+"\n")

			

			if (rlivejournal.ok) == True:

				file666.write("[+] LiveJournal     :     "+"https://"+uname+".livejournal.com"+"\n")



			if (rangellist.ok) == True:

				file666.write("[+] AngelList       :     "+"https://angel.co/"+uname+"\n")



			if (rlastfm.ok) == True:

				file666.write("[+] Last.fm         :     "+"https://last.fm/user/"+uname+"\n")

			

			if (rdribbble.ok) == True:

				file666.write("[+] Dribble         :     "+"https://dribbble.com/"+uname+"\n")

			
			if (rcodecademy.ok) == True:

				file666.write("[+] Codecademy      :     "+"https://www.codecademy.com/"+uname+"\n")

			

			if (rgravatar.ok) == True:

				file666.write("[+] Gravatar        :     "+"https://en.gravatar.com/"+uname+"\n")

			

			if (rpastebin.ok) == True:

				file666.write("[+] Pastebin        :     "+"https://pastebin.com/u/"+uname+"\n")
		 
			
			if (rfoursquare.ok) == True:

				file666.write("[+] Foursquare      :     "+"https://foursquare.com/"+uname+"\n")

			

			if (rroblox.ok) == True:

				file666.write("[+] Roblox          :     "+"https://foursquare.com/"+uname+"\n")



			if (rgumroad.ok) == True:

				file666.write("[+] Gumroad         :     "+"https://www.gumroad.com/"+uname+"\n")

			

			if (rnewgrounds.ok) == True:

				file666.write("[+] Newgrounds      :     "+"https://"+uname+".newgrounds.com"+"\n")

			
			if (rwattpad.ok) == True:

				file666.write("[+] Wattpad         :     "+"https://www.wattpad.com/user/"+uname+"\n")

			
			if (rcanva.ok) == True:

				file666.write("[+] Canva           :     "+"https://www.canva.com/"+uname+"\n")



			if (rcreativemarker.ok) == True:

				file666.write("[+] CreativeMarket  :     "+"https://creativemarket.com/"+uname+"\n")

			

			if (rtrakt.ok) == True:

				file666.write("[+] Trakt           :     "+"https://www.trakt.tv/users/"+uname+"\n")

			
			if (r500px.ok) == True:

				file666.write("[+] 500px           :     "+"https://500px.com/"+uname+"\n")

			
			if (rbuzzfeed.ok) == True:

				file666.write("[+] Buzzfeed        :     "+"https://buzzfeed.com/"+uname+"\n")

			
			if (rtripadvisor.ok) == True:

				file666.write("[+] TripAdvisor     :     "+"https://tripadvisor.com/members/"+uname+"\n")


			if (rhubpages.ok) == True:

				file666.write("[+] HubPages        :     "+"https://"+uname+".hubpages.com/"+"\n")

			

			if (rhouzz.ok) == True:

				file666.write("[+] Houzz           :     "+"https://houzz.com/user/"+uname+"\n")

			
			if (rblipfm.ok) == True:

				file666.write("[+] Blip.fm         :     "+"https://blip.fm/"+uname+"\n")

			

			if (rhackernews.ok) == True:

				file666.write("[+] HackerNews      :     "+"https://news.ycombinator.com/user?id="+uname+"\n")

			
			if (rcodementor.ok) == True:

				file666.write("[+] Codementor      :     "+"https://www.codementor.io/"+uname+"\n")


			if (rreverbnation.ok) == True:

				file666.write("[+] ReverbNation    :     "+"https://www.reverbnation.com/"+uname+"\n")

			

			if (rifttt.ok) == True:

				file666.write("[+] IFTTTT          :     "+"https://www.ifttt.com/p/"+uname+"\n")


			if (rebay.ok) == True:

				file666.write("[+] Ebay            :     "+"https://www.ebay.com/usr/"+uname+"\n")

			
			if (rslack.ok) == True:

				file666.write("[+] Slack           :     "+"https://"+uname+".slack.com"+"\n")

			

			if (rtrip.ok) == True:

				file666.write("[+] Trip            :     "+"https://www.trip.skyscanner.com/user/"+uname+"\n")

			

			if (rello.ok) == True:

				file666.write("[+] Ello            :     "+"https://ello.co/"+uname+"\n")

			

			if (rtripit.ok) == True:

				file666.write("[+] Tripit          :     "+"https://www.tripit.com/people/"+uname+"#/profile/basic-info"+"\n")

			

			if (retsy.ok) == True:
		 
				file666.write("[+] Etsy            :     "+"https://www.etsy.com/shop/"+uname+"\n")

			

			if (rbasecamp.ok) == True:
		 
				file666.write("[+] Basecamp        :     "+"https://"+uname+".basecamphq.com/login"+"\n")


			if (rtracky.ok) == True:
		 
				file666.write("[+] Tracky          :     "+"https://tracky.com/user/"+uname+"\n")


			if (rokcupid.ok) == True:
		 
				file666.write("[+] OkCupid         :     "+"https://www.okcupid.com/profile/"+uname+"\n")



			if (rbandcamp.ok) == True:
		 
				file666.write("[+] Bandcamp        :     "+"https://www.bandcamp.com/"+uname+"\n")

			

			if (rwikipedia.ok) == True:
		 
				file666.write("[+] Wikipedia       :     "+"https://www.wikipedia.org/wiki/User:"+uname+"\n")

			

			if (rcontently.ok) == True:
		 
				file666.write("[+] Contently       :     "+"https://"+uname+".contently.com"+"\n")

			

			if (rbitbucket.ok) == True:
		 
				file666.write("[+] BitBucket       :     "+"https://bitbucket.org/"+uname+"\n")

			

			if (rfotolog.ok) == True:
		 
				file666.write("[+] Fotolog         :     "+"https://fotolog.com/"+uname+"\n")

			

			if (rdesignspiration.ok) == True:
		 
				file666.write("[+] Designspiration :     "+"https://www.designspiration.net/"+uname+"\n")

		window2.config(cursor='arrow')

		messagebox.showinfo("Info","Results has been successfully saved to "+dir2)


	def rgrab2():
		Thread(target=grab2).start()

	button5 = ttk.Button(window2, text='Grab', command=rgrab2)
	button5.place(x=172,y=350)



	window2.mainloop()


button2 = ttk.Button(root,text='Multi usernames ', command=multiusernamesmode).place(x=155,y=45)


try:
	response = urlopen('https://www.google.com/', timeout=10)
	pass
except: 
	root.config(cursor="wait")
	time.sleep(1)
	root.config(cursor="arrow")
	messagebox.showwarning("Warning","Maybe you are not connected to internet, check your intrnet connection and try again")
	quit()


root.mainloop()


















