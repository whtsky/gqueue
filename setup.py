from setuptools import setup

version = '0.1'

setup(
    name='GQueue',
    version=version,
    author='whtsky',
    author_email='whtsky@gmail.com',
    url='https://github.com/whtsky/gqueue',
    py_modules=['gqueue'],
    description='GQueue: Simple job queues',
    long_description='',
    install_requires=['gevent'],
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
)
