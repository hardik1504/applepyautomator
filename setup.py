from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name='applepyautomator',
  packages=['applepyautomator'],
  version='0.2',
  license='MIT',
  description='applepyautomator is a simplified implementation of applescript automation for macOs in python3. With applepyautomator you can easily automate ur macOs without having to write applescript or using automator.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author='Hardik Sharma',
  author_email='sharmahardikdev@gmail.com',
  url='https://github.com/hardik1504/applepyautomator',
  download_url='https://github.com/hardik1504/applepyautomator/archive/v_0.2.tar.gz',
  keywords=['applescript', 'automation'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Environment :: MacOS X'
  ],
)
