from pathlib import Path
import automation

#absolute
#c:\program files\microsoft
# user\local\bin
#relative

path = Path()
for file in path.glob('*.xlsx'):
    automation.update_xlsheet(file)
    print(file)