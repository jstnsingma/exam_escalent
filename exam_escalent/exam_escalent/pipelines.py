# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class ExamEscalentPipeline:   
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        logo = adapter.get('logo')
        if logo:
            adapter['logo'] = re.sub(r'<img src="(.*?)">', r'\1', logo)

        number = adapter.get('number')
        if number:
            adapter['number'] = re.sub(r'(#\d+) \| .*', r'\1', number)

        position = adapter.get('position')
        if position:
            adapter['position'] = re.sub(r'#\d+ \| (.*)', r'\1', position)

        return item
