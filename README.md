# 🖤 Wallpaper Monochrome Converter

A simple Python script to convert a folder of wallpapers into **pure black & white (monochrome)** images.

Perfect for:

* Minimalist setups
* Terminal / tiling WM aesthetics
* Reducing visual noise in wallpapers

---

## 📸 Features

* Batch convert all images in a folder
* Supports: `.jpg`, `.jpeg`, `.png`, `.webp`
* Outputs **true monochrome (1-bit)** images
* Keeps original filenames.
* Skips invalid/corrupted files safely

---

## 📂 Project Structure

```
.
├── v.py
├── wallpapers/
└── wallpapers_bw/
```

* `wallpapers/` → input images
* `wallpapers_bw/` → converted output

---

## ⚙️ Requirements

* Python 3.10+
* Pillow library

---

## 🔧 Installation

### Option 1: Virtual Environment (Recommended)

```bash
python3 -m venv imgenv
source imgenv/bin/activate
pip install pillow
```

### Option 2: System Package (Kali/Debian)

```bash
sudo apt install python3-pil
```

---

## ▶️ Usage

1. Place your images inside:

```
wallpapers/
```

2. Run the script:

```bash
python v.py
```

3. Get results in:

```
wallpapers_bw/
```

---

## 🧠 How It Works

1. Converts image → grayscale
2. Applies threshold → black or white
3. Saves as **1-bit monochrome image**

---

## 🎛️ Customization

### Change threshold (default = 128)

Inside `v.py`:

```python
bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
```

* Lower value → more white
* Higher value → more black

---

### Better quality (dithering)

Replace with:

```python
bw = gray.convert("1")
```

👉 Produces smoother, more visually pleasing results for wallpapers.

---

## ⚡ Alternative (Faster CLI Method)

Using ImageMagick:

```bash
sudo apt install imagemagick
mkdir wallpapers_bw
mogrify -path wallpapers_bw -colorspace Gray -threshold 50% *.jpg *.png
```

---

## ⚠️ Notes

* Original images are not modified
* Output images are strictly black & white (no grayscale)
* Large batches (100+ images) are supported

---

## 🚀 Future Improvements

* Recursive folder support
* Adaptive threshold (Otsu method)
* GUI version
* Drag-and-drop support

---

## 📄 License

MIT License (or choose your preferred license)

---

## 🙌 Author

Created for quick wallpaper processing on Linux (Kali, Arch, etc.)
