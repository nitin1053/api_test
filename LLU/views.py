import csv
from io import TextIOWrapper
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
import requests
from django.http import Http404
from rest_framework import status

class Hello(APIView):
    def get(self, request):
        # Define the response data
        data = {'message': 'Hello'}

        # Return a JSON response with the message
        return Response(data)
    
class TrainingClass(APIView):
    def get(self, request, **kwargs):
        train=kwargs.get('train')
        result_source=[]
        
        if train=="paragraph":
            
            return result_source            
        if train=="QnA":
            return result_source
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
import json
from io import TextIOWrapper

class csvreader(APIView):
    def post(self, request):
        # Check if a file was uploaded
        if 'file' not in request.data:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the uploaded CSV file
        uploaded_file = request.data['file']

        # Check if the uploaded file is a CSV file
        if not uploaded_file.name.endswith('.csv'):
            return Response({'error': 'Uploaded file is not a CSV file'}, status=status.HTTP_400_BAD_REQUEST)

        # Read and process the CSV file
        try:
            csv_data = []
            csv_reader = csv.DictReader(TextIOWrapper(uploaded_file.file, encoding='utf-8'))
            for row in csv_reader:
                # Format the response as required
                response_entry = {
                    'text': f"### Human: {row['Questions']} \n### Assistant: {row['Answers']}"
                }
                csv_data.append(response_entry)
        except Exception as e:
            return Response({'error': 'Error reading CSV file'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return the CSV data as JSON
        return Response(csv_data, status=status.HTTP_200_OK)

        
        
        
        
        
    