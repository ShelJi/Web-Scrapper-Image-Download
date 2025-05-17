from typing import List


urls = ['https://plus.unsplash.com/premium_photo-1676478746990-4ef5c8ef234a?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1523224042829-4731dd15a3bb?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1560790671-b76ca4de55ef?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://plus.unsplash.com/premium_photo-1676068243733-df1880c2aef8?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1474112704314-8162b7749a90?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1527061011665-3652c757a4d4?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://plus.unsplash.com/premium_photo-1683121484963-a491b935780b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1520763185298-1b434c919102?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://plus.unsplash.com/premium_photo-1676475964992-6404b8db0b53?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1487139975590-b4f1dce9b035?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1470509037663-253afd7f0f51?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/32/RgJQ82pETlKd0B7QzcJO_5912578701_92397ba76c_b.jpg?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1490750967868-88aa4486c946?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1471899236350-e3016bf1e69e?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1516205651411-aef33a44f7c2?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1538998073820-4dfa76300194?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Zmxvd2VyfGVufDB8fDB8fHww', 'https://images.unsplash.com/photo-1546842931-886c185b4c8c?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1447875569765-2b3db822bec9?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D', 'https://plus.unsplash.com/premium_photo-1677094766116-aa0f8742d36b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGZsb3dlcnxlbnwwfHwwfHx8MA%3D%3D']
# urls = ['https://plus.unsplash.com/premium_photo-1676478746990-4ef5c8ef234a?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Zmxvd2VyfGVufDB8fDB8fHww']

urls = ['https://plus.unsplash.com/premium_photo-1676478746990-4ef5c8ef234a?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1490750967868-88aa4486c946?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1460039230329-eb070fc6c77c?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1508808703020-ef18109db02f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1720475982311-94a0dac1f32f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1476994230281-1448088947db?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1582794543139-8ac9cb0f7b11?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1486944859394-ed1c44255713?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1613539246066-78db6ec4ff0f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1454262041357-5d96f50a2f27?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://plus.unsplash.com/premium_photo-1674986175088-2d7dda41f7f8?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://plus.unsplash.com/premium_photo-1677178628425-84a64dc416b6?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1526047932273-341f2a7631f9?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://plus.unsplash.com/premium_vector-1712614779372-248dd015213b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0', 'https://plus.unsplash.com/premium_vector-1689096811839-56e58bd0c120?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0', 'https://plus.unsplash.com/premium_vector-1712168936685-a4ae412d31d9?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0', 'https://plus.unsplash.com/premium_vector-1710933932766-5d0440efcd4f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0', 'https://images.unsplash.com/photo-1541275055241-329bbdf9a191?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://plus.unsplash.com/premium_photo-1676068243733-df1880c2aef8?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://plus.unsplash.com/premium_photo-1676475964992-6404b8db0b53?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Zmxvd2Vyc3xlbnwwfHwwfHx8MA%3D%3D', 'https://images.unsplash.com/photo-1591350832024-68c7491dd46e?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1496661415325-ef852f9e8e7c?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1602615576820-ea14cf3e476a?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D', 'https://images.unsplash.com/photo-1600647993560-11a92e039466?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGZsb3dlcnN8ZW58MHx8MHx8fDA%3D']

def extract_img_id(urls: List[str]) -> List[str]:
    """Extract image id from url."""
    extracted = []
    for i in urls:
        extracted.append(i.split("?")[0].split("unsplash.com/")[1])
    return extracted


data = extract_img_id(urls)
for i in data:
    print(i)
    
# op
"""
premium_photo-1676478746990-4ef5c8ef234a
photo-1523224042829-4731dd15a3bb
photo-1560790671-b76ca4de55ef
premium_photo-1676068243733-df1880c2aef8
photo-1474112704314-8162b7749a90
photo-1527061011665-3652c757a4d4
photo-1525310072745-f49212b5ac6d
premium_photo-1683121484963-a491b935780b
photo-1520763185298-1b434c919102
premium_photo-1676475964992-6404b8db0b53
photo-1487139975590-b4f1dce9b035
photo-1470509037663-253afd7f0f51
32/RgJQ82pETlKd0B7QzcJO_5912578701_92397ba76c_b.jpg
photo-1490750967868-88aa4486c946
photo-1471899236350-e3016bf1e69e
photo-1516205651411-aef33a44f7c2
photo-1538998073820-4dfa76300194
photo-1546842931-886c185b4c8c
photo-1447875569765-2b3db822bec9
premium_photo-1677094766116-aa0f8742d36b
"""

"""
premium_photo-1676478746990-4ef5c8ef234a
photo-1490750967868-88aa4486c946
photo-1460039230329-eb070fc6c77c
photo-1508808703020-ef18109db02f
photo-1720475982311-94a0dac1f32f
photo-1476994230281-1448088947db
photo-1582794543139-8ac9cb0f7b11
photo-1486944859394-ed1c44255713
photo-1613539246066-78db6ec4ff0f
photo-1454262041357-5d96f50a2f27
premium_photo-1674986175088-2d7dda41f7f8 
premium_photo-1677178628425-84a64dc416b6 
photo-1526047932273-341f2a7631f9

premium_vector-1712614779372-248dd015213b
premium_vector-1689096811839-56e58bd0c120
premium_vector-1712168936685-a4ae412d31d9
premium_vector-1710933932766-5d0440efcd4f

photo-1541275055241-329bbdf9a191
premium_photo-1676068243733-df1880c2aef8
premium_photo-1676475964992-6404b8db0b53
photo-1591350832024-68c7491dd46e
photo-1496661415325-ef852f9e8e7c
photo-1602615576820-ea14cf3e476a
photo-1600647993560-11a92e039466
"""