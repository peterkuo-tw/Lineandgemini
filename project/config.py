import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# LINE Bot 設定
LINE_CHANNEL_SECRET = os.environ.get("70db86fcabf3d431f77e03ce76c8422a")
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("dBoPfPOoIT0POeSL9E3/KXCgIuQ9PslP0c/7kpOekIH64bii0MM0nhozkL2tYRSuTo/5cWxC+IKFTCahVz0SLdi+jRzMqaFIS7PL1BcHXuEsxeJdn7wv1iBuFhCm85YjVIIrIODqvMi5eS140On55wdB04t89/1O/w1cDnyilFU=")
GOOGLE_API_KEY = os.environ.get('AIzaSyDkxu2wWY8PKIvGB1VDsEVUvUVSULh39uU')
FIREBASE_URL = os.environ.get('https://line-and-gemini-default-rtdb.firebaseio.com')
