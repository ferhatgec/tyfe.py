import tyfe
from pathlib import Path

init = tyfe.Tyfe()
data = str(input())

print({
          tyfe.Tyfes.FPaper: 'FPaper',
          tyfe.Tyfes.Jpeg: 'JPEG',
          tyfe.Tyfes.FlaScript: 'FlaScript',
          tyfe.Tyfes.Bash: 'BASH',
          tyfe.Tyfes.Sh: 'SH',
          tyfe.Tyfes.Png: 'PNG',
          tyfe.Tyfes.Gif: 'GIF',
          tyfe.Tyfes.Python: 'Python',
          tyfe.Tyfes.Bmp: 'BMP',
          tyfe.Tyfes.Webp: 'WEBP',
          tyfe.Tyfes.Pdf: 'PDF',
          tyfe.Tyfes.Ico: 'ICO'
      }.get(init.check(data.lower()), Path(data).suffix.upper()[:1]))
