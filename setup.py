from setuptools import setup

setup(name='idcardgenerator',
      version='0.0.2',
      description='idcardgenerator',
      url='https://github.com/airob0t/idcardgenerator',
      author='airobot',
      author_email='airobot@airobot.link',
      license='GPL-3.0',
      packages=['idcardgenerator'],
      # data_files=['idcardgenerator/usedres/empty.png', 'idcardgenerator/usedres/fzhei.ttf', 'idcardgenerator/usedres/hei.ttf', 'idcardgenerator/usedres/ico.icns', 'idcardgenerator/usedres/ocrb10bt.ttf'],
      include_package_data=True,
      install_requires=['numpy', 'pillow', 'opencv-python']
      )
