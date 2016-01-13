for i in xrange(len(df)):
    h=df.start_obj[i].hour
    hours.append(h)
    if df.span[i]>pd.Timedelta('1 hour'):
        while h<df.end_obj[i].hour:
        	h+=1
        	hours.append(h)