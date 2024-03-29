import os
import pandas as pd

from module.wav_detector import WavDetector


class MyTest(object):
    def __init__(self):
        pass

    @staticmethod
    def load_files():
        files = os.listdir('files')
        return files

    def ts_wav_detector(self):
        files = self.load_files()
        result = []
        for file in files:
            if not  file.endswith('wav'):
                continue
            wav_detector = WavDetector('files/' + file)

            features = wav_detector.extract_features()
            features['file'] = file
            result.append(features)
        df = pd.DataFrame(result)
        df.to_excel('result.xlsx', index=False)


if __name__ == '__main__':
    ts = MyTest()
    ts.ts_wav_detector()
