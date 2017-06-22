try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(  description= 'Time Locker',
        author= 'Sannidhya Sandheer',
        url= 'https://github.com/bhediathewolf/timelocker',
        download_url= 'https://github.com/bhediathewolf/timelocker',
        author_email= 'bhediathewolf@gmail.com',
        version='0',
        install_requires= [],
        packages= ['timelocker'],
        scripts= [],
        name= 'timelocker')
