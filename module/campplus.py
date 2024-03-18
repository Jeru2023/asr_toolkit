from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

if __name__ == '__main__':
    audio_in = 'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_speaker_demo.wav'
    output_dir = "./results"
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='yeyupiaoling/speech_paraformer-large-campplus-vad-punc-spk_asr_nat-zh-cn',
        vad_model='damo/speech_fsmn_vad_zh-cn-16k-common-pytorch',
        punc_model='damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch',
        output_dir=output_dir,
    )
    rec_result = inference_pipeline(audio_in=audio_in, batch_size_token=5000, batch_size_token_threshold_s=40, max_single_segment_time=6000)
    print(rec_result)
    