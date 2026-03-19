import os
from PIL import Image

input_folder = "wallpapers"
output_folder = "wallpapers_bw"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            img = Image.open(input_path)

            # Convert to grayscale
            gray = img.convert("L")

            # Convert to pure black & white (monochrome)
            bw = gray.point(lambda x: 0 if x < 128 else 255, '1')

            bw.save(output_path)

            print(f"[✓] Converted: {filename}")

        except Exception as e:
            print(f"[!] Skipped {filename}: {e}")

print("\nDone! Check 'wallpapers_bw' folder.")
