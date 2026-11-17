[app]

title = MERVY ANTIVIRUS
package.name = mervyantivirus
package.domain = org.mervy
source.dir = .
source.include_exts = py,txt,png,jpg
version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 35
android.minapi = 23

[buildozer]

log_level = 2
warn_on_root = 1
