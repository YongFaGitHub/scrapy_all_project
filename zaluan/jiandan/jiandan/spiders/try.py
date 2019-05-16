
import base64

a = "Ly93eDIuc2luYWltZy5jbi9tdzYwMC82NjFlYjk1Y2x5MWZ1ejM1aXRkM3NqMjB4YzFveXF2NS5qcGc="



def decode_base64(data):
    missing_padding=4-len(data)%4
    if missing_padding:
        data += '='* missing_padding
    return base64.b64decode(data)


b = decode_base64(a).decode('utf8')
print(b)


