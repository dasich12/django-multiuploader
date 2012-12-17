ALLOWED_FILE_TYPES = ["txt","zip","jpg","jpeg","flv","png"]

CONTENT_TYPES = ['image', 'video','document','text']

MAX_UPLOAD_SIZE = 10485760
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160

MAX_FILE_NUMBER = 5

MULTI_FILE_DELETE_URL = "multi_delete"
MULTI_FILE_URL = "multi_file"

# Expiration time in seconds, one hour as default
EXPIRATION_TIME = 3600