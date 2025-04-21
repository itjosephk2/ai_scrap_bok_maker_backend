import os
import openai
import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ScrapImageSerializer
from .models import ScrapImage


def generate_caption(aesthetic):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"Write a short, creative scrapbook caption in a {aesthetic} aesthetic."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a scrapbook caption writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        max_tokens=60,
    )

    return response.choices[0].message["content"].strip()


class ScrapbookView(APIView):
    def post(self, request):
        try:
            print("Request data:", request.data)
            print("Request FILES:", request.FILES)

            serializer = ScrapImageSerializer(data=request.data, files=request.FILES)
            if serializer.is_valid():
                instance = serializer.save()

                # Generate AI caption
                instance.caption = generate_caption(instance.aesthetic)
                instance.edited_image = instance.original_image
                instance.save()

                return Response(ScrapImageSerializer(instance).data, status=status.HTTP_201_CREATED)

            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Exception occurred:", str(e))
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
