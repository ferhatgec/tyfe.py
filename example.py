import tyfe

init = tyfe.Tyfe()
data = str(input())

print({
          tyfe.Tyfes.Jpeg: 'JPEG',
          tyfe.Tyfes.FlaScript: 'FlaScript',
          tyfe.Tyfes.Bash: 'BASH',
          tyfe.Tyfes.Sh: 'SH',
          tyfe.Tyfes.Png: 'PNG',
          tyfe.Tyfes.Gif: 'GIF',
          tyfe.Tyfes.Python: 'Python',
          tyfe.Tyfes.Bmp: 'BMP',
          tyfe.Tyfes.Webp: 'WEBP'
      }.get(init.check(data), ''))
