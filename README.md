# Introduction

Heimdall is a python library that makes it very straightforward to quickly and easily create screenshots from web pages:

	heimdall.png("https://www.distilled.net/", device="Kindle Fire")

Heimdall knows about lots of common devices, and can simulate them (their resolution and user agent) when you request a screenshot. For example, you could take a screenshot as an original iPad might see a page. However, you can also specify resolution and user agent yourself.

You can also specify what format you'd like the output in, and whether you want to crop the image based on the display size, or if you would rather get the whole webpage.

NOTE: Heimdall uses PhantomJS and as such does not fully support device-pixel-ratio for emulating devices with hige density displays - this doesn't seem to matter for most purposes but you should be aware. There is a [$1000 bounty](https://github.com/ariya/phantomjs/issues/10964) for anyone who can get the functionality added to PhantomJS.

# Installing Heimdall

Firstly, you need to install [phantomjs](http://phantomjs.org/):

	npm install phantomjs
	
If you get any problems try: npm install -g phantomjs
	
Then simply install Heimdall via pip:

	pip install heimdall

You should now be good to go.

# Using Heimdall



Quick and easy:

	from heimdall import heimdall

	heimdall.png("https://www.distilled.net/", device="Kindle Fire")
	heimdall.jpeg("https://www.facebook.com/", device="iPhone") # Will use iPhone 6
	heimdall.pdf("http://news.ycombinator.com", device="iPhone 3") # Specify a device version
	heimdall.pdf("https://twitter.com/", device="Laptop")

	heimdall.png("https://github.com/", crop_to_visible=True) # Crop the image
	heimdall.png("http://www.tomanthony.co.uk/", width=1440, height=900) # Specify own display size

You can get information about the screenshot you took:

	screenshot = heimdall.png("https://www.distilled.net/", width=1440, height=900)

	screenshot.filename # www_distilled_net.png
	screenshot.path # /tmp/www_distilled_net.png
	screenshot.directory # /tmp
	screenshot.ext # png

If you want to would like to pass the file type in as a parameter for whatever reason, then that is easy:

	heimdall.save("https://www.distilled.net/", format="PNG", device="Galaxy S3")

You can specify an `optimize` flag should you want the image optimized on save:

	heimdall.png("https://www.distilled.net/", optimize=True , device="Galaxy S3")

# To Do

- It would be nice to resolve the device-pixel-ratio issue. PhantomJS is moving from QtWebKit to a Blink based engine, so hopefully we will see this resolved down the line.
- renderafter functionality to wait a certain amount of time before screenshotting

# Why Heimdall?

Heimdall is the all seeing god of Norse mythology, and this was a hackday project so we got stuck there. :)

# Thanks

We are using Johan Dahlberg's fantastic [optparse-js library](https://github.com/jfd/optparse-js/blob/master/lib/optparse.js).

Thanks to [Raphaël Goetter](https://twitter.com/goetter) for (http://mydevice.io/), which we used to get some device resolutions.

# Contributing

See CONTRIBUTING file.

# License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License

See LICENSE file.
