def divisibility(code):
    code = int(code)
    div2 = code % 2 == 0
    div3 = code % 3 == 0 
    div5 = code % 5 == 0
    div7 = code % 7 == 0

    venn_dict = {
        '01':'A',
        '02':'E',
        '03':'C',
        '04':'B',
        '05':'C',
        '06':'D',
        '07':'A',
        '08':'E',
        '09':'F',
        '10':'B',
        '11':'A',
        '12':'B',
        '13':'C',
        '14':'E',
        '15':'F'
    }

    div2_region = '0102040506071314'
    div2_region = [div2_region[i:i+2] for i in range(0,len(div2_region),2)]
    div3_region = '0405060910111213'
    div3_region = [div3_region[i:i+2] for i in range(0,len(div3_region),2)]
    div5_region = '0607081112131415'
    div5_region = [div5_region[i:i+2] for i in range(0,len(div5_region),2)]
    div7_region = '0203050607081011'
    div7_region = [div7_region[i:i+2] for i in range(0,len(div7_region),2)]
    
    region_checklist = []

    if div2:
        region_checklist.append(div2_region)
    if div3:
        region_checklist.append(div3_region)
    if div5:
        region_checklist.append(div5_region)
    if div7:
        region_checklist.append(div7_region)

    if len(region_checklist) == 0:
        return 'F'

    for i in region_checklist[0]:
        for j in [region_checklist.pop(0)]:
            check = i in j
        if check:
            result = i
            break
    
    return venn_dict[result]