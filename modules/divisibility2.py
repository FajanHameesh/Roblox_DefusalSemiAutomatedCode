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
div2_region = [div2_region[i:i+2] for i in range(0, len(div2_region), 2)]

div3_region = '0405060910111213'
div3_region = [div3_region[i:i+2] for i in range(0, len(div3_region), 2)]

div5_region = '0607081112131415'
div5_region = [div5_region[i:i+2] for i in range(0, len(div5_region), 2)]

div7_region = '0203050607081011'
div7_region = [div7_region[i:i+2] for i in range(0, len(div7_region), 2)]


# ==========================================
# Build signature -> result mapping
# ==========================================

signature_result = {}

for region, value in venn_dict.items():

    signature = (
        region in div2_region,
        region in div3_region,
        region in div5_region,
        region in div7_region
    )

    signature_result[signature] = value


# ==========================================
# Main classifier
# ==========================================

def divisibility(code):

    code = int(code)

    signature = (
        code % 2 == 0,
        code % 3 == 0,
        code % 5 == 0,
        code % 7 == 0
    )

    return signature_result.get(signature)