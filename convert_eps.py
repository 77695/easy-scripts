import os
for rt, dirs, files in os.walk('./'):
  for f in files:
    fn=os.path.join(rt,f)
    if fn.find('.pdf')!=-1:
      cmd='pdftops -f 1 -l 1 -eps "'+fn+'" '
      print cmd
      os.system(cmd)
