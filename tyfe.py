# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# tyfe[dot]py - Python3 implementation of Tyfe
#
# github.com/ferhatgec/tyfe.py
# github.com/ferhatgec/tyfe

from enum import IntEnum

class Tyfes(IntEnum):
    Nothing = -1
    Jpeg = 0
    Png = 1
    Gif = 2
    FlaScript = 3
    Bash = 4
    Sh = 5
    Python = 6
    Bmp = 7
    Webp = 8


class Tyfe:
    def __init__(self):
        self.extension: str = ''
        self.filename: str = ''

        self.binary_ext = [
            '.jpg',
            '.jpeg',
            '.png',
            '.gif',
            '.bmp',
            '.webp'
        ]

    class Markers(IntEnum):
        Jpeg_Soi = 0xD8
        Jpeg_Start = 0xFF

        Png_Soi = 0x89
        Png_Start_2 = 0x50
        Png_Start_3 = 0x4E
        Png_Start_4 = 0x47

        Gif_Soi = 0x47
        Gif_Start_2 = 0x49
        Gif_Start_3 = 0x46

        Bmp_Soi = 0x42
        Bmp_Start_2 = 0x4D

        Webp_Soi = 0x57
        Webp_Start_2 = 0x45
        Webp_Start_3 = 0x42
        Webp_Start_4 = 0x50

    def ext(self, ext2: str, ext3: str) -> bool:
        return (self.extension == ext2) or (self.extension == ext3)

    def check(self, file: str) -> Tyfes:
        from pathlib import Path

        self.filename = file
        self.extension = Path(self.filename).suffix

        found = False

        for ext in self.binary_ext:
            if self.extension == ext:
                self.found = True

        if self.found:
            return self.what_is_this()
        else:
            return self.is_shebang()

    def what_is_this(self) -> Tyfes:
        marker = []
        with open(self.filename, 'rb') as file:
            while byte := file.read(1):
                marker += byte

        if marker[0] == self.Markers.Jpeg_Start and \
            marker[1] == self.Markers.Jpeg_Soi and \
            marker[2] == self.Markers.Jpeg_Start:
            return Tyfes.Jpeg

        if marker[0] == self.Markers.Png_Soi and \
            marker[1] == self.Markers.Png_Start_2 and \
            marker[2] == self.Markers.Png_Start_3 and \
            marker[3] == self.Markers.Png_Start_4:
            return Tyfes.Png

        if marker[0] == self.Markers.Gif_Soi and \
            marker[1] == self.Markers.Gif_Start_2 and \
            marker[2] == self.Markers.Gif_Start_3:
            return Tyfes.Gif

        if marker[0] == self.Markers.Bmp_Soi and \
            marker[1] == self.Markers.Bmp_Start_2:
            return Tyfes.Bmp

        if marker[8] == self.Markers.Webp_Soi and \
            marker[9] == self.Markers.Webp_Start_2 and \
            marker[10] == self.Markers.Webp_Start_3 and \
            marker[11] == self.Markers.Webp_Start_4:
            return Tyfes.Webp

        return Tyfes.Nothing

    def is_shebang(self) -> Tyfes:
        with open(self.filename, 'r') as file:
            for line in file:
                if line[0] == '#' and line[1] == '!':
                    if 'bash' in line:
                        return Tyfes.Bash
                    elif 'fla' in line:
                        return Tyfes.FlaScript
                    elif 'sh' in line:
                        return Tyfes.Sh
                    elif 'python' in line:
                        return Tyfes.Python