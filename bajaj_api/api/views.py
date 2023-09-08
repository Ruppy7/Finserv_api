from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BFHLView(APIView):
    def post(self, request):
        data = request.data.get('data')
        user_id = 'rupesh_sri_sai_chand_kancharlapalli_12052003'
        email = 'ks7171@srmist.edu.in'
        roll_number = 'RA2011030010108'
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = max(alphabets, default=None)
        
        response_data = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        
        return Response(response_data, status=status.HTTP_200_OK)

    def get(self, request):
        response_data = {'operation_code': 1}
        return Response(response_data, status=status.HTTP_200_OK)
