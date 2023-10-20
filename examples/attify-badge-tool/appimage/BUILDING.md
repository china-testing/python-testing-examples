### AppImage building instructions

On a Ubuntu 22.04 container run,

```
# apt update && apt install python3-pip --yes
# ./appimage-builder-1.1.0-x86_64.AppImage --recipe attify-badge-tool.yml
```

appimage-builder can be downloaded from https://github.com/AppImageCrafters/appimage-builder


Reference: https://appimage-builder.readthedocs.io/en/latest/examples/pyqt.html