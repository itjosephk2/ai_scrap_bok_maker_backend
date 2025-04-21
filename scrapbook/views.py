from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser  # ✅ Required for file upload
from .serializers import ScrapImageSerializer
from .models import ScrapImage


class ScrapbookView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # ✅ Enable form/file upload in DRF

    def post(self, request):
        serializer = ScrapImageSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            # TODO: Process the image with selected aesthetic
            # TODO: Generate a caption based on aesthetic

            # Simulate transformation
            instance.caption = f"A {instance.aesthetic} moment captured forever."
            instance.edited_image = instance.original_image  # Just return the original for now
            instance.save()

            return Response(ScrapImageSerializer(instance).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
