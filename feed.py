import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_ele = xml_tree.Element('rss', {'version': '2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})
    
channel_ele = xml_tree.SubElement(rss_ele, 'channel')
link_prefix = yaml_data['link']

xml_tree.SubElement(channel_ele, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_ele, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_ele, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_ele, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_ele, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_ele, 'itunes:image', {
    'href': link_prefix + yaml_data['image']
})
xml_tree.SubElement(channel_ele, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_ele, 'link').text = link_prefix
xml_tree.SubElement(channel_ele, 'itunes:category', {
    'text': yaml_data['category']
})

for item in yaml_data['item']:
    item_ele = xml_tree.SubElement(channel_ele, 'item')
    xml_tree.SubElement(item_ele, 'title').text = item['title']
    xml_tree.SubElement(item_ele, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(item_ele, 'description').text = item['description']
    xml_tree.SubElement(item_ele, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_ele, 'pubDate').text = item['published']

    enclosure = xml_tree.SubElement(item_ele, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })

output_tree = xml_tree.ElementTree(rss_ele)
output_tree.write('sample.xml', encoding="UTF-8", xml_declaration=True)    

    