from distutils.core import setup

setup(
    name='django-availability',
    version='0.1.0',
    author='dashavoo',
    author_email='',
    packages=['availability'],
    url='https://github.com/dashavoo/django-availability',
    license='LICENSE.txt',
    description='Manage availability of objects in Django',
    long_description=open('README.md').read(),
    zip_safe = False,
    include_package_data=True,
)
