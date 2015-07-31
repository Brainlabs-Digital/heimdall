

def save(url,
         device=None,
         width=1440,
         height=900,
         format="PNG",
         fullpage=False):
    pass


def png(**kwargs):
    kwargs['format'] = "PNG"
    save(kwargs)


def jpeg(**kwargs):
    kwargs['format'] = "JPEG"
    save(kwargs)


def pdf(**kwargs):
    kwargs['format'] = "PDF"
    save(kwargs)
