# jakewu
#fblink

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))