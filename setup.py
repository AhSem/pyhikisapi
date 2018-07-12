# Copyright (c) 2018-2022 Chin Sem Chang <https://github.com/AhSem>
# Licensed under the MIT license.

# git tag 0.1 -m "0.1 release"
# git push --tags origin master
#
# Upload to PyPI Live
# python setup.py register -r pypi
# python setup.py sdist upload -r pypi


from distutils.core import setup
setup(
    name='pyisapi',
    packages=['isapi'],
    version='0.0.1',
    description='A wrapper to HIKVISION ISAPI, written in Python.',
    author='Chin Sem Chang',
    author_email='chin.sem.chang@gmail.com',
    url='https://github.com/AhSem/pyhikisapi',
    # download_url='https://github.com/AhSem/pyhikisapi/tarball/0.0.1',
    keywords=['hik', 'hikvision', 'event stream', 'events', 'api wrapper'],
    classifiers=[],
    )
