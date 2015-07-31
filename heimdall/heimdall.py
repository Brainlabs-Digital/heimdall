import os
import re
import subprocess

from devices import heimdallDevice


def save(url, *args, **kwargs):

    device = heimdallDevice("iPad")

    kwargs['width'] = kwargs.get('width', None) or device.width
    kwargs['height'] = kwargs.get('height', None) or device.height
    kwargs['user_agent'] = kwargs.get('user_agent', None) or device.user_agent

    screenshot(url, **kwargs)


def png(**kwargs):
    kwargs['format'] = "PNG"
    save(kwargs)


def jpeg(**kwargs):
    kwargs['format'] = "JPEG"
    save(kwargs)


def pdf(**kwargs):
    kwargs['format'] = "PDF"
    save(kwargs)


def screenshot(url, *args, **kwargs):

    phantomscript = os.path.join(os.path.dirname(__file__),
                                 'take_screenshot.js')

    image_name = kwargs.get('image_name', None) or _image_name_from_url(url)

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
        str(kwargs.get('save_dir', '/tmp')),
        '--ext',
        str(kwargs.get('format', 'png').lower()),
        '--name',
        str(image_name),
    ]

    print cmd_args

    # TODO:
    # - croptovisible
    # - quality
    # - renderafter
    # - maxexecutiontime
    # - resourcetimeout

    output = subprocess.Popen(cmd_args,
                              stdout=subprocess.PIPE).communicate()[0]

    print output

    # return save_path


def _image_name_from_url(url):
    """Create an image name from the url"""

    find = r'https?://|[^\w]'
    replace = '_'
    return re.sub(find, replace, url).strip('_')


def debug():
    device = heimdallDevice("iPad")

    print device.width
    print device.height
    print device.user_agent

    save('https://www.apple.com')

if __name__ == '__main__':
    debug()
