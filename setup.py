from distutils.core import setup
setup(
    name='heimdall',
    packages=['heimdall'],
    version='0.0.3',
    description='A library for taking website screenshots, whilst emulating various devices and resolutions.',
    author='Distilled R&D',
    author_email='tom.anthony@distilled.net',
    url='https://github.com/DistilledLtd/heimdall',
    download_url='https://github.com/DistilledLtd/heimdall/tarball/0.0.3',
    keywords=['screenshot', 'phantomjs'],
    classifiers=[],
    install_requires=[
        'Pillow',
        'wheel'
    ]
)
