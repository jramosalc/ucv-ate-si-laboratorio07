import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def process_image(input_path: str, output_path: str, rotation_angle: int, filter_name: str, watermark_text: str) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Falta la imagen original en: {input_path}")
        
    image = Image.open(input_path).convert("RGB")
    processed_image = image.rotate(rotation_angle, expand=True)
    
    filters_map = {
        "EMBOSS": ImageFilter.EMBOSS,
        "FIND_EDGES": ImageFilter.FIND_EDGES,
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR
    }
    
    selected_filter = filters_map.get(filter_name.upper())
    if selected_filter:
        processed_image = processed_image.filter(selected_filter)
        
    draw = ImageDraw.Draw(processed_image)
    try:
        font = ImageFont.load_default()
    except IOError:
        font = None
        
    draw.text((30, 30), watermark_text, fill=(255, 255, 255), font=font)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    processed_image.save(output_path)
    return output_path