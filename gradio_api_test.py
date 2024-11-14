import time
import numpy as np
import soundfile as sf
from gradio_client import Client, file

# 记录开始时间
start_time = time.time()

client = Client("https://5e39fb98f4c11c6f0b.gradio.live")
job = client.submit(
    audio=file('https://funaudiollm.github.io/audios/s2st/zh/zh_prompt.wav'),
    history=[['对所以说你现在的话这个账单的话你既然说能处理那你就想办法处理掉 ', '生成风格: Neutral.; 播报内容: 好的，我来帮你想办法看看怎么处理这个问题。[breath]再耐心等一下。']],
    api_name="/model_chat"
)

for o in job:
    print(o)

# result = job.result()
# # 记录结束时间
# end_time = time.time()

# # 计算总耗时
# elapsed_time = end_time - start_time

# # 合并音频片段
# audio_data_list = []
# for item in result:
#     audio_path = item[1]  # 假设音频路径在结果的第二个位置
#     audio_data, samplerate = sf.read(audio_path)
#     audio_data_list.append(audio_data)

# # 将所有的音频数据拼接起来
# concatenated_audio_data = np.concatenate(audio_data_list)

# # 保存合并后的音频文件
# output_audio_path = "merged_output.wav"
# sf.write(output_audio_path, concatenated_audio_data, samplerate)

# print("预测结果:", result)
# print(f"耗时: {elapsed_time:.2f} 秒")
# print(f"合并后的音频文件路径: {output_audio_path}")