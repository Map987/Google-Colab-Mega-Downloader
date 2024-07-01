# Google-Colab-Mega-Downloader
Download Mega.nz into Google Drive

Open in Colab
→
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/Map987/Google-Colab-Mega-Downloader/blob/master/Mega_Drive.ipynb)

## 安装
```
!apt-get update; apt --fix-broken install; sudo apt-get install -y asciidoc; apt-get install -y libglib2.0-dev
!curl 'https://megatools.megous.com/builds/megatools-1.10.3.tar.gz' | tar xz
%cd megatools-1.10.3/
!./configure; make; make install
```
## 下载链接
```
!megadl --path '/content' 'https://mega.nz/folder/QzMTCCTQ#GtY46oxHOa4CMrF_W__f_w'
```
