import os, base64, numpy as np, traceback, json
from deepface import DeepFace
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

TEMP_SELFIE = "temp_selfie.jpg"
MATCH_THRESHOLD = 0.40
MODEL_NAME = "Facenet512"
cached_folder_embeddings = {}

def save_base64_image(base64_str, filename):
    with open(filename, "wb") as f:
        f.write(base64.b64decode(base64_str))

def compute_embeddings(img_path):
    try:
        return DeepFace.represent(img_path=img_path, model_name=MODEL_NAME, enforce_detection=True)
    except:
        return DeepFace.represent(img_path=img_path, model_name=MODEL_NAME, enforce_detection=False)

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def load_embeddings_from_folder(folder):
    if folder in cached_folder_embeddings:
        return cached_folder_embeddings[folder]

    folder_path = os.path.join(os.getcwd(), folder)
    embeddings = []
    if not os.path.exists(folder_path):
        return []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            faces = compute_embeddings(file_path)
            for face in faces:
                embeddings.append({
                    "embedding": face["embedding"],
                    "filename": filename
                })
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

    cached_folder_embeddings[folder] = embeddings
    return embeddings

@csrf_exempt
@require_http_methods(["POST"])
def compare_faces(request):
    try:
        data = json.loads(request.body)
        selfie_base64 = data.get("image")
        folder = data.get("folder")

        if not selfie_base64 or not folder:
            return JsonResponse({"error": "Missing 'image' or 'folder'"}, status=400)

        save_base64_image(selfie_base64, TEMP_SELFIE)
        selfie_faces = compute_embeddings(TEMP_SELFIE)
        known_faces = load_embeddings_from_folder(folder)

        all_matches = []

        for face in selfie_faces:
            face_embedding = face["embedding"]
            matched_urls = []

            for known in known_faces:
                try:
                    similarity = cosine_similarity(face_embedding, known["embedding"])
                    if similarity > (1 - MATCH_THRESHOLD):
                        matched_urls.append(f"{request.scheme}://{request.get_host()}/{folder}/{known['filename']}")
                except:
                    continue

            all_matches.append(matched_urls)

        return JsonResponse({"matches": all_matches})
    
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({"error": "Server Error"}, status=500)

def serve_known_face(request, folder, filename):
    file_path = os.path.join(os.getcwd(), folder, filename)
    return FileResponse(open(file_path, 'rb'))
