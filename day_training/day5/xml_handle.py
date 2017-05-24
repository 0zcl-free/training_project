import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")
root = tree.getroot()
print(root.tag)
print(root)
#data
#<Element 'data' at 0x0000000002F61228>


# 遍历xml文档
for child in root:
    #<country    name="Liechtenstein">
    print(child.tag, child.attrib)  #标签名及属性
    for i in child:
        # <rank updated="yes">2</rank>
        print(i.tag, i.text)

# country {'name': 'Liechtenstein'}
# rank 2
# year 2008
# gdppc 141100
# neighbor None
# neighbor None




# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

# year 2008
# year 2011
# year 2011