# idcardgenerator
【仅做研究使用，请遵守当地法律法规，法律后果自负】

身份证图片生成工具,填入信息，选择一张头像图片,即可生成黑白和彩色身份证图片。

可以选择是否自动抠图，自动抠图目前仅支持纯色背景，对自动抠图效果不满意可以手动抠图。

在线抠图地址:(https://burner.bonanza.com/)

(https://www.gaoding.com/koutu)

## 更新:
- 1.自动改变头像大小
- 2.自动从纯色背景中抠图
- 3.需要安装opencv

## ToDo
- 自动从复杂背景下抠图

## 环境
- numpy
- pillow
- opencv

## 下载
### Windows
[下载](https://github.com/airob0t/idcardgenerator/releases/download/win_v1.2/idcardgenerator.exe)
### Mac
[下载](https://github.com/airob0t/idcardgenerator/releases/download/v1.1/idcardgenerator)

## 打包程序

安装pyinstaller

`pip install pyinstaller`

Mac打包(打包成Mac app尚有问题未解决)

    pyinstaller -i usedres/ico.icns --windowed --clean --noconfirm --onefile --add-data ./usedres:./usedres idcardgenerator.py

Windows打包

    pyinstaller -i usedres/ico.ico --windowed --clean --noconfirm --onefile --add-data usedres;usedres idcardgenerator.py

## 参照标准：
### 正面
　　“姓名”、“性别”、“民族”、“出生年月日”、“住址”、“公民身份号码”为6号黑体字，用蓝色油墨印刷；登记项目中的姓名项用5号黑体字印刷；其他项目则用小5号黑体字印刷；出生年月日 方正黑体简体字符大小：姓名＋号码（11点）其他（9点）字符间距（AV）：号码（50）字符行距：住址（12点）；身份证号码字体   OCR-B 10 BT   文字 华文细黑。

### 背面
　　左上角为国徽，用红色油墨印刷;其右侧为证件名称“中华人民共和国居民身份证”，分上下两排排列，其中上排的“中华人民共和国”为4号宋体字，下排的“居民身份证”为2号宋体字;“签发机关”、“有效期限”为6号加粗黑体字;签发机关登记项采用，“xx市公安局”;有效期限采用“xxxx.xx-xxxx.xx.xx”格式，使用5号黑体字印刷，全部用黑色油墨印刷。
