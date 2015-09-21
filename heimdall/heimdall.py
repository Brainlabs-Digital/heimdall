import os
import re
import subprocess
from collections import namedtuple

from PIL import Image

from devices import heimdallDevice

Screenshot = namedtuple('Screenshot', ['path', 'directory', 'filename', 'ext'])


def save(url, *args, **kwargs):
    """ Parse the options, set defaults and then fire up PhantomJS. """

    device = heimdallDevice(kwargs.get('device', None))

    kwargs['width'] = kwargs.get('width', None) or device.width
    kwargs['height'] = kwargs.get('height', None) or device.height
    kwargs['user_agent'] = kwargs.get('user_agent', None) or device.user_agent

    screenshot_image = screenshot(url, **kwargs)

    if kwargs.get('optimize'):
        image = Image.open(screenshot_image.path)
        image.save(screenshot_image.path, optimize=True)

    return screenshot_image


def png(url, *args, **kwargs):
    kwargs['format'] = "PNG"
    return save(url, **kwargs)


def jpeg(url, *args, **kwargs):
    kwargs['format'] = "JPEG"
    return save(url, **kwargs)


def pdf(url, *args, **kwargs):
    kwargs['format'] = "PDF"
    return save(url, **kwargs)


def screenshot(url, *args, **kwargs):
    """ Call PhantomJS with the specified flags and options. """

    phantomscript = os.path.join(os.path.dirname(__file__),
                                 'take_screenshot.js')

    directory = kwargs.get('save_dir', '/tmp')
    image_name = kwargs.get('image_name', None) or _image_name_from_url(url)
    ext = kwargs.get('format', 'png').lower()
    save_path = os.path.join(directory, image_name) + '.' + ext
    crop_to_visible = kwargs.get('crop_to_visible', False)

    cmd_args = [
        'phantomjs',
        '--ssl-protocol=any',
        phantomscript,
        url,
        '--width',
        str(kwargs['width']),
        '--height',
        str(kwargs['height']),
        '--useragent',
        str(kwargs['user_agent']),
        '--dir',
        directory,
        '--ext',
        ext,
        '--name',
        str(image_name),
    ]
    if crop_to_visible:
        cmd_args.append('--croptovisible')

    # TODO:
    # - quality
    # - renderafter
    # - maxexecutiontime
    # - resourcetimeout

    output = subprocess.Popen(cmd_args,
                              stdout=subprocess.PIPE).communicate()[0]

    return Screenshot(save_path, directory, image_name + '.' + ext, ext)


def _image_name_from_url(url):
    """ Create a nice image name from the url. """

    find = r'https?://|[^\w]'
    replace = '_'
    return re.sub(find, replace, url).strip('_')


def debug():
    """ Debug function - runs if heimdall called directly. """

    png('https://www.distilled.net/', device="iPhone")

if __name__ == '__main__':
    debug()
