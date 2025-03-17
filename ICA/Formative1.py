squence=input("Give me mRNA squence, thanks :) ")
squence_list=list(squence)

def find_squence():
    coding_region=[]
    start_code=False
    start_position=-1
    for i in range(0,len(squence_list)-2):
        code=squence[i:i+3]
        if code=="AUG":
            start_position=i
            start_code=True
            break
    if start_code:
        remaining_squence=squence[start_position:]
        j=0
        while j<len(remaining_squence)-2:
            end_code=remaining_squence[j:j+3]
            if end_code in ["UAA","UAG","UGA"]:
                for v in remaining_squence[:j]:
                    coding_region.append(v)
                break
            j+=3
    return coding_region
x=find_squence()
result="".join(x)
print(result)