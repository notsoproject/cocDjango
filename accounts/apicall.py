import requests

headers = {
    # 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhiOGFjYzE3LWNkODItNGI3MS1hNjUwLWQ3N2JiMjczMGU0OCIsImlhdCI6MTcyMTgyOTEwOCwic3ViIjoiZGV2ZWxvcGVyL2Q4NmY2N2EwLWJhOWItMWRkOS0xZjI0LWZiMDE4YzliY2U2NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xODEuMjI2LjIxIl0sInR5cGUiOiJjbGllbnQifV19.yNmEtKS5JNwEWhQ1Kicggi3OsIxLVmiZrZJmprm_7yRkO2vLhuHrbJw8H5R_pMfM2DJLpJyE_f4_vqljdC70sQ'
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRkY2VhODY1LWZlZWQtNGUzZS05MDliLWQ1MGFkNTI4NTMyYSIsImlhdCI6MTcyMDkzODE1MSwic3ViIjoiZGV2ZWxvcGVyL2Q4NmY2N2EwLWJhOWItMWRkOS0xZjI0LWZiMDE4YzliY2U2NyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xMzQuNzIuMTMwIl0sInR5cGUiOiJjbGllbnQifV19.v2CKQJYaz0meR_ygIkRAjQ3tWEcHsMtcFn3EKDg3NA52w4xaG65q-MJZbCdf_Tq42982BwGs8L1_unMDTsqU1w'
    # 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA0MGU1Zjk2LWRjNTktNDQ4Ny04Y2UwLTY1NGY0MmU1ZWE4YyIsImlhdCI6MTcyMDg1ODg4MCwic3ViIjoiZGV2ZWxvcGVyL2RmNjY5ZWM4LWM0OGEtOTExMi1iMDRlLWJhOGExZDZkODA0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4xMjMuNjAuMTU2Il0sInR5cGUiOiJjbGllbnQifV19.LGh6PXEG3rryk0bjjNy3Op3txXttSydSJ5QCHie5qy1TuiGINQT12mZt42jIMXRWHdpgW08_L0fUXkgzw67e0A'  # Replace 'Bearer Token' with your actual bearer token
}

def get_response(playerTag):
    # Construct the URL with the player tag
    url = f'https://api.clashofclans.com/v1/players/%23{playerTag.lstrip("#")}'
    
    # Make the GET request with headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        user_json = response.json()  # Convert response to JSON format
        return user_json
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

# # Example usage:
# player_tag = "#8CGUQQLPQ"  # Replace with the actual player tag
# user_data = get_response(player_tag)
# print(type(user_data))

# if user_data:
#     print("User data:")
#     # print(user_data)
# else:
#     print("Failed to fetch user data.")