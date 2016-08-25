# -*- mode: python -*-

block_cipher = None


a = Analysis(['idcardgenerator.py'],
             pathex=['C:\\Users\\AIRobot\\Desktop\\idcardgenerator'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('empty.png','C:\\Users\\AIRobot\\Desktop\\idcardgenerator\\empty.png','DATA'),('hei.ttf','C:\\Users\\AIRobot\\Desktop\\idcardgenerator\\hei.ttf','DATA'),
			('fzhei.ttf','C:\\Users\\AIRobot\\Desktop\\idcardgenerator\\fzhei.ttf','DATA'),('ocrb10bt.ttf','C:\\Users\\AIRobot\\Desktop\\idcardgenerator\\ocrb10bt.ttf','DATA'),
			('ico.ico','C:\\Users\\AIRobot\\Desktop\\idcardgenerator\\ico.ico','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='idcardgenerator',
          debug=False,
          strip=False,
          upx=True,
          console=False )
