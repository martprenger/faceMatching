import face_recognition
import os

# Step 3: Face Detection
def detect_faces(photo_path):
    image = face_recognition.load_image_file(photo_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

# Step 4: Face Encoding
def encode_faces(photo_path):
    image = face_recognition.load_image_file(photo_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

# Step 6: Matching Faces
def match_faces(encoding_to_match, known_encodings, threshold=0.6):
    matches = face_recognition.compare_faces(known_encodings, encoding_to_match, tolerance=threshold)
    return matches

# Step 7: Generate Links
def generate_links(match_results, photo_paths):
    matching_links = [photo_paths[i] for i, match in enumerate(match_results) if match]
    return matching_links

# Example Usage
photo_folder = "path/to/your/photos"
all_photo_paths = [os.path.join(photo_folder, photo) for photo in os.listdir(photo_folder)]

# Assuming you have a reference encoding to match against
reference_encoding = encode_faces("path/to/reference/photo.jpg")

# Iterating through all photos
for photo_path in all_photo_paths:
    # Step 3: Detect Faces
    face_locations = detect_faces(photo_path)
    
    # Step 4: Encode Faces
    face_encodings = encode_faces(photo_path)
    
    # Step 6: Matching Faces
    match_results = match_faces(reference_encoding, face_encodings)
    
    # Step 7: Generate Links
    matching_links = generate_links(match_results, [photo_path])
    
    print(f"Matching faces in {photo_path}: {matching_links}")

