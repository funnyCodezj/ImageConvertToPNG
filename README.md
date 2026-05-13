# ImageConvertToPNG

[中文](#中文) | [English](#english)

![Python](https://img.shields.io/badge/Python-3.10-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

> 在线图片背景去除工具，支持转换为透明 PNG 和多尺寸 ICO 图标。
>
> An online background removal tool that converts images to transparent PNG and multi-size ICO icons.

---

## 中文

一键去除图片背景，生成透明 PNG，并支持转换为 Windows ICO 图标（可自定义多尺寸）。

### 功能特性

- **AI 去除背景**：基于深度学习模型（U²-Net），自动识别主体并去除背景
- **透明 PNG 输出**：生成 RGBA 模式的 PNG 图片，保留透明度通道
- **ICO 图标转换**：将透明 PNG 转换为 Windows ICO 图标格式
- **多尺寸选择**：支持 16×16 到 256×256 共 8 种尺寸，可多选
- **尺寸预设**：提供「仅 32×32」「常用」「高清」「全尺寸」快捷选项
- **拖拽上传**：支持拖拽和点击选择文件
- **实时预览**：原图和结果对比显示
- **单文件 EXE**：使用 PyInstaller 打包为文件夹版本，启动无需解压

### 技术栈

| 组件 | 技术 |
|------|------|
| 后端框架 | FastAPI + Uvicorn |
| 背景去除 | rembg (U²-Net 模型) |
| 图像处理 | Pillow (PIL) |
| 前端 | 原生 HTML/CSS/JS |
| 打包 | PyInstaller (onedir) |

### 快速开始

#### 源码运行

```bash
# 安装依赖
pip install "rembg==2.0.50" "numpy<2" fastapi uvicorn python-multipart pillow

# 运行
python main.py
```

打开浏览器访问 http://localhost:8000

#### EXE 运行

运行 `build.bat` 打包，或直接使用 `dist/ImageConvertToPNG/ImageConvertToPNG.exe`。

首次运行会自动下载 AI 模型（约 176MB）。

### 使用流程

1. 拖拽或选择图片（JPG / PNG / WebP / BMP / TIFF / GIF，≤20MB）
2. 点击「去除背景」，等待 AI 处理
3. 下载透明 PNG，或选择尺寸生成 ICO 图标
4. 点击「下载 ICO」保存图标文件

### 项目结构

```
ImageConvertToPNG/
├── main.py                  # FastAPI 后端（包含 API 路由和模型加载）
├── static/index.html        # Web 前端界面
├── ImageConvertToPNG.spec   # PyInstaller 打包配置
├── build.bat                # 一键打包脚本
└── dist/ImageConvertToPNG/  # 打包后的可执行程序
```

---

## English

Remove image backgrounds with one click, generate transparent PNGs, and convert to Windows ICO icons with multiple size options.

### Features

- **AI Background Removal**: Deep learning model (U²-Net) automatically detects and removes backgrounds
- **Transparent PNG Output**: Generates RGBA PNG images with alpha channel preserved
- **ICO Icon Conversion**: Converts transparent PNGs to Windows ICO format
- **Multi-size Selection**: Supports 8 sizes from 16×16 to 256×256, multi-select enabled
- **Size Presets**: Quick options for "32×32 only", "Common", "HD", and "Full size"
- **Drag & Drop Upload**: Supports drag-and-drop and file picker
- **Live Preview**: Side-by-side comparison of original and result
- **Portable EXE**: Packaged with PyInstaller as onedir - no installation required

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI + Uvicorn |
| Background Removal | rembg (U²-Net model) |
| Image Processing | Pillow (PIL) |
| Frontend | Vanilla HTML/CSS/JS |
| Packaging | PyInstaller (onedir) |

### Quick Start

#### Run from Source

```bash
# Install dependencies
pip install "rembg==2.0.50" "numpy<2" fastapi uvicorn python-multipart pillow

# Start server
python main.py
```

Open http://localhost:8000 in your browser.

#### Run as EXE

Run `build.bat` to package, or use `dist/ImageConvertToPNG/ImageConvertToPNG.exe` directly.

The AI model (~176MB) will be downloaded automatically on first launch.

### Workflow

1. Drag & drop or select an image (JPG / PNG / WebP / BMP / TIFF / GIF, ≤20MB)
2. Click "去除背景" (Remove Background) and wait for AI processing
3. Download the transparent PNG, or select sizes and generate an ICO icon
4. Click "下载 ICO" (Download ICO) to save the icon file

### Project Structure

```
ImageConvertToPNG/
├── main.py                  # FastAPI backend (API routes & model loading)
├── static/index.html        # Web frontend
├── ImageConvertToPNG.spec   # PyInstaller build config
├── build.bat                # One-click build script
└── dist/ImageConvertToPNG/  # Packaged executable
```

---

## License

MIT
