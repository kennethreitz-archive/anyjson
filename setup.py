from setuptools import setup, find_packages

import anyjson.metadata as meta
author, email = meta.__author__[:-1].split(' <')

setup(name='anyjson',
      version=meta.__version__,
      description=meta.__doc__,
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
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      platforms=["any"],
      test_suite = 'nose.collector',
)
