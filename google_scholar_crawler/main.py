from datetime import datetime, timezone
import json
import os

from scholarly import scholarly


def write_json(path, payload):
    with open(path, 'w', encoding='utf-8') as outfile:
        json.dump(payload, outfile, ensure_ascii=False, indent=2)
        outfile.write('\n')


def main():
    author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices'])
    author['updated'] = datetime.now(timezone.utc).isoformat()

    os.makedirs('results', exist_ok=True)
    write_json('results/gs_data.json', author)
    write_json('results/gs_data_shieldsio.json', {
        'schemaVersion': 1,
        'label': 'citations',
        'message': str(author.get('citedby', 'N/A')),
    })
    write_json('results/gs_data_hindex.json', {
        'schemaVersion': 1,
        'label': 'h-index',
        'message': str(author.get('hindex', 'N/A')),
    })

    print(f"Citations: {author.get('citedby', 'N/A')}")
    print(f"H-index: {author.get('hindex', 'N/A')}")


if __name__ == '__main__':
    main()
