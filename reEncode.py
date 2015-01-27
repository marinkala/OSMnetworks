import re
import os.path

def convert(bucket):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets_exp/'+bucket+'_hour/'
	out_folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets_exp_reEncoded/'+bucket+'_hour/'

	for file in os.listdir(folder):
		f=open(folder+file,'r')
		of=open(out_folder+file,'w')
		for line in f:
			found=re.findall(r'\"(.+?)\"',line)
			if len(found)>0:
				repl=found[0].encode('string_escape')
				new_l=re.sub(r'\"(.+?)\"', '"'+repl+'"', line)
			else:
				new_l=line
			of.write(new_l)
		of.close()
		f.close()

#convert(8)