import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joyful_text(self):
        self.assertEqual(emotion_detector(GetStatement('joy'))['dominant_emotion'], 'joy')
    def test_angry_text(self):
        self.assertEqual(emotion_detector(GetStatement('anger'))['dominant_emotion'], 'anger')
    def test_disgusted_text(self):
        self.assertEqual(emotion_detector(GetStatement('disgust'))['dominant_emotion'], 'disgust')
    def test_sad_text(self):
        self.assertEqual(emotion_detector(GetStatement('sadness'))['dominant_emotion'], 'sadness')
    def test_fearful_text(self):
        self.assertEqual(emotion_detector(GetStatement('fear'))['dominant_emotion'], 'fear')
    
def GetStatement(emotion):
    statements = {
            'joy': 'I am glad this happened',
            'anger': 'I am really mad about this',
            'disgust': 'I feel disgusted just hearing about this',
            'sadness': 'I am so sad about this',
            'fear': 'I am really afraid that this will happen'
        }
    return statements[emotion]

unittest.main()