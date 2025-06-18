def find_the_redheads(family):
    return list(filter(lambda name: family[name] == 'red', family))

# ตัวอย่างการใช้งาน
dupont_family = {
    "florian": "red",
    "sarrie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))