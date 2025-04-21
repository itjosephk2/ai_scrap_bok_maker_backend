import os
import traceback
from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScrapImageSerializer
from .models import ScrapImage
from rest_framework.parsers import MultiPartParser, FormParser


# Initialize OpenAI client for v1.x interface
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_caption(aesthetic):
    prompt = f"Write a short, creative scrapbook caption in a {aesthetic} aesthetic."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a scrapbook caption writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        max_tokens=60,
    )

    # Access the returned text in the v1.x structure
    return response.choices[0].message.content.strip()


class ScrapbookView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # ensure file uploads work

    def post(self, request):
        try:
            print("Request data:", request.data)
            print("Request FILES:", request.FILES)

            serializer = ScrapImageSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()

                # Generate caption using OpenAI v1.x client
                instance.caption = generate_caption(instance.aesthetic)

                # For now, simulate the image transformation by using the original
                instance.edited_image = instance.original_image
                instance.save()

                return Response(ScrapImageSerializer(instance).data,
                                status=status.HTTP_201_CREATED)

            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Exception occurred:", str(e))
            traceback.print_exc()
            return Response({"error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
