#!/usr/bin/env python


from setuptools import setup

setup(name='Glide Springboard Old',
      version='1.1',
      description='springboard themes for Glide.',
      author='Elie Schoppik',
      author_email='eschoppik@gmail.com',
      url='https://github.com/elie/glide-springboard-old',
      packages=['glide_springboard_old'],
      install_requires=["glide"],
      include_package_data=True,
      entry_points={
        'sphinx.html_themes': [
            'revealjs-springboard = glide_springboard_old',
            'handouts-springboard = glide_springboard_old',
        ],
    },
)
