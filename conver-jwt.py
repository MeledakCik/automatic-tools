import base64
import json

# Token JWT dari auth_token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrYWthbmdrYXN5YWZAZ21haWwuY29tIiwiaWRfaGNtX2thcnlhd2FuIjoiMTEyMjAxNTAzNDAwMTEiLCJncm91cF91c2VyIjoicmVxdWVzdGVyIiwiZXhwIjoxNzMzMjE4MTYyfQ.1HYfmzqP2B74a2j8ZsJj5QdyGKiMm72TaBlqdkSKdr4"

# Pisahkan payload
payload_encoded = auth_token.split('.')[1]
payload_decoded = base64.urlsafe_b64decode(payload_encoded + "==").decode('utf-8')

# Parse JSON
payload = json.loads(payload_decoded)

# Ambil informasi nama/email
nama = payload.get("sub", "Nama tidak ditemukan")
print(f"Nama: {nama}")
