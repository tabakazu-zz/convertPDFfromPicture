import re
import glob,os

class ConvertPDF():
"""
* 指定したフォルダ内の画像ファイルをPDF出力
?PDFの出力場所=>指定したフォルダ内にPDFフォルダを作成してその中に保存
#jpegファイルの場合はpngに変更->何故？

"""

    def convertPNGtoJPG():
        files=glob.glob("./Test/*.png")
        match=re.compile("(png)")

        for file_name in files:
            im=Image.open(file_name)
            im=im.convert("RGB")
            new_file_name=match.sub("jpeg",file_name)
            os.remove(file_name)
            im.save(new_file_name,quality=100)
            print(file_name + "convert is completed")

import os
import img2pdf
from PIL import Image # img2pdfと一緒にインストールされたPillowを使います

if __name__ == '__main__':
    pdf_FileName = "./Test/output.pdf" # 出力するPDFの名前
    png_Folder = "./Test/" # 画像フォルダ
    extension  = ".jpg" # 拡張子がPNGのものを対象

    with open(pdf_FileName,"wb") as f:
        # 画像フォルダの中にあるPNGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(img2pdf.convert([Image.open(png_Folder+j).filename for j in os.listdir(png_Folder)if j.endswith(extension)]))