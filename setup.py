from setuptools import setup

setup(name='surfpy',
      version='0.97.3',
      description='Wave and weather tools written in pure python',
      url='https://github.com/mpiannucci/surfpy',
      author='Matthew Iannucci',
      author_email='rhodysurf13@gmail.com',
      license='MIT',
      packages=['surfpy'],
      install_requires=['pygrib', 'requests', 'pytz'],
      test_suite='nose.collector',
      tests_require=['nose'],
      setup_requires=['nose>=1.0'],
      zip_safe=False)
