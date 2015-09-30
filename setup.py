from distutils.core import setup

setup(
    name='heimdall',
    packages=['heimdall'],
    version='0.0.6',
    description='A library for taking website screenshots, whilst emulating various devices and resolutions.',
    author='Distilled R&D',
    author_email='tom.anthony@distilled.net',
    url='https://github.com/DistilledLtd/heimdall',
    download_url='https://github.com/DistilledLtd/heimdall/tarball/0.0.6',
    package_data={'': ['take_screenshot.js', 'optparse.js']},
    keywords=['screenshot', 'phantomjs'],
    classifiers=[],
    install_requires=[
        'Pillow',
        'wheel'
    ]
)
