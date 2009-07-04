from setuptools import setup

import anyjson
author, email = anyjson.__author__[:-1].split(' <')

setup(name='anyjson',
      version=anyjson.__version__,
      description=anyjson.__doc__,
      long_description=open("README").read(),
      classifiers=[
            'License :: OSI Approved :: BSD License',
            'Intended Audience :: Developers',
            'Programming Language :: Python'
            ],
      keywords='json',
      author=author,
      author_email=email,
      url='http://bitbucket.org/runeh/anyjson',
      license='BSD',
      py_modules=['anyjson'],
      zip_safe=False,
      platforms=["any"],
)
