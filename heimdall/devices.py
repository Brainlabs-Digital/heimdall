DEVICE_ALIASES = {

    # Popular devices - generic name points to latest version
    "iPad":         "Apple iPad 4",
    "iPad mini":    "Apple iPad mini 3",
    "iPhone":       "Apple iPhone 6",
    "Galaxy":       "Samsung Galaxy S4",
    "Nexus":        "Motorola Nexus 6",
    "Nexus 10":     "Samsung Nexus 10",
    "Surface":      "Microsoft Surface",
    "Surface Pro":  "Microsoft Surface Pro",
    "Blackberry":   "Blackberry Z30",
    "Kindle Fire":   "Amazon Kindle Fire",
    "Kindle Fire HD":   "Amazon Kindle Fire HD 8.9 inc",

    # Popular devices - older versions
    "iPhone 4":     "Apple iPhone 4",
    "iPad 1":       "Apple iPad 1",
    "Nexus 5":      "LG Nexus 5",
    "Nexus 7":      "Asus Nexus 7 (v2)",
    "Galaxy S3":    "Samsung Galaxy S3"
}

DEVICES = {
    # Desktops
    "Desktop": (1920, 1080, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"),

    # Laptops
    "Laptop": (1280, 800, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"),

    # Smartphones
    "Apple iPhone 6": (375, 667, "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"),
    "Apple iPhone 5": (320, 568, "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"),
    "Apple iPhone 4": (320, 480, "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5"),
    "Blackberry Z30": (360, 640, "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+"),
    "HTC One": (360, 640, "Mozilla/5.0 (Linux; U; Android 4.2.2; nl-nl; HTC_One_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
    "LG Nexus 5": (360, 640, "Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Mobile Safari/537.36"),
    "Samsung Galaxy S3": (360, 640, "Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
    "Samsung Galaxy S4": (360, 640, "Mozilla/5.0 (Linux; Android 4.4.2; GT-I9505 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36"),

    # Phablets
    "Apple iPhone 6 Plus": (414, 736, "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"),
    "Motorola Nexus 6": (412, 690, "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.20 Mobile Safari/537.36"),
    "Microsoft Lumia 1520": (320, 480, "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 1520)"),
    "Samsung Galaxy Note 3": (360, 640, "Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),

    # Tablets
    "Amazon Kindle Fire HD 8.9 inch": (800, 1280, "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.22 like Chrome/34.0.1847.137 Safari/537.36"),
    "Amazon Kindle Fire": (600, 1024, "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"),
    "Apple iPad Air": (768, 1024, "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"),
    "Apple iPad 4": (768, 1024, "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"),
    "Apple iPad 1": (768, 1024, "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"),
    "Apple iPad mini 3": (768, 1024, "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"),
    "Asus Nexus 7 (v2)": (600, 960, "Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36"),
    "Microsoft Surface Pro": (720, 1280, "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0; Touch)"),
    "Microsoft Surface": (768, 1366, "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0; Touch)"),
    "Samsung Nexus 10": (800, 1280, "Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36"),

}


class heimdallDevice(object):

    def __init__(self, device_name):

        device_name = device_name or 'iPad'

        self.user_agent = None
        self.width = None
        self.height = None

        if device_name in DEVICE_ALIASES:
            w, h, ua = DEVICES[DEVICE_ALIASES[device_name]]
        elif device_name in DEVICES:
            w, h, ua = DEVICES[device_name]

        self.user_agent = ua
        self.width = w
        self.height = h

    def __repr__(self):
        return self.user_agent