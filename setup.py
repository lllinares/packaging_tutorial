from setuptools import setup
from biketrauma_brd import __version__ as current_version

setup(
  name='biketrauma_brda',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/Assiab2707/packaging_tutorial',
  author='Assia Berrandou',
  author_email='assia.berrandou@etu.umontpellier.fr',
  license='MIND',
  packages=['biketrauma_brd','biketrauma_brd.io', 'biketrauma_brd.preprocess', 'biketrauma_brd.vis'],
  zip_safe=False
)