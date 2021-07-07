from freesms  import FreeClient

f = FreeClient(user="...", passwd="...")
resp = f.send_sms("hello this is my SMS")
resp.status_code  # 200