import datetime
import jwt

secret_key = 'secret'

sample_token = jwt.encode({'video_id': '197', 'access_user': 231}, secret_key, algorithm='HS256')

token_with_issuer = jwt.encode({'video_id': '197', 'access_user': 231, 'iss': 'file operations'}, secret_key, algorithm='HS256')

token_with_issuer_expiry = jwt.encode({'video_id': '197', 'access_user': 231, 'iss': 'file operations', 'exp': datetime.datetime.utcnow()}, secret_key, algorithm='HS256')

print(sample_token)
print(token_with_issuer)
print(token_with_issuer_expiry)
