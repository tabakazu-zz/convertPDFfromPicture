# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import pathlib
import pprint
import re
from PIL import Image
import img2pdf
import glob

# ファイル選択ダイアログの表示
root = tkinter.Tk ()
root.withdraw ()
fTyp = [("", "*")]
iDir = os.path.abspath ( os.path.dirname ( __file__ ) )

# iDirPath=選択したフォルダ名
iDirPath = tkinter.filedialog.askdirectory ( initialdir=iDir )
#iDirName=os.path.basename(os.path.dirname(iDirPath))
iDirName=os.path.basename(iDirPath)

# PDFフォルダ確認->無ければ作成
p = pathlib.Path ( f"{iDirPath}/PDF" )
if not p.exists ():
    p.mkdir ()


#pngファイルを一括返還
p_iDirPath=pathlib.Path(iDirPath)
files=sorted([p for p in p_iDirPath.glob('**/*') if re.search('.*\.(png|PNG)',str(p))])

match = re.compile("(png|PNG)")

for file_name in files:
    im = Image.open(str(file_name))
    im = im.convert("RGB")
    new_file_name = match.sub("jpeg", str(file_name))
    os.remove(str(file_name))
    im.save(new_file_name, quality=100)

    #print(file_name + " convert is completed")

# 画像ファイル一覧を取得
p_iDirPath = pathlib.Path ( iDirPath )

images= sorted( [p for p in p_iDirPath.glob ( '**/*' ) if re.search ( '.*\.(jpg|jpeg|png|bmp)', str ( p ) )] )

#pdfフォルダ内にPDFファイルを作成
with open(f'{iDirPath}/PDF/{iDirName}.pdf','wb') as f:
    f.write(img2pdf.convert([Image.open(str(elem_image)).filename for elem_image in images]))


