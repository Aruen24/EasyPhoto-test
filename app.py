from easyphoto.easyphoto_ui import on_ui_tabs
from easyphoto.easyphoto_utils import reload_javascript
import os
os.environ["CUDA_VISIBLE_DEVICES"]='0'
# 下载的模型都会默认下载到你设置的目录
# os.environ['MODELSCOPE_CACHE']='./facechain_models'
os.environ['MODELSCOPE_CACHE']='G:\\easyphoto_models'

if __name__ == "__main__": 
    reload_javascript()
    easyphoto = on_ui_tabs()
    easyphoto.queue(status_update_rate=1).launch()