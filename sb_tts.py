# sb_tts.py
# sb 2024-6-12
# 封装ChatTTS语音合成函数

import torchaudio
import torch
from ChatTTS import ChatTTS
import soundfile
from IPython.display import Audio

chat = ChatTTS.Chat()

# 加载默认下载的模型
chat.load(compile=False) # 设置为Flase获得更快速度，设置为True获得更佳效果

# 使用随机音色
# speaker = chat.sample_random_speaker()

# 载入保存好的音色
speaker = torch.load('speaker/speaker_5_girl.pth')

def sb_tts(text, oral=3, laugh=3, bk=3):
    
    '''
    输入文本，输出音频
    '''
    
    # 句子全局设置：讲话人音色和速度
    params_infer_code = ChatTTS.Chat.InferCodeParams(
        spk_emb = speaker, # add sampled speaker 
        temperature = .3,   # using custom temperature
        top_P = 0.7,        # top P decode
        top_K = 20,         # top K decode
    )
    
    ###################################
    # For sentence level manual control.

    # 句子全局设置：口语连接、笑声、停顿程度
    # oral：连接词，AI可能会自己加字，取值范围 0-9，比如：卡壳、嘴瓢、嗯、啊、就是之类的词。不宜调的过高。
    # laugh：笑，取值范围 0-9
    # break：停顿，取值范围 0-9
    # use oral_(0-9), laugh_(0-2), break_(0-7)
    # to generate special token in text to synthesize.
    params_refine_text = ChatTTS.Chat.RefineTextParams(
        prompt='[oral_{}][laugh_{}][break_{}]'.format(oral, laugh, bk)
    )
    
    wavs = chat.infer(text, params_refine_text=params_refine_text, params_infer_code=params_infer_code)
    
    return wavs
    

    
    
    
    