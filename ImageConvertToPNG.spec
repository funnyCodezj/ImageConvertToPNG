# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = [('static', 'static')]
datas += collect_data_files('pymatting')
datas += collect_data_files('rembg')
datas += collect_data_files('onnxruntime')
datas += collect_data_files('scikit_image')
datas += copy_metadata('pymatting')
datas += copy_metadata('rembg')
datas += copy_metadata('onnxruntime')
# 内置 AI 模型，避免首次下载
datas += [('C:/Users/lzj/.u2net/u2net.onnx', '.u2net')]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['uvicorn.logging', 'uvicorn.loops.auto', 'uvicorn.protocols.http.auto', 'uvicorn.protocols.websockets.auto', 'uvicorn.lifespan.on', 'uvicorn.lifespan.off', 'pydantic', 'pydantic.color', 'pydantic.types', 'starlette', 'multipart', 'python_multipart', 'onnxruntime', 'skimage', 'skimage.transform', 'skimage.measure', 'pymatting', 'pymatting.util.kdtree', 'cv2', 'numba', 'llvmlite'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['torch', 'torchvision', 'tensorflow', 'pandas', 'matplotlib', 'lxml', 'sqlalchemy', 'django'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ImageConvertToPNG',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ImageConvertToPNG',
)
