from django.http import JsonResponse
from .mongo import students_collection


def students(request):
    data = []

    for student in students_collection.find():
        data.append({
            "id": str(student["_id"]),
            "name": student.get("name"),
            "age": student.get("age"),
            "department": student.get("department"),
            "specialization": student.get("specialization")
        })

    return JsonResponse(data, safe=False)