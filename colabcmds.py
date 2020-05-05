# Copying data_src.mp4 and data_dst.mp4 from your Google Drive to Google Colab environment
#Mount Google Drive as folder
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

!cp /content/drive/My\ Drive/data_src.mp4 /content/workspace
!cp /content/drive/My\ Drive/data_dst.mp4 /content/workspace

!ls /content/workspace
