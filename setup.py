from distutils.core import setup

import anyjson
author, email = anyjson.__author__[:-1].split(' <')

setup(name='anyjson',
      version=anyjson.__version__,
      description=anyjson.__doc__,
      long_description="""""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='json',
      author=author,
      author_email=email,
      url='http://bitbucket.org/runeh/anyjson',
      license='BSD',
      modules=["anyjson.py"],
      include_package_data=True,
      zip_safe=False
      )
