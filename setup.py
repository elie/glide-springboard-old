#!/usr/bin/env python


from setuptools import setup

setup(name='Glide airbnb',
      version='1.1',
      description='airbnb themes for Glide.',
      author='Elie Schoppik',
      author_email='eschoppik@gmail.com',
      url='https://github.com/elie/glide-airbnb',
      packages=['glide_airbnb'],
      install_requires=["glide"],
      include_package_data=True,
     )
