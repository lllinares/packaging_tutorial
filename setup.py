from setuptools import setup
from biketrauma_brd import __version__ as current_version

setup(
  name='biketrauma_brd',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/xxxxxxxxxxx.git',
  author='xxxxxxxxxxx',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['biketrauma_brd','biketrauma_brd.io', 'biketrauma_brd.preprocess', 'biketrauma_brd.vis'],
  zip_safe=False
)