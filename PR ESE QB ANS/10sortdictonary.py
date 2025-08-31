#10.	Write a Python script to sort (ascending and descending) a dictionary by value.
d1={1:14,2:63,3:9}
srt_asc=sorted(d1.values())
srt_desc=sorted(d1.values(),reverse=True)
print(srt_asc)
print(srt_desc)