from setuptools import setup, find_packages


setup(
    name='django-redmine-models',
    version='0.3',
    url='https://github.com/zvin/django-redmine-models',
    description=(
        'Django models for the Redmine database.'
    ),
    long_description=open('README.rst').read(),
    author='Alexis Svinartchouk',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Groupware',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=['django>=1.7'],
    requires=['django (>=1.7)'],
)
