import os
import sys
import uuid
import webbrowser
import threading
import time
from pathlib import Path
from typing import List

import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from PIL import Image
from rembg import remove, new_session

# 适配 PyInstaller 打包后的路径
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
    STATIC_DIR = Path(sys._MEIPASS) / "static"
else:
    BASE_DIR = Path(__file__).parent
    STATIC_DIR = BASE_DIR / "static"

UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".tif", ".gif"}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB

# 懒加载 AI 模型，等执行到 main 再初始化
_session = None

def _get_session():
    global _session
    if _session is None:
        _session = new_session("u2net")
    return _session

app = FastAPI(title="Image to Transparent PNG")


@app.get("/", response_class=HTMLResponse)
async def index():
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")


@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"Unsupported file type: {ext}")

    body = await file.read()
    if len(body) > MAX_FILE_SIZE:
        raise HTTPException(400, "File too large (max 20MB)")
    if len(body) == 0:
        raise HTTPException(400, "Empty file")

    input_path = UPLOAD_DIR / f"{uuid.uuid4()}{ext}"
    output_path = OUTPUT_DIR / f"{uuid.uuid4()}.png"

    try:
        input_path.write_bytes(body)
        img = Image.open(input_path)
        output = remove(img, session=_get_session())
        output.save(output_path, "PNG")
        return FileResponse(
            output_path,
            media_type="image/png",
            filename=Path(file.filename).stem + "_nobg.png",
            headers={"Cache-Control": "no-cache"},
        )
    except Exception as e:
        raise HTTPException(500, f"Processing failed: {str(e)}")
    finally:
        if input_path.exists():
            input_path.unlink()


@app.post("/convert-to-ico")
async def convert_to_ico(
    file: UploadFile = File(...),
    sizes: str = Form("32"),
):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"Unsupported file type: {ext}")

    body = await file.read()
    if len(body) > MAX_FILE_SIZE:
        raise HTTPException(400, "File too large (max 20MB)")
    if len(body) == 0:
        raise HTTPException(400, "Empty file")

    # Parse sizes, e.g. "16,32,48" → [16, 32, 48]
    try:
        size_list = sorted(
            {int(s.strip()) for s in sizes.split(",") if s.strip()}
        )
    except ValueError:
        raise HTTPException(400, "Invalid sizes format")

    # Clamp & validate
    size_list = [s for s in size_list if 1 <= s <= 512]
    if not size_list:
        size_list = [32]

    input_path = UPLOAD_DIR / f"{uuid.uuid4()}{ext}"
    output_path = OUTPUT_DIR / f"{uuid.uuid4()}.ico"

    try:
        input_path.write_bytes(body)
        img = Image.open(input_path)
        # Remove background
        rgba = remove(img, session=_get_session())
        # Save as multi-size ICO
        rgba.save(output_path, format="ICO", sizes=[(s, s) for s in size_list])
        return FileResponse(
            output_path,
            media_type="image/x-icon",
            filename=Path(file.filename).stem + ".ico",
            headers={"Cache-Control": "no-cache"},
        )
    except Exception as e:
        raise HTTPException(500, f"ICO conversion failed: {str(e)}")
    finally:
        if input_path.exists():
            input_path.unlink()


def _open_browser():
    time.sleep(1.5)
    webbrowser.open("http://localhost:8000")

def _print(msg: str):
    """立即输出到控制台，确保用户能看到"""
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    _print(">> 正在加载 AI 模型（首次约 176MB，后续秒级）...")
    _get_session()  # 在这里才真正加载模型，用户能看到进度
    _print(">> AI 模型加载完成！")
    _print(">> 正在启动 Web 服务器...")
    threading.Thread(target=_open_browser, daemon=True).start()
    _print("")
    _print(">> 浏览器已自动打开 http://localhost:8000")
    _print("   如果没有弹出，请手动访问该地址")
    _print("   关闭此窗口即可停止服务")
    _print("")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
