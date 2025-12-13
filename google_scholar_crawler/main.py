from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

# 计算论文总数
total_publications = len(author['publications'])

print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

# 为shields.io创建多个数据源
shieldio_citations = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_citations, outfile, ensure_ascii=False)

# 添加论文数量统计
shieldio_publications = {
  "schemaVersion": 1,
  "label": "publications",
  "message": f"{total_publications}",
}
with open(f'results/gs_data_publications.json', 'w') as outfile:
    json.dump(shieldio_publications, outfile, ensure_ascii=False)

# 添加h-index统计
shieldio_hindex = {
  "schemaVersion": 1,
  "label": "h-index",
  "message": f"{author.get('hindex', 'N/A')}",
}
with open(f'results/gs_data_hindex.json', 'w') as outfile:
    json.dump(shieldio_hindex, outfile, ensure_ascii=False)

print(f"✓ Total publications: {total_publications}")
print(f"✓ Citations: {author['citedby']}")
print(f"✓ H-index: {author.get('hindex', 'N/A')}")
