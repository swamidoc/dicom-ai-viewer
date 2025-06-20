[app]
title = DICOM AI Viewer
package.name = dicomai
package.domain = org.example
source.dir = .
source.include_exts = py,kv,tflite
version = 0.1
requirements = python3,kivy,kivymd,pillow,pydicom,numpy,opencv-python
orientation = portrait
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
