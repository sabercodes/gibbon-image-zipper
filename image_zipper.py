import os
import zipfile
from PIL import Image
import io

def validate_and_prepare_zip(input_folder, output_zip):
    # Ensure the input folder exists
    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return
    
    # Create a new ZIP file
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    # Ensure the filename follows the format "username.extension"
                    if '.' in filename:
                        name, ext = filename.split('.', 1)
                        if ext.lower() not in ['jpg', 'jpeg', 'png']:
                            print(f"Invalid format for {filename}. Skipping.")
                            continue

                        image_path = os.path.join(input_folder, filename)
                        with Image.open(image_path) as img:
                            width, height = img.size
                            aspect_ratio = width / height

                            # Check size range and aspect ratio
                            if width > 360 or height > 480 or not (1/1.4 <= aspect_ratio <= 1/1.2):
                                print(f"Resizing {filename} to fit required size and aspect ratio.")
                                img = img.resize((240, 320), Image.BILINEAR)
                            
                            # Save the validated and resized image to a bytes buffer
                            img_buffer = io.BytesIO()
                            img_format = img.format if img.format else 'JPEG'  # Default to JPEG if format is None
                            img.save(img_buffer, format=img_format)
                            img_buffer.seek(0)

                            # Add the image to the ZIP file from the bytes buffer
                            zipf.writestr(filename, img_buffer.read())
                            print(f"Added {filename} to ZIP file.")
                except OSError as e:
                    print(f"Error processing {filename}: {e}")
                except Exception as e:
                    print(f"Unexpected error processing {filename}: {e}")

    print(f"ZIP file created: {output_zip}")

# Usage
input_folder = os.path.join(os.path.dirname(__file__), 'photos')
output_zip = os.path.join(os.path.dirname(__file__), 'output.zip')
validate_and_prepare_zip(input_folder, output_zip)
